# Translation Decisions: foreword.html

## Overview
This is the foreword by Swami Sivasubramanian, Vice President of AI and Data at AWS. It is a short endorsement discussing distributed systems principles and AWS services. The tone is personal and inspirational.

## Key Translation Decisions

| Term | Translation | Rationale |
|------|-------------|-----------|
| Foreword | 推荐序 | Standard Chinese book term for a foreword written by a third party (as opposed to 前言, which is written by the author); 推荐序 fits because this is written by an AWS VP |
| CAP theorem | CAP 定理 | Universally used in Chinese CS literature; glossary entry #803 |
| blast radius | 爆炸半径 | AWS official CN translation confirmed in Well-Architected Reliability Pillar; glossary entry #804 |
| units of blast radius | 爆炸半径的量化单位 | "units of" rendered as "量化单位" to convey the idea of measuring/scoping the blast radius |
| trade-offs | 权衡取舍 | Standard Chinese rendering; used throughout the book |
| scalable / scalability | 可扩展 / 可扩展性 | Glossary entry #75 |
| available / availability | 高可用 | Standard Chinese rendering |
| performant | 高性能的 | Direct equivalent; "performant" has no single Chinese word, rendered as 高性能的 |
| workload | 工作负载 | Glossary entry #655 (workload management); 工作负载 is the standard AWS CN term |
| caching strategy | 缓存策略 | Glossary entry #86 (cache eviction policy uses 缓存 as base word) |
| seamless scalability | 无缝扩展 | "seamless" rendered as 无缝; "scalability" as 扩展 (shortened from 可扩展性 for fluency) |
| "order of magnitude" | 数量级 | Standard Chinese mathematical/technical term |
| "robust discussions" | 大量深入的讨论 | "robust" here means thorough/substantive, not technically "robust"; 深入 (in-depth) captures the intent |
| "incredibly robust AWS services" | 极为强健的 AWS 服务 | 强健 (strong and robust) better captures the engineering robustness than 健壮 in this context |
| "delight their customers" | 令用户爱不释手 | Idiomatic Chinese for products users love; more vivid than the literal 让用户满意 |
| Vice President, AI and Data at AWS | AWS 人工智能与数据业务副总裁 | Full Chinese title per standard corporate title conventions |
| "I hope the you grasp" | 我希望你能真正领会 | Source has a typo ("the you"); corrected in translation; 领会 (truly grasp/internalize) more idiomatic than 理解 |
| "best of luck to all who embark on this journey" | 祝所有踏上这段旅程的读者一切顺利 | Standard Chinese well-wishing closing |

## Structural Decisions
- Three content paragraphs preserved with identical paragraph boundaries.
- Byline structure preserved with `class="byline"` and `class="byline cont"` intact.
- The `id` attribute on the `<section>` tag preserved verbatim.
- Source typo ("I hope the you grasp") silently corrected in translation.
