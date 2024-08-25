import os
import pandas as pd


if __name__ == '__main__':
    pd_all = pd.read_csv(os.path.join("test_results.tsv"), sep='\t', header=None)

    data = pd.DataFrame(columns=['score'])
    # print(pd_all.shape)

    for index in pd_all.index:
        res0 = pd_all.loc[index].values[0]
        res025 = pd_all.loc[index].values[1]
        res05 = pd_all.loc[index].values[2]
        res075 = pd_all.loc[index].values[3]
        res1 = pd_all.loc[index].values[4]

        if max(res0, res025, res05, res075, res1) == res0:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["0"]
        if max(res0, res025, res05, res075, res1) == res025:
            # data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index + 1] = ["0.25"]
        if max(res0, res025, res05, res075, res1) == res05:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["0.5"]
        if max(res0, res025, res05, res075, res1) == res075:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["0.75"]
        if max(res0, res025, res05, res075, res1) == res1:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["1"]

    data.to_csv(os.path.join("pre_sample.csv"), sep=',')
    #print(data)
