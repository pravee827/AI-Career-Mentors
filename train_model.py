import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("job_roles.csv")

X = df["skills"]
y = df["role"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(X, y)

with open("role_predictor.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")