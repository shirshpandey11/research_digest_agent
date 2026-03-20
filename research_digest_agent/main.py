from agent.loader import load_sources
from agent.cleaner import clean_text
from agent.extractor_tfidf import extract_claims_tfidf
from agent.grouper_tfidf import group_claims_tfidf
from agent.generator import generate_digest, generate_json

def run_pipeline(inputs):
    print("Loading sources...")
    raw_data = load_sources(inputs)

    if not raw_data:
        print("No valid sources found!")
        return

    all_claims = []
    structured_output = []

    for item in raw_data:
        print(f"Processing: {item['source']}")

        clean = clean_text(item["text"])
        claims = extract_claims_tfidf(clean)

        structured_output.append({
            "source": item["source"],
            "claims": claims
        })

        all_claims.extend(claims)

    print("Grouping claims...")
    groups = group_claims_tfidf(all_claims, num_clusters=3)

    print("Generating outputs...")
    generate_digest(groups)
    generate_json(structured_output)

    print("✅ Done! Check 'output/' folder.")

if __name__ == "__main__":
    inputs = [
        "data/sample1.txt",
        "data/sample2.txt",
        "data/sample3.txt"
    ]

    run_pipeline(inputs)