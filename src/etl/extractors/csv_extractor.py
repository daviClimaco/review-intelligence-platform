import csv
from pathlib import Path

class CsvExtractor:

    def __init__(self, file_path: str) -> None:
        # stores the path to the CSV file
        self.file_path = Path(file_path)

    def extract(self) -> list[dict]:
        # check if file exists before trying to read
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        rows = []
        with open(self.file_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))

        print(f"[Extractor] {len(rows)} rows extracted from {self.file_path.name}")
        return rows
