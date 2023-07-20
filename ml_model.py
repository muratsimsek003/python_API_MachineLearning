import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
import warnings
warnings.filterwarnings("ignore")
# Load the dataset in a dataframe object and include only four features as mentioned
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df_short = df[include]
df_short.head()
#missing value analysis
df_short.isnull().sum()
df_short.dropna(inplace=True)
df_short.info()


df_categorical=df_short.select_dtypes(include=["object"]).copy()

df_columns=df_categorical.columns

from sklearn.preprocessing import LabelEncoder
for i in df_columns:
  lbe = LabelEncoder()
  df_short[i]=lbe.fit_transform(df_short[i])



df_short.head()

import autosklearn.classification



from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import pickle
import warnings
warnings.filterwarnings("ignore")


y=df_short["Survived"]
X=df_short.drop(["Survived"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

RF_model=RandomForestClassifier().fit(X_train,y_train)
y_pred=RF_model.predict(X_test)
RF_skor= accuracy_score(y_test,y_pred)
print('RF Model Accuracy:', RF_skor)
print("Random Forest Classification Report")
print(classification_report(y_test,y_pred))


pickle.dump(RF_model, open("model.pkl", "wb"))
print("Model created")
