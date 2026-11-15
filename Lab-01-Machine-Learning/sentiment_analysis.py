import pandas as pd
import re

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DATA_DIR = Path("data")

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def load_dataset(filename):
    records = []

    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")

            if not line.strip():
                continue

            text, label = line.rsplit("\t", 1)

            records.append({
                "text": text.strip(),
                "label": int(label.strip())
            })

    return pd.DataFrame(records)


# Load all three datasets
amazon = load_dataset("amazon_cells_labelled.txt")
imdb = load_dataset("imdb_labelled.txt")
yelp = load_dataset("yelp_labelled.txt")

# Combine datasets
data = pd.concat([amazon, imdb, yelp], ignore_index=True)

# Apply text cleaning
data["clean_text"] = data["text"].apply(clean_text)

# Display original and cleaned text
print("\nOriginal and Cleaned Text:")
print(data[["text", "clean_text"]].head())

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nSentiment distribution:")
print(data["label"].value_counts())

# Display positive reviews
print("\nPositive Reviews:")
print(data[data["label"] == 1]["clean_text"].head(5))

# Display negative reviews
print("\nNegative Reviews:")
print(data[data["label"] == 0]["clean_text"].head(5))

from collections import Counter

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Positive words without stop words
positive_words = [
    word
    for text in data[data["label"] == 1]["clean_text"]
    for word in text.split()
    if word not in ENGLISH_STOP_WORDS
]

positive_frequency = Counter(positive_words)

print("\nTop 10 Positive Words:")
print(positive_frequency.most_common(10))

# Negative words without stop words
negative_words = [
    word
    for text in data[data["label"] == 0]["clean_text"]
    for word in text.split()
    if word not in ENGLISH_STOP_WORDS
]

negative_frequency = Counter(negative_words)

print("\nTop 10 Negative Words:")
print(negative_frequency.most_common(10))

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(7, 5))

sns.countplot(data=data, x="label")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment (0 = Negative, 1 = Positive)")
plt.ylabel("Number of Reviews")

plt.xticks([0, 1], ["Negative", "Positive"])

plt.show()

# Separate features and target
X = data["clean_text"]
y = data["label"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining and Testing Data:")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# Create Bag of Words model
bow_vectorizer = CountVectorizer()

# Fit on training data and transform
X_train_bow = bow_vectorizer.fit_transform(X_train)

# Transform testing data
X_test_bow = bow_vectorizer.transform(X_test)

print("\nBag of Words Results:")
print("Training data shape:", X_train_bow.shape)
print("Testing data shape:", X_test_bow.shape)

# Task 6 - TF-IDF

tfidf_vectorizer = TfidfVectorizer()

X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

print("\nTF-IDF Results:")
print("Training data shape:", X_train_tfidf.shape)
print("Testing data shape:", X_test_tfidf.shape)

# Task 7 - Train Machine Learning Model

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

print("\nModel Training Completed!")

# Task 8 - Model Evaluation

print("\nModel Evaluation:")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Precision:", precision_score(y_test, y_pred))

print("Recall:", recall_score(y_test, y_pred))

print("F1 Score:", f1_score(y_test, y_pred))

print("\nClassification Report:")

print(classification_report(y_test, y_pred))

# Task 9 - Test New Review

new_review = ["The product is excellent and works perfectly"]

new_review_tfidf = tfidf_vectorizer.transform(new_review)

prediction = model.predict(new_review_tfidf)

print("\nNew Review Prediction:")
print("Positive" if prediction[0] == 1 else "Negative")