import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sqlalchemy import create_engine

from src.core.config import settings

# model output directory
MODEL_DIR = Path("src/ml/sentiment/models")
MODEL_DIR.mkdir(exist_ok=True)


def label_from_rating(rating: float) -> str:
    if rating <= 2:
        return "negative"
    elif rating == 3:
        return "neutral"
    else:
        return "positive"


def run_training() -> None:
    print("[Trainer] Loading data from database...")

    engine = create_engine(settings.DATABASE_URL)
    df = pd.read_sql("SELECT review_text, rating FROM review", engine)

    # create labels from ratings
    df["label"] = df["rating"].apply(label_from_rating)

    print(f"[Trainer] {len(df)} reviews loaded")
    print(df["label"].value_counts())

    X_train, X_test, y_train, y_test = train_test_split(
        df["review_text"], df["label"], test_size=0.2, random_state=42
    )

    # vectorize text with TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # train logistic regression
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # evaluate
    y_pred = model.predict(X_test_vec)
    print("\n[Trainer] Classification Report:")
    print(classification_report(y_test, y_pred))

    # save model and vectorizer
    with open(MODEL_DIR / "vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    with open(MODEL_DIR / "model.pkl", "wb") as f:
        pickle.dump(model, f)

    print(f"[Trainer] Model saved to {MODEL_DIR}")


if __name__ == "__main__":
    run_training()
