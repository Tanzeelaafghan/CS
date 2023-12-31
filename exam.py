# -*- coding: utf-8 -*-
"""exam

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17JsmNPwMKu959_hhS_CKGPO7Nw-cL01M
"""

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn import metrics

#Load & Explore the Dataset
df=pd.read_csv('/content/fish.csv')
df

df.head()

df.info()

df.isnull().sum()

df.describe()

df.columns

#Select the feature and target variable
X = df.drop('Species', axis=1)
y = df['Species']

# Spliting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Create a Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Training the model
model.fit(X_train, y_train)

# Predict the response for the test dataset
y_pred = model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display additional classification metrics
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))