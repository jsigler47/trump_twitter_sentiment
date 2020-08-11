import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data/totals.csv', names=['sent', 'values'])
#print(data.head())

names = ['Positive', 'Negative', 'Uncertain']
values = data['values']
plt.bar(names, values)
plt.show()