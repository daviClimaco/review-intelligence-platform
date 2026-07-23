import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# download vader lexicon if not already downloaded
nltk.download("vader_lexicon", quiet=True)


class VaderClassifier:

    def __init__(self) -> None:
        self.analyzer = SentimentIntensityAnalyzer()

    def classify(self, text: str) -> str:
        # returns a dict with neg, neu, pos, compound scores
        scores = self.analyzer.polarity_scores(text)

        # compound score ranges from -1 (most negative) to +1 (most positive)
        compound = scores["compound"]

        if compound >= 0.05:
            return "positive"
        elif compound <= -0.05:
            return "negative"
        else:
            return "neutral"

    def classify_batch(self, texts: list[str]) -> list[str]:
        return [self.classify(text) for text in texts]
