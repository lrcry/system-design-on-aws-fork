# Preface

System design is a disciplined art, so let’s create some large-scale masterpieces.

*System Design on AWS* is a comprehensive guide to helping software architects and engineers understand, build, and scale complex systems on the Amazon Web Services (AWS) cloud. The book provides a structured approach to tackling real-world system design challenges on AWS in a continuously evolving cloud landscape. The material focuses on fundamental principles, architectural trade-offs, and practical use cases, guiding you from Day 0 (minimum viable product) to Day N (most valuable product). Through detailed chapters, this book demystifies AWS’s wide-ranging services and how they can be strategically leveraged to address both technical and business requirements.

# How This Book Is Organized

Organized into three core parts, this book begins by establishing a foundation in system design, then dives into the essential AWS services for building resilient architectures, and concludes with practical system design use cases. Foundational system design patterns, scaling mechanisms, caching strategies, network protocols, and deployment strategies are covered. By exploring these elements in a cloud context, the book offers a toolkit for approaching and solving large-scale design problems in any industry. Each part opener breaks down the chapters included in that part, so take a look at those openers for details. This book aims to equip you with:

* A solid understanding of fundamental system design principles and trade-offs
* Proficiency in key AWS services and their roles in building large-scale systems
* Insight into real-world use cases that illustrate how to structure and deploy scalable architectures on AWS
* Strategies to balance performance, scalability, and cost in AWS cloud environments

# What This Book Isn’t

This book does not provide detailed code implementations for deploying the infrastructure or application business logic. Instead, it emphasizes the architecture and design process, helping you understand how to break a system down into manageable components and make informed architectural decisions.

# Who Should Read This Book

This book is ideal for software architects, developers, DevOps engineers, and system architects who want to build or scale applications on AWS. It is especially useful for professionals transitioning from on-premises to cloud infrastructure or aiming to leverage AWS for large-scale applications. A basic understanding of software implementation and familiarity with one programming language are recommended.

This book is also recommended for people holding leadership positions in software development and DevOps. The guidance and principles in the book will help you remove team blockers while building systems and making informed decisions.

While this book is titled *System Design on AWS* and the focus is on the AWS cloud, we recommend it to everyone who loves to build systems on any of the cloud providers’ platforms or for on-premises data centers as well as anyone who is just curious about building systems. The design and scaling principles discussed in the book are agnostic of cloud providers.

# Conventions Used in This Book

The following typographical conventions are used in this book:

*Italic*
:   Indicates new terms, URLs, email addresses, filenames, and file extensions.

`Constant width`
:   Used for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.

**`Constant width bold`**
:   Shows commands or other text that should be typed literally by the user.

*`Constant width italic`*
:   Shows text that should be replaced with user-supplied values or by values determined by context.

###### Note

This element signifies a general note.

Many of the tools and services discussed in these pages are abbreviated on repeated mentions for your convenience. For example, *Amazon Elastic Compute Cloud* is sometimes called *Amazon EC2* or just *EC2*.

# O’Reilly Online Learning

###### Note

For more than 40 years, [*O’Reilly Media*](https://oreilly.com) has provided technology and business training, knowledge, and insight to help companies succeed.

Our unique network of experts and innovators share their knowledge and expertise through books, articles, and our online learning platform. O’Reilly’s online learning platform gives you on-demand access to live training courses, in-depth learning paths, interactive coding environments, and a vast collection of text and video from O’Reilly and 200+ other publishers. For more information, visit [*https://oreilly.com*](https://oreilly.com).

# How to Contact Us

Please address comments and questions concerning this book to the publisher:

* O’Reilly Media, Inc.
* 1005 Gravenstein Highway North
* Sebastopol, CA 95472
* 800-889-8969 (in the United States or Canada)
* 707-827-7019 (international or local)
* 707-829-0104 (fax)
* [*support@oreilly.com*](mailto:support@oreilly.com)
* [*https://oreilly.com/about/contact.html*](https://oreilly.com/about/contact.html)

We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at [*https://oreil.ly/SystemDesignOnAWS*](https://oreil.ly/SystemDesignOnAWS).

For news and information about our books and courses, visit [*https://oreilly.com*](https://oreilly.com).

Find us on LinkedIn: [*https://linkedin.com/company/oreilly-media*](https://linkedin.com/company/oreilly-media).

Watch us on YouTube: [*https://youtube.com/oreillymedia*](https://youtube.com/oreillymedia).

# Acknowledgments

This book is the culmination of insights, experience, and feedback from numerous collaborators and industry experts. We thank our colleagues, reviewers, and readers for their contributions and dedication to advancing cloud-based system design.

We extend our sincere gratitude to the entire O’Reilly team, both visible and behind the scenes, for their contributions and feedback on this book. We would not have met with the O’Reilly team without an introduction from John Culkin and his expert review of our early proposal of this book. We would like to thank Megan Laddusaw for support on the book proposal and getting the chapters outline ready. A special thanks to Melissa Potter, our development editor, for her patience and support. Her initial reviews were incredibly helpful in structuring the content and helped make the book more valuable.

A big thanks to Swami Sivasubramanian for taking the time to write a wonderful foreword; his words perfectly set the stage, and we couldn’t have asked for a better introduction. Thank you to Harshit Bangar, Rakesh Kumar, Neha Shetty, Dinesh Chittibala, Alankrit Kharbanda, Kristina Manukyan, and Rohn Arya for reviewing the book and providing many helpful suggestions and insightful comments.

We would also like to thank the Dragonfly DB team for sponsoring the two early-release chapters on their website and making them freely available for the tech community. Special thanks to all the companies out there publishing detailed engineering blogs and sharing the innovations and deep dives.

## Mandeep Singh

I would like to thank my wonderful wife, Priyanka, for her patience and encouragement and for putting up with me spending long hours writing. I am forever grateful to my parents for enabling me to achieve my dreams and always putting my interests before theirs. Thanks to all my family members for their support and guidance.

Thanks to my college, Army Institute of Technology, for introducing me to computer science and helping me become a disciplined individual. Thanks to all the amazing opportunities I had working at different organizations: AWS, Amazon, Jupiter, and Skytap (a Kyndryl company). I met a lot of amazing folks, and they have greatly shaped my thinking around decision making and systems building. I would also like to thank my friends, teachers, and professional connections for suggestions and discussions along the way.

The idea of writing a book would never have originated without my coauthor, Jayanth. Thanks for sharing the opportunity with me—the entire writing of this book has been entirely a new experience and learning for me.

## Jayanth Kumar

This book is a heartfelt expression of gratitude to my family and all the teachers who have guided me throughout my life. I am forever grateful for their support, encouragement, and wisdom that have profoundly shaped who I am. I got the inspiration to author such a technical book from my professors, [Pushpak Bhattacharya](https://en.wikipedia.org/wiki/Pushpak_Bhattacharyya) and [George Varghese](https://en.wikipedia.org/wiki/George_Varghese), who infected me with their enthusiasm for the music of systems and algorithmics.

I owe much of my journey to the institutions that nurtured my curiosity and skills: my alma maters IIT Bombay and the University of California, Los Angeles. These environments were instrumental in developing my foundation and pushing me to explore new horizons in technology and system design.

My career has been a canvas of experiences, shaped by incredible mentors and colleagues at SAP, Goodhealthapp, Delhivery, Amazon, and Turl Street Group. Each role allowed me to build and scale systems through various growth stages, from 0 to 1 at Goodhealthapp (startup), 1 to 10 at Delhivery (unicorn), 10 to 1,000 at SAP (enterprise), and 1,000+ at Amazon (FAANG), and each taught me invaluable lessons in resilience, adaptability, and innovation.

This book could not have come to life without the dedication of my coauthor, Mandeep Singh, who tirelessly worked alongside me, often burning the midnight oil to cover ground where I left off. His commitment and attention to detail have been invaluable in bringing this work to completion.

There are a lot of folks whom I wish I could mention individually, whose contributions, guidance, and shared knowledge shaped this book, but I am constrained by space, so please know that your impact is felt and appreciated. I am also indebted to the broader tech community, whose inspiration fuels my dedication to this field. It is my hope that this book will add value to our shared pursuit of innovation and learning.
