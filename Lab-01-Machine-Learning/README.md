
# Lab 01 – Machine Learning: Sentiment Analysis

## 1. Laboratory Objective

The objective of this laboratory session is to understand the basic concepts of Natural Language Processing (NLP) and Machine Learning by developing a sentiment analysis model.

The model classifies text reviews into two categories:
- Positive (1)
- Negative (0)

## 2. Tasks and Implementation

### Task 1 – Dataset Loading
Loaded the Amazon, IMDb, and Yelp labelled datasets and combined them into a single dataset.

### Task 2 – Text Preprocessing
Performed basic text preprocessing:
- Converted text into lowercase.
- Removed unnecessary characters and punctuation.
- Removed extra whitespace.
- Created a new column named `clean_text`.

### Task 3 – Text Data Exploration
- Examined positive and negative reviews.
- Identified frequently occurring words.
- Compared common words in positive and negative reviews.
- Visualized sentiment distribution.

### Task 4 – Train-Test Split
Divided the dataset into:
- Training data: 80% (2,400 samples)
- Testing data: 20% (600 samples)

### Task 5 – Text Representation
Applied two text representation techniques:
- Bag of Words (BoW)
- Term Frequency–Inverse Document Frequency (TF-IDF)

### Task 6 – Model Training
Trained a Logistic Regression model using TF-IDF features.

### Task 7 – Model Evaluation
Evaluated the model using:
- Accuracy
- Precision
- Recall
- F1-score

### Task 8 – New Review Prediction
Tested the trained model using a new review:
"The product is excellent and works perfectly"

The model predicted the review as Positive.

## 3. Results and Evidence

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 83.33% |
| Precision | 81.45% |
| Recall | 86.33% |
| F1-score | 83.82% |

The model achieved an accuracy of 83.33% on the test dataset.

## 4. Observations

- Text preprocessing helped prepare reviews for machine learning.
- Positive and negative reviews contained different frequently occurring words.
- Both BoW and TF-IDF were explored for text representation.
- TF-IDF features were used to train the Logistic Regression model.
- The model successfully predicted a new positive review.

## 5. Learning Outcomes

After completing this laboratory, I gained practical experience in:

- Loading and exploring text datasets using Python.
- Performing basic NLP text preprocessing.
- Understanding Bag of Words and TF-IDF.
- Splitting datasets into training and testing sets.
- Training a Logistic Regression classification model.
- Evaluating machine learning models.
- Predicting sentiment for new text reviews.

## 6. Tools and Technologies

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- VS Code

## 7. AI Assistance Declaration

AI tools were used for technical guidance, learning support, and debugging assistance during this laboratory activity. The implementation and results were reviewed and understood by the student.

 
