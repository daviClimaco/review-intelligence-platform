# Review Intelligence Platform

An end-to-end review intelligence platform built to study software architecture, data engineering, analytics, machine learning and AI.

## Goals

- Learn Software Architecture
- Learn System Design
- Learn Data Engineering
- Learn Machine Learning
- Learn AI & NLP
- Build an end-to-end real-world project

## Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn

## Status

- (DONE) Planning & Architecture
- (DONE) Project Structure
- (DONE) Python Environment Setup
- (DONE) PostgreSQL Configuration
- (DONE) SQLAlchemy Setup
- (DONE) Database Modeling (Author, Category, Review)
- (DONE) FastAPI Setup
- (DONE) Initial API & Swagger Documentation
- (DONE) Backend Architecture (Repositories, Services, Schemas & Routers)
- (DONE) ETL Pipeline (CSV Extractor, Transformer & Loader)
- (DOING) Data Processing & Analysis
- (WAITING) NLP & Sentiment Analysis
- (WAITING) Machine Learning
- (WAITING) Dashboard & Analytics
- (WAITING) AI Assistant (RAG)
- (WAITING) Docker & Deployment

## Architecture

The project follows a layered architecture inspired by Java/Spring Boot:

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
│   ├── extractors/       # Data extraction (CSV, future: scraping)
│   ├── transformers/     # Data cleaning and normalization
│   └── loaders/          # Database persistence via repositories
├── ml/                   # Machine learning models (coming soon)
└── utils/                # Shared utilities
```

## Running the project

```bash
# activate virtual environment
source .venv/Scripts/activate

# start the API
uvicorn src.main:app --reload

# run ETL pipeline
python -m src.etl.pipeline data/raw/reviews.csv
```

API docs available at `http://localhost:8000/docs`

## About

End-to-end review intelligence platform built to study software architecture, data engineering, analytics, machine learning and AI.
