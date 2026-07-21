from src.database.session import SessionLocal
from src.etl.extractors.csv_extractor import CsvExtractor
from src.etl.transformers.review_transformer import ReviewTransformer
from src.etl.loaders.review_loader import ReviewLoader


def run_pipeline(file_path: str) -> None:
    print("[Pipeline] Starting ETL pipeline...")

    # step 1: extract raw data from CSV
    extractor = CsvExtractor(file_path)
    raw_rows = extractor.extract()

    # step 2: transform and normalize the raw data
    transformer = ReviewTransformer()
    clean_rows = transformer.transform(raw_rows)

    # step 3: load into the database
    db = SessionLocal()
    try:
        loader = ReviewLoader(db)
        loader.load(clean_rows)
    finally:
        db.close()

    print("[Pipeline] ETL pipeline completed successfully.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m src.etl.pipeline <path_to_csv>")
        sys.exit(1)

    run_pipeline(sys.argv[1])
