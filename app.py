import pandas as pd
from textblob import TextBlob
import streamlit as st
import matplotlib.pyplot as plt

# 🎨 Microsoft style
st.set_page_config(page_title="InsightPulse", page_icon="💬", layout="wide")
st.markdown("""
    <style>
    .stApp {background-color: #f7f9fc;}
    h1, h2, h3 {color: #0078d4;}
    </style>
""", unsafe_allow_html=True)

# 🧠 App title
st.title("💬 InsightPulse: User Feedback Sentiment Analyzer")
st.write("Upload your feedback file (CSV with a 'Review' column) to get instant insights!")

# 📂 File uploader
uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'Review' not in df.columns:
        st.error("CSV must contain a column named 'Review'")
    else:
        # 🧮 Sentiment analysis
        df['Sentiment'] = df['Review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        df['Category'] = df['Sentiment'].apply(
            lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
        )

        # 📊 Metrics row
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🧾 Total Reviews", len(df))
        col2.metric("😊 Positive", (df['Category'] == 'Positive').sum())
        col3.metric("😐 Neutral", (df['Category'] == 'Neutral').sum())
        col4.metric("😞 Negative", (df['Category'] == 'Negative').sum())

        # 📈 Sentiment distribution chart
        st.subheader("📊 Sentiment Distribution")
        st.bar_chart(df['Category'].value_counts())

        # 📅 Sentiment trend
        df['Index'] = range(1, len(df)+1)
        st.subheader("📈 Sentiment Trend Over Reviews")
        st.line_chart(df[['Index', 'Sentiment']].set_index('Index'))

        # 🧾 Data preview
        st.subheader("🧾 Data Preview")
        st.dataframe(df[['Review', 'Sentiment', 'Category']])
else:
    st.info("👆 Upload a CSV file to begin!")

