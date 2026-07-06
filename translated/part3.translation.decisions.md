# Translation Decisions: part3.html

## Overview
Part III opener introducing system design use cases (ch14–ch21). Contains the epigraph by Kernighan and Plauger, a general introduction to the Part III methodology, the chapter outline structure, learning outcomes, and summaries of 8 use-case chapters.

## Key Translation Decisions

| Term | Translation | Rationale |
|------|-------------|-----------|
| System Design Use Cases (part title) | 系统设计实战案例 | 实战 (practical/real-world) added to 案例 to better convey "hands-on use cases" over a dry literal translation |
| epigraph | 现在交付九成功能，远胜于永远交付不了的百分之百。 | Kernighan & Plauger quote; adapted for natural Chinese rhythm; "delivered now" → 现在交付, "delivered never" → 永远交付不了 |
| Brian Kernighan and P. J. Plauger | 布莱恩·柯尼汉 和 P. J. 普劳格尔 | Standard Chinese transliterations |
| Day 0 architecture | Day 0 架构（初日架构） | Glossary #381 |
| Day N architecture | Day N 架构 | Glossary #382 |
| minimum viable product | 最小可行产品 | Glossary #807; "MVP" acronym omitted in running text for fluency |
| most valuable product | 最有价值产品 | Consistent with Day 0/N glossary entry #381 |
| Make It Work, Make It Right, Make It Fast | 先让它跑起来，再让它做对，最后让它快起来 | Glossary #383 |
| Amazon DynamoDB | Amazon DynamoDB | Glossary #260 |
| Docstore | Docstore | Proper name, kept as-is |
| functional and nonfunctional requirements | 功能性需求与非功能性需求 | Glossary #368 and #369 |
| "one thousand customers" | 约为一千人 | 约 added for natural Chinese; direct context from "say, one thousand customers" |
| bottlenecks | 瓶颈 | Standard Chinese technical term |
| best practices | 最佳实践 | Standard Chinese translation |
| "Make sure the system is extensible enough" | 只需确保系统具备足够的可扩展性 | 可扩展性 from glossary #75; 足够的 captures "extensible enough" |
| URL shorteners | URL 短链服务 | Standard Chinese rendering |
| web crawlers | 网络爬虫 | Standard Chinese technical term |
| social network | 社交网络 | Standard Chinese term |
| newsfeed system | 新闻信息流系统 | 信息流 for "feed" is widely used in Chinese social media context |
| leaderboards | 排行榜 | Standard Chinese gaming term |
| hotel reservation system | 酒店预订系统 | Standard Chinese term |
| booking conflicts and transaction handling | 预订冲突和事务处理 | Standard terms; 事务 for transaction in DB context |
| chat application | 聊天应用程序 | Standard Chinese term |
| video processing pipeline | 视频处理流水线 | Standard Chinese term; 流水线 for pipeline |
| stockbroker application | 股票经纪商应用程序 | Glossary #766 |
| "from 0 to 1 at startup" | 初创企业从 0 到 1 | Omitted; this phrase appears in pr01, not part3 |
| "So let's dive in" | 让我们一起投入其中 | Natural Chinese closing for an energetic call-to-action |

## Structural Decisions
- Figure tag with `id` and `img src` preserved verbatim.
- Nested `<ol>` structure for chapter outline preserved exactly.
- `<a contenteditable="false" data-type="indexterm">` index markers preserved verbatim.
- External link to Make It Work principle preserved verbatim.
- External link to Docstore preserved verbatim.
- All `data-type="xref"` links preserved verbatim.
- `class="keep-together"` on "interruptions" preserved.
