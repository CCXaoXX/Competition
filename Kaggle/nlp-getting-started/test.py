import pandas as pd
import torch
import os
from summarizer import Summarizer
import re

# 使用GPU加速
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
print(torch.cuda.is_available())


def summer(body):
    model = Summarizer()
    num = model.calculate_optimal_k(body, k_max=10)
    result = model(body, num_sentences=num, min_length=1, max_length=10240)
    full = ''.join(result)
    return full


# re过滤
def re_clean(text):
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除@
    text = re.sub(r"\[\S+\]", "", text)  # 去除表情符号
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s('
        r')<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)  # 去除网址
    text = re.sub('[^a-zA-Z.,?!\']', ' ', text).lower()  # 保留英文内容及标点
    # text = re.sub('[^a-zA-Z]', ' ', text).lower()  # 保留英文内容
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s+", " ", text)  # 去除多余空格
    text = text.split()
    return text


# 停用词表
def stop_word(change):
    # 获取停用词表
    stop = []
    standard_stop = []
    file_stop = r'D:\\My_Files\\stopwords.txt'
    with open(file_stop, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        for line in lines:
            change_line = line.strip()
            stop.append(change_line)

    for i in range(0, len(stop)):
        for word in stop[i].split():
            standard_stop.append(word)

    # 使用停用词表
    after = []
    for w in change:
        if w not in standard_stop and len(w) < 15:  # 停用词表
            for ii in range(len(w) - 2):
                if w[ii] == w[ii + 1] and w[ii] == w[ii + 2]:
                    break  # 过滤异状单词
                else:
                    after.append(w)
                    break

    return after


# 读取文件
path = r"D:\Desktop\nlp-getting-started\train.csv"
path_test = r"D:\Desktop\nlp-getting-started\test.csv"
data = pd.read_csv(path, sep=',', encoding='ISO-8859-1')
data_test = pd.read_csv(path, sep=',', encoding='ISO-8859-1')

from bert_serving.client import BertClient

# 向量提取
bc = BertClient(port=86500, port_out=86501, show_server_config=True, timeout=1000000)
# 文件处理
i = 0
for wi in data['text']:
    wi = wi.lower()
    wi = re.sub('[0-9]', '', wi)
    wi = re.sub('#', '', wi)
    vec_text = bc.encode([str(wi)])
    data['text'][i] = vec_text
    i += 1
    print(vec_text)

i = 0
for wi in data_test['text']:
    wi = wi.lower()
    wi = re.sub('[0-9]', '', wi)
    wi = re.sub('#', '', wi)
    vec_text = bc.encode([str(wi)])
    data_test['text'][i] = vec_text
    i += 1

from sklearn.linear_model import LogisticRegression

FinalModel = LogisticRegression(max_iter=1000, C=3)
FinalModel.fit(data['text'], data['target'])

pred = FinalModel.predict(data_test['text'])

FinalModel.score(pred, data_test['target'])
