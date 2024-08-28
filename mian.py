import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


print(train.isnull().sum())