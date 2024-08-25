import pandas as pd
from sklearn.model_selection import train_test_split


path = r"D:\My_Files\Kaggle\us-patent-phrase-to-phrase-matching\train.csv"

train = pd.read_csv(path, sep=',')
x_train, x_test = train_test_split(train, train_size=0.9)

x_train.to_csv(r'D:\My_Files\Kaggle\us-patent-phrase-to-phrase-matching\train_data.txt', mode='w', index=False, sep='\t')
x_test.to_csv(r'D:\My_Files\Kaggle\us-patent-phrase-to-phrase-matching\test_data.txt', mode='w', index=False, sep='\t')