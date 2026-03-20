import json
import os

def generate_digest(groups, filename="output/digest.md"):
    os.makedirs("output", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Research Digest\n\n")

        for i, group in enumerate(groups, 1):
            f.write(f"## Theme {i}\n")

            for claim in group:
                f.write(f"- {claim['claim']}\n")

            f.write("\n")

def generate_json(data, filename="output/sources.json"):
    os.makedirs("output", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)