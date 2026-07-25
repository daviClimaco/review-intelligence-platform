import pickle
from pathlib import Path

MODEL_DIR = Path("src/ml/sentiment/models")


class MlClassifier:

    def __init__(self) -> None:
        with open(MODEL_DIR / "vectorizer.pkl", "rb") as f:
            self.vectorizer = pickle.load(f)

        with open(MODEL_DIR / "model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def classify(self, text: str) -> str:
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]

    def classify_batch(self, texts: list[str]) -> list[str]:
        vec = self.vectorizer.transform(texts)
        return list(self.model.predict(vec))
