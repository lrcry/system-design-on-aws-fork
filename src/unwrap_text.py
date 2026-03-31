#!/usr/bin/env python3
"""
unwrap_text.py - 将 Markdown 文件中被硬换行 (Hard Wrap) 切断的段落合并为单行。

用法:
    python3 unwrap_text.py <file1.md> [file2.md ...]
    python3 unwrap_text.py --all          # 处理 markdown/ 下所有 chXX.md

原理:
    Markdown 源文件为了排版，每行约 80~100 字符就强制换行，
    但同一段落的行之间没有空行。本脚本把属于同一段落/列表项/引用块/
    定义列表的多行合并为一行，方便后续翻译时做逐行对照。

    脚本只改变换行符位置，不增删任何文字内容。

保留不动的结构:
    - 标题 (# ...)
    - 代码块 (``` ... ```)
    - 图片 (![...)
    - 空行（段落分隔符）
"""

import re
import sys
import glob
import os


def flush_buffer(result, buffer, buffer_type):
    """将缓冲区中的行合并为一行，追加到 result。"""
    if not buffer:
        return

    if buffer_type == 'blockquote':
        # 去掉每行的 '> ' 或 '>' 前缀，合并后重新加上 '> '
        parts = []
        for line in buffer:
            text = re.sub(r'^>\s?', '', line)
            parts.append(text)
        merged = ' '.join(parts)
        result.append('> ' + merged + '\n')

    elif buffer_type == 'list':
        # 第一行是列表项起始，后续是缩进续行
        first = buffer[0].rstrip()
        rest = [line.strip() for line in buffer[1:]]
        if rest:
            merged = first + ' ' + ' '.join(rest)
        else:
            merged = first
        result.append(merged + '\n')

    elif buffer_type == 'definition':
        # :   开头的定义体，续行有 4+ 空格缩进
        first = buffer[0].rstrip()
        rest = [line.strip() for line in buffer[1:]]
        if rest:
            merged = first + ' ' + ' '.join(rest)
        else:
            merged = first
        result.append(merged + '\n')

    else:  # 'text'
        parts = [line.strip() for line in buffer]
        merged = ' '.join(parts)
        result.append(merged + '\n')

    buffer.clear()


def process_file(filepath):
    """处理单个文件，将多行段落合并为单行。"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    buffer = []
    buffer_type = 'text'  # 'text' | 'blockquote' | 'list' | 'definition'
    in_code_block = False

    for line in lines:
        stripped = line.rstrip('\n')

        # ── 代码块开关 ──
        if stripped.lstrip().startswith('```'):
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'text'
            in_code_block = not in_code_block
            result.append(line)
            continue

        # 代码块内部：原样保留
        if in_code_block:
            result.append(line)
            continue

        # ── 空行：段落分隔 ──
        if not stripped.strip():
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'text'
            result.append(line)
            continue

        # ── 标题行 ──
        if re.match(r'^#{1,6}\s', stripped):
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'text'
            result.append(line)
            continue

        # ── 图片行 ──
        if stripped.strip().startswith('!['):
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'text'
            result.append(line)
            continue

        # ── 引用块 ──
        if stripped.startswith('>'):
            # '>' 单独一行是引用块内的段落分隔符
            if stripped.strip() == '>':
                flush_buffer(result, buffer, buffer_type)
                buffer_type = 'text'
                result.append(line)
                continue
            # 引用块续行
            if buffer_type == 'blockquote':
                buffer.append(stripped)
            else:
                flush_buffer(result, buffer, buffer_type)
                buffer_type = 'blockquote'
                buffer.append(stripped)
            continue

        # ── 列表项起始 ──
        if re.match(r'^\s*[\*\-\+]\s', stripped) or re.match(r'^\s*\d+\.\s', stripped):
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'list'
            buffer.append(stripped)
            continue

        # ── 定义列表起始 (:   ) ──
        if re.match(r'^:\s{3,}', stripped):
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'definition'
            buffer.append(stripped)
            continue

        # ── 列表项续行（2+ 空格缩进） ──
        if buffer_type == 'list' and re.match(r'^\s{2,}', stripped):
            buffer.append(stripped)
            continue

        # ── 定义体续行（4+ 空格缩进） ──
        if buffer_type == 'definition' and re.match(r'^\s{4,}', stripped):
            buffer.append(stripped)
            continue

        # ── 普通文本 ──
        if buffer_type == 'text':
            buffer.append(stripped)
        else:
            # 前一个结构结束，开始新的文本段落
            flush_buffer(result, buffer, buffer_type)
            buffer_type = 'text'
            buffer.append(stripped)

    # 文件末尾：刷新剩余缓冲
    flush_buffer(result, buffer, buffer_type)

    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(result)

    print(f"✓ {filepath}")


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 unwrap_text.py <file1.md> [file2.md ...]")
        print("  python3 unwrap_text.py --all   # 处理 markdown/ 下所有 chXX.md")
        sys.exit(1)

    if sys.argv[1] == '--all':
        script_dir = os.path.dirname(os.path.abspath(__file__))
        md_dir = os.path.join(script_dir, '..', 'markdown')
        files = sorted(glob.glob(os.path.join(md_dir, '*.md')))
        if not files:
            print(f"未找到 Markdown 文件: {md_dir}/*.md")
            sys.exit(1)
    else:
        files = sys.argv[1:]

    for f in files:
        if not os.path.isfile(f):
            print(f"✗ 文件不存在: {f}")
            continue
        process_file(f)

    print(f"\n完成，共处理 {len(files)} 个文件。")


if __name__ == '__main__':
    main()
