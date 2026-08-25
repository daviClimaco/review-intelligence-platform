import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# importing our data functions - separating data logic from display logic
# is the same principle as separating Service from Router in the API
from data import load_reviews, load_summary

# st.set_page_config must be the first streamlit call in the file
st.set_page_config(page_title="Review Intelligence Platform", layout="wide")

st.title("Review Intelligence Platform")
st.markdown("Dashboard for analyzing customer reviews.")

# st.cache_data tells streamlit to cache the result of this function
# without it, the data would be reloaded from the database on every interaction
@st.cache_data
def get_data():
    return load_reviews()

df = get_data()
summary = load_summary(df)

# --- OVERVIEW SECTION ---
st.header("Overview")

# st.columns splits the page into N equal columns side by side
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews", summary["total_reviews"])
col2.metric("Average Rating", summary["avg_rating"])
col3.metric("Total Authors", summary["total_authors"])
col4.metric("Total Platforms", summary["total_platforms"])

st.divider()

# --- RATINGS SECTION ---
st.header("Ratings")

# two charts side by side using columns again
col1, col2 = st.columns(2)

with col1:
    st.subheader("Rating Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="rating", hue="rating", palette="Blues_d", legend=False, ax=ax)
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    # st.pyplot renders a matplotlib figure inside streamlit
    st.pyplot(fig)

with col2:
    st.subheader("Average Rating per Category")
    fig, ax = plt.subplots()
    avg = df.groupby("category_name")["rating"].mean().sort_values()
    avg.plot(kind="barh", color="steelblue", ax=ax)
    ax.set_xlabel("Average Rating")
    st.pyplot(fig)

st.divider()

# --- SENTIMENT SECTION ---
st.header("Sentiment Analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots()
    palette = {"positive": "green", "neutral": "gray", "negative": "red"}
    sns.countplot(data=df, x="sentiment", hue="sentiment", palette=palette, legend=False, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Average Rating per Sentiment")
    fig, ax = plt.subplots()
    df.groupby("sentiment")["rating"].mean().sort_values().plot(kind="barh", color="steelblue", ax=ax)
    ax.set_xlabel("Average Rating")
    st.pyplot(fig)

st.divider()

# --- EXPLORER SECTION ---
st.header("Review Explorer")

# selectbox creates a dropdown filter
category_filter = st.selectbox("Filter by category", ["All"] + sorted(df["category_name"].unique()))
sentiment_filter = st.selectbox("Filter by sentiment", ["All", "positive", "neutral", "negative"])
platform_filter = st.selectbox("Filter by platform", ["All"] + sorted(df["platform"].unique()))

# apply filters only when they are not "All"
filtered = df.copy()
if category_filter != "All":
    filtered = filtered[filtered["category_name"] == category_filter]
if sentiment_filter != "All":
    filtered = filtered[filtered["sentiment"] == sentiment_filter]
if platform_filter != "All":
    filtered = filtered[filtered["platform"] == platform_filter]

st.write(f"{len(filtered)} reviews found")

# st.dataframe renders an interactive table
st.dataframe(filtered[["author_name", "category_name", "rating", "sentiment", "review_text", "platform"]])
