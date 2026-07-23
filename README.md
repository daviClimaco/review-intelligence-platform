# Review Intelligence Platform

An end-to-end review intelligence platform built to study software architecture, data engineering, analytics, machine learning and AI.

## Goals

- Learn Software Architecture & System Design
- Learn Data Engineering & ETL
- Learn Machine Learning & NLP
- Build an end-to-end real-world project

## Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn
- Pandas
- Scikit-learn
- NLTK (VADER)
- Jupyter Notebook

## Status

- (DONE) Planning & Architecture
- (DONE) Project Structure & Python Environment Setup
- (DONE) PostgreSQL + SQLAlchemy Configuration
- (DONE) Database Modeling (Author, Category, Review)
- (DONE) FastAPI Setup & Swagger Documentation
- (DONE) Backend Architecture (Repositories, Services, Schemas, Routers)
- (DONE) ETL Pipeline (CSV Extractor, Transformer, Loader)
- (DONE) Exploratory Data Analysis (EDA)
- (DONE) NLP & Sentiment Analysis (VADER)
- (DOING) Machine Learning (Logistic Regression + TF-IDF)
- (WAITING) Dashboard & Analytics
- (WAITING) AI Assistant (RAG)
- (WAITING) Docker & Deployment

## Architecture

```
src/
├── api/
│   └── routers/          # HTTP layer (FastAPI routers)
├── core/
│   └── config.py         # Centralized settings (Pydantic)
├── database/             # SQLAlchemy engine and session
├── models/               # ORM entities (Author, Category, Review)
├── schemas/              # Pydantic DTOs (Create, Update, Response)
├── repositories/         # Data access layer (CRUD)
├── services/             # Business logic layer
├── etl/
│   ├── extractors/       # Data extraction (CSV)
│   ├── transformers/     # Data cleaning and normalization
│   └── loaders/          # Database persistence via repositories
├── ml/
│   └── sentiment/        # Sentiment analysis (VADER + ML)
└── utils/                # Shared utilities

notebooks/
├── 01_eda.ipynb                  # Exploratory data analysis
└── 02_sentiment_analysis.ipynb   # Sentiment distribution and validation

data/
└── raw/                  # Raw input datasets
```

## Running the project

```bash
# activate virtual environment
source .venv/Scripts/activate  # Git Bash
.venv\Scripts\activate         # PowerShell

# start the API
uvicorn src.main:app --reload

# run ETL pipeline
python -m src.etl.pipeline data/raw/reviews.csv

# run sentiment analysis
python -m src.ml.sentiment.updater

# start Jupyter
jupyter notebook
```

API docs available at `http://localhost:8000/docs`

## Dataset

Google Maps Restaurant Reviews — 1100 reviews across 100 restaurants.
Categories: taste, menu, indoor_atmosphere, outdoor_atmosphere.

## Key Insights (EDA)

- 70% of reviews are rated 4 or 5 stars (positive bias)
- Menu category has the lowest average rating (3.69)
- Negative reviews tend to be slightly longer than positive ones
- VADER classified 76% positive, 14% negative, 9% neutral
- Strong correlation between sentiment and rating (negative avg: 2.55, positive avg: 4.25)
