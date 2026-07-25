import sys
from pathlib import Path

# add project root to Python path so 'src' is found
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
from sqlalchemy import create_engine

# importing settings from our config module - this is why we centralized
# the database config there instead of repeating os.getenv() everywhere
from src.core.config import settings


def get_engine():
    # create_engine doesnt open a connection immediately
    # it just sets up the "factory" - the connection only opens when we query
    return create_engine(settings.DATABASE_URL)


def load_reviews() -> pd.DataFrame:
    engine = get_engine()

    # instead of querying each table separately and merging in Python (slow),
    # we let PostgreSQL do the JOIN - much more efficient for larger datasets
    # this is the same query we used in the notebook, now reusable as a function
    query = """
        SELECT
            r.id,
            r.rating,
            r.sentiment,
            r.review_text,
            r.platform,
            r.created_at,
            a.name as author_name,
            c.name as category_name
        FROM review r
        JOIN author a ON r.author_id = a.id
        JOIN category c ON r.category_id = c.id
    """

    # pd.read_sql runs the query and returns a DataFrame directly
    # no need to fetch rows manually like we would with psycopg2
    return pd.read_sql(query, engine)


def load_summary(df: pd.DataFrame) -> dict:
    # receives the DataFrame instead of querying again
    # reusing data already in memory is always better than a new db call
    return {
        "total_reviews": len(df),
        "avg_rating": round(df["rating"].mean(), 2),
        "total_authors": df["author_name"].nunique(),    # nunique = count distinct
        "total_platforms": df["platform"].nunique(),
    }
