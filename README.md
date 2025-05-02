# 📦 amazon-reviews

📊 EDA of 50K+ Amazon app reviews. Includes text cleaning, score trends, wordclouds, and top liked reviews using pandas, matplotlib, and wordcloud.

---

## ⚙️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/thepeoplethings/amazon-reviews.git
cd amazon-reviews

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt

cd notebooks
jupyter notebook eda.ipynb

🗂️ Folder Structure

amazon-reviews/
├── data/
│   └── raw/
│       └── amazon_reviews.csv
├── notebooks/
│   └── eda.ipynb
├── src/
│   └── data/
│       └── load_data.py
├── stopwords.txt
├── .venv/
└── README.md

🧪 Objectives
Understand overall user satisfaction through score distribution

Identify key themes in positive and negative reviews

Analyze trends over time

Find reviews with the most likes (thumbsUpCount)

📊 Key Findings
⭐ Majority of reviews are 5-star, but 1-star reviews are also significant

🔍 Negative reviews frequently mention delays, crashes, or wishlist bugs

🕒 Weekly trend shows stable review count with occasional score dips

👍 Most-liked reviews are usually critical and highly detailed

🧹 Data Cleaning Steps
Lowercasing & removing punctuation

Removing stopwords (custom stopwords.txt)

Created cleaned columns:

clean_content

clean_no_stopwords

📈 Visualizations
Barplot of score distribution

Wordcloud (overall, positive vs negative)

Time series: review count & average score per week

Weekly comparison: positive vs negative reviews

🧰 Tools Used
Python 3.12

pandas, matplotlib, wordcloud

Jupyter Notebook (VSCode)

Manual stopword loading due to SSL issue on Mac

👩‍💻 Author
Shifa Chairunissa
Data Analyst in training with a passion for customer behavior and review analysis.
