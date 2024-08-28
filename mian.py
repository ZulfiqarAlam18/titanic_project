import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


#print(train.isnull().sum())


# sns.barplot(x='Sex', y = 'Survived',data = train)
# plt.title('No title')
# plt.show()


# sns.barplot(x='Sex', y='Survived', data=train)
# plt.title('Survival Rate by Gender')
# plt.show()


# train['Age'].hist(bins=30)
# plt.title('Distribution of Age')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()


# sns.pairplot(train, hue='Survived')
# plt.show()

#train['Age'].fillna(train['Age'].median(), inplace=True)

#train['Age'] = train['Age'].fillna(train['Age'].median())

#train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)

train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])

train = train.drop(['Name', 'Ticket', 'PassengerId'], axis=1)


