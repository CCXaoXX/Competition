import pandas as pd
from sklearn.model_selection import train_test_split


data_train = pd.read_csv(r'D:\My_Files\Tianchi\NEWS\trainData.csv', sep=',')

x_train, x_test = train_test_split(data_train, train_size=0.9)
x_train.to_csv(r'D:\My_Files\Tianchi\NEWS\train_data1.csv', mode='w', header=['label', 'text'], index=False, sep=',')
x_test.to_csv(r'D:\My_Files\Tianchi\NEWS\test_data.csv', mode='w', header=['label', 'text'], index=False, sep=',')
'''

for index in data_train.itertuples():
    out = []
    out = pd.DataFrame([out])
    label = index[1].split('\t')[0]
    content = index[1].split('\t')[1]
    out[0] = label
    out[1] = content
    out.to_csv(r'D:\My_Files\Tianchi\NEWS\trainData.csv', mode='a', header=False, index=False)
    
'''


