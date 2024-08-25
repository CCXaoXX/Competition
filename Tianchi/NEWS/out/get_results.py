import os
import pandas as pd


if __name__ == '__main__':
    pd_all = pd.read_csv(os.path.join("test_results.tsv"), sep='\t', header=None)

    data = pd.DataFrame(columns=['label'])
    # print(pd_all.shape)

    for index in pd_all.index:
        res0 = pd_all.loc[index].values[0]
        res1 = pd_all.loc[index].values[1]
        res2 = pd_all.loc[index].values[2]
        res3 = pd_all.loc[index].values[3]
        res4 = pd_all.loc[index].values[4]
        res5 = pd_all.loc[index].values[5]
        res6 = pd_all.loc[index].values[6]
        res7 = pd_all.loc[index].values[7]
        res8 = pd_all.loc[index].values[8]
        res9 = pd_all.loc[index].values[9]
        res10 = pd_all.loc[index].values[10]
        res11 = pd_all.loc[index].values[11]
        res12 = pd_all.loc[index].values[12]
        res13 = pd_all.loc[index].values[13]


        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res0:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["0"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res1:
            # data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index + 1] = ["1"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res2:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["2"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res3:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["3"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res4:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["4"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res5:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["5"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res6:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["6"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res7:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["7"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res8:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["8"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res9:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["9"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res10:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["10"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res11:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["11"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res12:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["12"]
        if max(res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13) == res13:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["13"]

    data.to_csv(os.path.join("pre_sample.csv"), sep=',')
    #print(data)
