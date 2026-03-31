# Foreword

Systems design is one of the most important aspects of building apps that are scalable, available, performant, and secure, even when your usage increases by an order of magnitude or two. That’s why I found the topic of this book to be so important. I like that this book starts with covering the basics of trade-offs in distributed systems, such as the CAP theorem, units of blast radius, and other common trade-offs in systems design, and then moves to how to apply these principles in practice. I found this approach—going from core principles to actually putting them into practice on critical design decisions (such as “What is the best database for running my workload?” and “What’s the best caching strategy for my workloads?” and “Which storage service should I choose?”)—to be especially helpful as it teaches people how to think about these problems even as new capabilities from AWS emerge, making the concepts in this book more durable.

Personally, reading this book reminded me so much of the early days of AWS, when we spent a lot of time discussing these trade-offs. At that time, concepts like CAP theorem, blast radius, and seamless scalability were not well understood, and we had robust discussions around these topics and the inherent trade-offs they come with. However, those discussions led to some incredibly robust AWS services, such as S3, DynamoDB, and many others that millions of AWS customers love. I hope the you grasp these concepts and are inspired to build similarly amazing products and services that delight their customers.

Congratulations to the authors for writing such an excellent book, and best of luck to all who embark on this journey!

Swami Sivasubramanian,

Vice President, AI and Data at AWS
