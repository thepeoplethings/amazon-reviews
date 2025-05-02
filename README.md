# amazon-reviews
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
