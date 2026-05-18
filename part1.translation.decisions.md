# Translation Decisions: part1.html

## Overview
Part I opener introducing system design fundamentals (ch01–ch08). Contains the epigraph by Antoine de Saint-Exupéry, a bullet-point overview of learning outcomes, and brief chapter synopses.

## Key Translation Decisions

| Term | Translation | Rationale |
|------|-------------|-----------|
| System Design Basics (part title) | 系统设计基础 | Direct, standard Chinese translation |
| epigraph (Saint-Exupéry quote) | 完美并非无物可加，而是无物可删。 | Classic Chinese rendering of this well-known quote; preferred over more literal variants |
| trade-offs | 权衡取舍 | Established glossary rendering used throughout the book |
| scalability | 可扩展性 | Glossary #75 |
| reliability | 可靠性 | Glossary #805 |
| maintainability | 可维护性 | Glossary #806 |
| file, block, and object stores | 文件存储、块存储和对象存储 | Glossary #7, #8, #9 |
| relational and nonrelational databases | 关系数据库与非关系数据库 | Glossary #15, general usage |
| partitioning, indexing, replication, federation, sharding, denormalization | 分区、索引、复制、联合、分片和反范式化 | Established glossary translations from ch02/ch03 |
| content delivery networks (CDNs) | 内容分发网络（CDN） | Glossary #117–125 |
| load balancers | 负载均衡器 | Standard glossary term from ch05 |
| API gateways | API 网关 | Standard glossary term |
| reverse proxies | 反向代理 | Standard glossary term |
| Open Systems Interconnection (OSI) | 开放系统互连（OSI） | Standard Chinese technical term |
| TCP/IP | TCP/IP | Kept as-is; universally recognized |
| fallacies of distributed computing | 分布式计算谬误 | Standard Chinese rendering of Deutsch's 8 fallacies |
| CAP theorem | CAP 定理 | Glossary #803 |
| blast radius | 爆炸半径 | Glossary #804 |
| key-value, wide-column, document, and graph databases | 键值数据库、宽列数据库、文档数据库和图数据库 | Established glossary translations from ch03 |
| quorum-based replication | 基于法定人数的复制 | Established glossary term from ch03 |
| consistent hashing | 一致性哈希 | Established glossary term from ch03 |
| eventual consistency | 最终一致性 | Established glossary term |
| write-through, read-through, refresh-ahead, write-back, cache-aside | 直写、读穿、提前刷新、写回、旁路缓存 | Established glossary translations from ch04 |
| Layer 4 (L4) / Layer 7 (L7) | 第 4 层（L4）/ 第 7 层（L7） | Standard Chinese network layer naming |
| sticky sessions | 粘性会话 | Established glossary term from ch05 |
| UDP | 用户数据报协议（UDP） | Standard Chinese translation |
| SMTP | SMTP | Kept as acronym; widely recognized |
| XMPP | 可扩展消息与存在协议（XMPP） | Full expansion on first mention |
| REST, WebRTC, GraphQL | REST、WebRTC、GraphQL | All kept as-is; recognized technical acronyms |
| containerization | 容器化 | Standard Chinese translation |
| Docker containers | Docker 容器 | Established glossary term from ch07 |
| cloud native | 云原生 | Established glossary term |
| message brokers | 消息代理 | Established glossary term from ch08 |
| message queues | 消息队列 | Established glossary term from ch08 |
| publisher-subscriber patterns | 发布-订阅模式 | Established glossary term |
| microservices | 微服务 | Established glossary term |
| monolithic designs | 单体设计 | Established glossary term |
| serverless architecture | 无服务器架构 | Established glossary term |
| saga pattern | Saga 模式 | Established glossary term; "Saga" kept as proper name |
| event-sourcing pattern | 事件溯源模式 | Established glossary term |
| big data architectures | 大数据架构 | Standard Chinese term |
| domain-driven design | 领域驱动设计 | Established glossary term |
| "Part II" reference | "第二部分" → rendered as 第二部分/Part II via xref | xref links preserved verbatim |

## Structural Decisions
- All `data-type="xref"` links and `href` attributes preserved verbatim.
- `class="keep-together"` on "maintainability" / "applications" preserved.
- Epigraph attribution "Antoine de Saint-Exupéry" rendered as 安托万·德·圣-埃克苏佩里 (standard Chinese transliteration).
- "In Part I, you will:" rendered as "学完第一部分，你将能够：" — active, idiomatic Chinese for learning objectives.
