# Translation Decisions: part2.html

## Overview
Part II opener introducing AWS-managed services (ch09–ch13). Contains the epigraph by Mark Hill, a bullet-point overview of learning outcomes, and brief chapter synopses with AWS service names.

## Key Translation Decisions

| Term | Translation | Rationale |
|------|-------------|-----------|
| Diving Deep into AWS Services (part title) | 深入 AWS 服务 | "Diving Deep" rendered as 深入 (in-depth / deep-dive); common Chinese phrasing for technical deep-dives |
| epigraph "Big and dumb is better." | 大而简，胜于小而繁。 | Mark Hill's quote about processor design philosophy; adapted for natural Chinese; literal "大而笨更好" sounds awkward; 大而简（big and simple）captures the intent |
| machine learning (ML) | 机器学习（ML） | Standard Chinese translation |
| well-architected framework | 架构完善的框架 | AWS Well-Architected Framework; kept descriptive rather than translating as a proper name since the part intro uses it generically |
| workloads | 工作负载 | Glossary #655 |
| virtual private cloud (VPC) | 虚拟私有云（VPC） | Established glossary term from ch09 |
| NAT gateways | NAT 网关 | Established glossary term from ch09 |
| Amazon Route 53 | Amazon Route 53 | AWS service name kept as-is |
| Amazon CloudFront | 亚马逊 CloudFront | Glossary #125 |
| AWS Elastic Load Balancer (ELB) | AWS 弹性负载均衡（ELB） | Established glossary term from ch09 |
| Amazon API Gateway | Amazon API 网关 | Established glossary term |
| Amazon EBS | 亚马逊弹性块存储（EBS） | Glossary #3 |
| Amazon EFS | 亚马逊弹性文件系统（EFS） | Glossary #1 |
| Amazon S3 | 亚马逊简单存储服务（S3） | Glossary #4 |
| Amazon RDS | Amazon 关系数据库服务（RDS） | Glossary #5 |
| Amazon Aurora | Amazon Aurora | Glossary #6; no Chinese name confirmed |
| Amazon DynamoDB | Amazon DynamoDB | Glossary #260; no Chinese name |
| Amazon DocumentDB | Amazon DocumentDB | Glossary #261 |
| Amazon Keyspaces / Timestream / Neptune | Amazon Keyspaces / Timestream / Neptune | AWS service names kept as-is per established convention |
| Amazon ElastiCache | Amazon ElastiCache | AWS service name kept as-is |
| Amazon EC2 | 亚马逊弹性计算云（EC2） / Amazon EC2 | Glossary #2; short form EC2 used on repeat mention |
| AWS Lambda | AWS Lambda | Established glossary term from ch11 |
| Amazon ECR | 亚马逊弹性容器注册表（ECR） | Established glossary term from ch11 |
| AWS Fargate | AWS Fargate | Established glossary term from ch11 |
| Amazon ECS | 亚马逊弹性容器服务（ECS） | Established glossary term from ch11 |
| Amazon EKS | 亚马逊弹性 Kubernetes 服务（EKS） | Established glossary term from ch11 |
| Amazon SQS | 亚马逊简单队列服务（SQS） | Established glossary term from ch12 |
| Amazon SNS | 亚马逊简单通知服务（SNS） | Established glossary term from ch12 |
| Amazon MSK | Amazon Managed Streaming for Apache Kafka（MSK） | Established glossary term from ch12 |
| Amazon Kinesis | Amazon Kinesis | Established glossary term from ch12 |
| AWS Step Functions | AWS Step Functions | Established glossary term from ch12 |
| Amazon CloudWatch | Amazon CloudWatch | Established glossary term from ch12 |
| AWS IAM | AWS 身份与访问管理（IAM） | Established glossary term from ch12 |
| Amazon Cognito | Amazon Cognito | Established glossary term from ch12 |
| AWS AppSync | AWS AppSync | Established glossary term from ch12 |
| Amazon Redshift | Amazon Redshift | Glossary #237 |
| Amazon EMR | Amazon Elastic MapReduce（EMR） | Glossary #236 |
| Amazon Athena | Amazon Athena | Established glossary term from ch13 |
| AWS Glue | AWS Glue | Established glossary term from ch13 |
| Amazon QuickSight | Amazon QuickSight | Established glossary term from ch13 |
| ML pipelines | ML 数据流水线 | Standard Chinese rendering; 流水线 for pipeline |
| "You'll know how to build a strong, secure cloud infrastructure" | 能够构建强健、安全的云基础设施 | Shortened for fluency; 强健 used for "strong" in infrastructure context |

## Structural Decisions
- All `data-type="xref"` links preserved verbatim.
- `class="pagebreak-before less_space"` preserved on the bullet point.
- Epigraph attribution "Mark Hill" rendered as 马克·希尔.
- "At the end of Part II, you will:" → "学完第二部分，你将能够：" — consistent with Part I pattern.
- AWS service full names introduced on first mention in each chapter synopsis; shortened forms used on subsequent references within the same paragraph.
