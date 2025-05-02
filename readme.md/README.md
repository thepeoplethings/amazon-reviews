
---

## 🧪 Objectives

- Understand overall user satisfaction through score distribution
- Identify key themes in positive and negative reviews
- Analyze trends over time
- Find reviews with the most likes (thumbsUpCount)

---

## 📊 Key Findings

- ⭐ Majority of reviews are 5-star, but 1-star reviews are also significant
- 🔍 Negative reviews frequently mention delays, crashes, or wishlist bugs
- 🕒 Weekly trend shows stable review count with occasional score dips
- 👍 Most-liked reviews are usually critical and highly detailed

---

## 🧹 Data Cleaning Steps

- Lowercasing & removing punctuation
- Removing stopwords (custom `stopwords.txt`)
- Optional stemming (Porter Stemmer)
- Cleaned versions saved as new DataFrame columns

---

## 📈 Visualizations

- Barplot of score distribution
- Wordclouds (overall, positive, negative)
- Time series: review count & average score per week
- Weekly comparison: positive vs negative reviews

---

## 💡 Tools Used

- Python 3.12
- Pandas, Matplotlib, WordCloud
- Jupyter Notebook (VSCode)

---

## 📌 Next Steps

- Add sentiment classification using TextBlob or Vader
- Integrate this with dashboard tools (e.g. Streamlit)
- Run clustering on review themes using NLP techniques

---

## 👩‍💻 Author

Shifa Chairunissa  
*Data Analyst in training with a passion for customer behavior analysis.*