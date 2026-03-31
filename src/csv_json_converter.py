import csv
import json
import os
import sys
from datetime import datetime


def csv_to_json(csv_path, json_path=None):
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not json_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_path = os.path.join(os.path.dirname(csv_path), f"glossary_{timestamp}.json")

    output = json.dumps(rows, ensure_ascii=False, indent=2)

    with open(json_path, "w", encoding="utf-8") as f:
        f.write(output + "\n")

    print(f"Output: {json_path}")


def json_to_csv(json_path, csv_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON root must be a list of objects")

    if not csv_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = os.path.join(os.path.dirname(json_path), f"glossary_{timestamp}.csv")

    if not data:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            f.write("")
        print(f"Output: {csv_path}")
        return

    fieldnames = list(data[0].keys())
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Output: {csv_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input.(csv|json)>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    input_ext = os.path.splitext(input_path)[1].lower()

    if input_ext == ".csv":
        csv_to_json(input_path)
    elif input_ext == ".json":
        json_to_csv(input_path)
    else:
        print("Input file must be .csv or .json", file=sys.stderr)
        sys.exit(1)
