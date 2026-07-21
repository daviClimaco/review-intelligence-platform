class ReviewTransformer:

    # maps CSV column names to our model field names
    FIELD_MAP = {
        "author_name": "author_name",
        "text": "review_text",
        "rating": "rating",
        "rating_category": "category_name",
        "business_name": "platform",
    }

    def transform(self, raw_rows: list[dict]) -> list[dict]:
        transformed = []

        for row in raw_rows:
            # skip rows with empty text or missing rating
            if not row.get("text") or not row.get("rating"):
                continue

            transformed.append({
                "author_name": row["author_name"].strip(),
                "review_text": row["text"].strip(),
                "rating": float(row["rating"]),          # "5" → 5.0
                "category_name": row["rating_category"].strip(),
                "platform": row["business_name"].strip(),
                "sentiment": None,                       # filled later by NLP pipeline
                "review_date": None,                     # not available in this dataset
            })

        print(f"[Transformer] {len(transformed)} rows transformed (skipped {len(raw_rows) - len(transformed)})")
        return transformed
