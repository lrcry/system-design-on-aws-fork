from __future__ import annotations

import argparse
from pathlib import Path


def has_cjk(text: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in text)


def lstrip_preserve_newline(text: str) -> str:
    stripped = text.lstrip()
    if text.endswith("\n") and not stripped.endswith("\n"):
        return stripped + "\n"
    return stripped


def strip_english(lines: list[str]) -> list[str]:
    output: list[str] = []
    in_code_block = False
    pending_list_kind: str | None = None
    pending_list_number: str | None = None
    previous_blank = False

    for line in lines:
        if line.startswith("```"):
            in_code_block = not in_code_block
            output.append(line)
            pending_list_kind = None
            pending_list_number = None
            previous_blank = False
            continue

        if in_code_block:
            output.append(line)
            continue

        if line.strip() == "":
            if not previous_blank:
                output.append(line)
            previous_blank = True
            continue

        if line.startswith(">") and line.strip() == ">":
            output.append(line)
            previous_blank = False
            continue

        if line.startswith("![") or line.startswith("[!["):
            output.append(line)
            previous_blank = False
            continue

        if line.startswith("|"):
            output.append(line)
            previous_blank = False
            continue

        if line[:2] in {": ", ":\t"} and has_cjk(line):
            output.append(line)
            previous_blank = False
            continue

        if line.startswith("* ") and not has_cjk(line):
            pending_list_kind = "bullet"
            pending_list_number = None
            continue

        if ". " in line and not has_cjk(line):
            prefix, _, _ = line.partition(". ")
            if prefix.isdigit():
                pending_list_kind = "ordered"
                pending_list_number = prefix
                continue

        if has_cjk(line):
            normalized = line
            if pending_list_kind == "bullet":
                normalized = "* " + lstrip_preserve_newline(line)
            elif pending_list_kind == "ordered" and pending_list_number is not None:
                normalized = f"{pending_list_number}. " + lstrip_preserve_newline(line)
            output.append(normalized)
            pending_list_kind = None
            pending_list_number = None
            previous_blank = False
            continue

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Strip English source text from bilingual Markdown.")
    parser.add_argument("path", nargs="?", default="markdown/ch03.md", help="Markdown file to rewrite in place.")
    args = parser.parse_args()

    file_path = Path(args.path)
    original = file_path.read_text(encoding="utf-8")
    stripped = "".join(strip_english(original.splitlines(keepends=True)))
    file_path.write_text(stripped, encoding="utf-8")


if __name__ == "__main__":
    main()
