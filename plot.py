import matplotlib.pyplot as plt
import pandas as pd

pos = []
neg = []
unc = []

data = pd.read_csv('data/processed.csv')
print(data.head())



for index, row in data.iterrows():
    if row['Sentiment'] == 'pos':
        pos.append((row['created_at'], len(pos) + 1))
    elif row['Sentiment'] == 'neg':
        neg.append((row['created_at'], len(neg) + 1))
    else:
        unc.append((row['created_at'], len(unc) + 1))

pos_x = []
for x in pos:
    date = repr(x[0])[1:11]
    pos_x.append(date)
pos_y = [y[1] for y in pos]

neg_x = []
for x in neg:
    date = repr(x[0])[1:11]
    neg_x.append(date)
neg_y = [y[1] for y in neg]

unc_x = []
for x in unc:
    date = repr(x[0])[1:11]
    unc_x.append(date)
unc_y = [y[1] for y in unc]

#plt.plot(pos_x, pos_y)
#plt.plot(neg_x, neg_y)
plt.plot(unc_x, unc_y)
plt.show()



#names = ['Positive', 'Negative', 'Uncertain']
#values = data['values']
#plt.barh(names, values, edgecolor='black')
#for i, v in enumerate(values):
#    plt.text(v + 200, i, str(v), color='black', fontsize='medium', fontweight='normal')

#plt.show()