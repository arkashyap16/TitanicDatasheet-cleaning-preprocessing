import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('Titanic-Dataset.csv') 


print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)

df.fillna({'Age': df['Age'].median()}, inplace=True)
df.fillna({'Embarked':df['Embarked'].mode()},inplace = True)
df.drop(columns=['Cabin'], inplace=True)

df['Sex'] = df['Sex'].map({'male': 0 , 'female': 1})

df = pd.get_dummies(df, columns= ['Embarked'], drop_first= True)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

sns.boxplot(data=df[['Fare']])
plt.title('Fare Outliers')
plt.show()

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['Fare'] < (Q1 - 1.5 * IQR)) | (df['Fare'] > (Q3 + 1.5 * IQR)))]


df.to_csv('cleaned_Titanic-Dataset.csv', index=False)
print("Cleaned dataset saved successfully!")