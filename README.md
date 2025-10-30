💬 InsightPulse:
By simply uploading a CSV file of reviews, the app instantly analyzes tone (Positive, Neutral, or Negative) and visualizes key trends through interactive charts.
The name InsightPulse comes from the idea of feeling the pulse of user feedback: Capturing insights in real time to understand what users truly feel about a product.

🧠 Why I Built This
During my 6th semester, I noticed how companies often collect tons of user feedback but struggle to interpret it quickly.
So I built InsightPulse: A lightweight tool that translates raw text into data-driven insights within seconds.

🚀 Features
1)Upload any CSV file with a Review column
2)Automatic Sentiment Detection (Positive / Neutral / Negative)
3)Interactive Dashboards with charts and metrics
4)Trend Insights showing sentiment changes over time
5)Simple, clean Microsoft-style interface

💡Working of InsightPulse
1)Upload Data – The user uploads a CSV file containing customer reviews.
2️)Sentiment Analysis – Each review is analyzed using TextBlob to detect whether it’s positive, negative, or neutral.
3️)Categorization – Reviews are automatically grouped by sentiment.
4️)Visualization – The app displays metrics and a bar chart showing sentiment distribution.
5️)Instant Insights – Product teams can instantly see what users like or dislike — no manual analysis needed.

🛠️ Technologies Used
1)Python – for data processing and sentiment analysis
2)Streamlit – for interactive web app and dashboard
3)Pandas – for handling and cleaning user feedback data
4)TextBlob – for sentiment classification
5)Matplotlib / Plotly – for visualization of sentiment trends

⚙️ How to Run Locally (Commands)
git clone https://github.com/Shriya-23/InsightPulse.git
cd InsightPulse
pip install -r requirements.txt
streamlit run app.py

☁️ Live Demo
🚀 Try it here: https://insightpulse23.streamlit.app/
(Deployed using Streamlit Cloud)

💼 About Me Hi! 
I’m Shriya Sharma, a Computer Science student passionate about building practical, data-driven solutions that connect technology with real-world impact.
I enjoy creating simple, meaningful tools that help turn insights into smarter decisions.

Then open 👉 http://localhost:8501
