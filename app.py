import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata_sample.csv")
    # Convert publish_time to datetime
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    # Extract year
    df["year"] = df["publish_time"].dt.year
    # Abstract word count
    df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# App Layout
st.title("CORD-19 Data Explorer")
st.write("Simple interactive exploration of COVID-19 research papers")

# Sidebar Filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Select year range",
    int(df["year"].min()),
    int(df["year"].max()),
    (2020, 2021)
)

# Filter dataset
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Show Data Sample
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# Publications Over Time
st.subheader("Publications Over Time")
year_counts = filtered_df["year"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_title("Number of Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax, palette="viridis")
ax.set_title("Top 10 Journals Publishing COVID-19 Research")
ax.set_xlabel("Paper Count")
st.pyplot(fig)

# Source Distribution
st.subheader("Distribution of Papers by Source")
source_counts = filtered_df["source_x"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 4))
source_counts.plot(kind="bar", ax=ax, color="orange")
ax.set_title("Top 10 Sources")
ax.set_xlabel("Source")
ax.set_ylabel("Count")
st.pyplot(fig)

# Word Cloud (Safe)
st.subheader("Word Cloud of Paper Abstracts")
text = " ".join(filtered_df["abstract"].dropna())

try:
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        font_path="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"  # Adjust if needed
    ).generate(text)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

except ValueError as e:
    st.warning("WordCloud generation failed on this system. Skipping visualization.")

# Footer
st.markdown("---")
st.write("Built with Streamlit | Assignment Project")