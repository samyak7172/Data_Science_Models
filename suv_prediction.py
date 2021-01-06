# -*- coding: utf-8 -*-
"""SUV_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qjIrDpUgbE9KAg9u8J8VqzjmNr0Vjp3v
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/SUV_prediction.csv')
df.head(10)

sns.countplot(x='Gender',data=df)

sns.barplot(x='Gender',y='Purchased',data=df)

df.isnull().sum()

X = df.iloc[:,[2,3]].values
y = df.iloc[:,4].values

print(y)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=None)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()

logmodel.fit(X_train,y_train)

prediction = logmodel.predict(X_test)

from sklearn.metrics import classification_report

classification_report(y_test,prediction)

from sklearn.metrics import accuracy_score,confusion_matrix

confusion_matrix(y_test,prediction)

accuracy_score(y_test,prediction)

confusion_matrix(y_test,prediction)
