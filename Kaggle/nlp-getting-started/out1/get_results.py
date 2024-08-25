import os
import pandas as pd


if __name__ == '__main__':
    pd_all = pd.read_csv(os.path.join("test_results.tsv"), sep='\t', header=None)

    data = pd.DataFrame(columns=['target'])
    # print(pd_all.shape)

    for index in pd_all.index:
        positive_score = pd_all.loc[index].values[1]
        negative_score = pd_all.loc[index].values[0]

        if max(positive_score, negative_score) == positive_score:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["1"]
        else:
            #data.append(pd.DataFrame([index, "negative"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["0"]
        #print(negative_score, positive_score, negative_score)

    data.to_csv(os.path.join("pre_sample.csv"), sep=',')
    #print(data)
