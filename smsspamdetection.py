# -*- coding: utf-8 -*-
"""SMSspamDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mnzpv8niP3bDm14sIysPp2BHr9l8VoCS
"""

!pip install pandas scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv('spam.csv', encoding='latin-1')


data.head()

data = data[['v1', 'v2']]

data.columns = ['label', 'message']


data['label'] = data['label'].map({'ham': 0, 'spam': 1})


data.isnull().sum()

X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)

tfidf = TfidfVectorizer(max_features=3000)


X_train_tfidf = tfidf.fit_transform(X_train)


X_test_tfidf = tfidf.transform(X_test)

model = MultinomialNB()


model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)


accuracy = accuracy_score(y_test, y_pred)


print(f'Accuracy: {accuracy * 100:.2f}%')


print(classification_report(y_test, y_pred))


print(confusion_matrix(y_test, y_pred))