from sqlalchemy.orm import Session

from src.database.session import SessionLocal
from src.ml.sentiment.vader_classifier import VaderClassifier
from src.models.review import Review


def run_sentiment_update() -> None:
    print("[Sentiment] Starting sentiment analysis...")

    db: Session = SessionLocal()
    classifier = VaderClassifier()

    try:
        # fetch only reviews without sentiment
        reviews = db.query(Review).filter(Review.sentiment == None).all()
        print(f"[Sentiment] {len(reviews)} reviews to classify")

        for review in reviews:
            review.sentiment = classifier.classify(review.review_text)

        db.commit()
        print("[Sentiment] Sentiment update completed successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    run_sentiment_update()
