# DDIA

We can use this simple script to convert from csv to json or vice versa.
We use google sheet to align glossary and it's the single source of truth.
We use json format of glossary as an attachment for AI, as json is friendly for LLM read.

1. download csv file from google sheet
1. execute the script to convert to json
1. attach the json file
1. use shared prompt in prompt.md

## glossary generation for LLM
```
# from csv to json
auto/dev-environment python src/csv_json_converter.py glossary/glossary.csv 
# from json to csv
auto/dev-environment python src/csv_json_converter.py glossary/glossary_for_ai.json
```

## unwrap text for better diff
For more details, please see [here](./docs/unwrap_text.md).
```
auto/dev-environment python src/unwrap_text.py markdown/ch01.md
```

## References
- [wiki - Quorum](https://zh.wikipedia.org/wiki/Quorum_(%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F))
