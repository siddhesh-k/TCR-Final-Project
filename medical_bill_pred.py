import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv(r"../data/insurance.csv")
# print(dataset.head())
# print (dataset.describe())
# print(dataset.shape)

f, ax = plt.subplots(figsize=(15,10))
sns.set(style="ticks")
# sns.distplot(dataset['charges'])
# sns.set_context("paper")
ax.legend(ncol= 2, loc ="upper right",frameon =True)
# plt.show()

charges_by_region = dataset['charges'].groupby(dataset['region']).sum().sort_values(ascending = True)
# sns.barplot(charges_by_region)
# ax =sns.barplot(charges_by_region.head(), charges_by_region.head().index, palette='Blues')
# plt.show()

# ax = sns.barplot(x='region', y='charges', hue='sex', data=dataset, palette='cool')
# plt.show()

# ax = sns.barplot(x = 'region', y = 'charges', hue='smoker', data=dataset, palette='Reds_r')
# plt.show()

# ax = sns.barplot(x='region', y='charges', hue='children', data=dataset, palette='Set1')
# plt.show()

from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
label.fit(dataset.sex.drop_duplicates())
dataset.sex = label.transform(dataset.sex)
label.fit(dataset.smoker.drop_duplicates())
dataset.smoker = label.transform(dataset.smoker)
label.fit(dataset.region.drop_duplicates())
dataset.region = label.transform(dataset.region)
# print(dataset.dtypes)
print(dataset)