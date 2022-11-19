import numpy as np
import pandas as pd
import os
import re
from collections import defaultdict
path = 'C:/Users/k5000/Desktop/정류장 파일'
folder = os.listdir(path)
date = pd.date_range(start='10/1/2022', end='10/30/2022')
folder = sorted(folder, key = lambda s: int(re.search(r'\d+', s).group()))

for i in folder:
    each = path + "/" + i
    e_list = os.listdir(each)
    e_list = sorted(e_list, key = lambda s: int(re.search(r'\d+', s).group()))
    print(e_list)
    clean_df = pd.Series(date)
    clean_values = []

    for j in e_list:
        data = pd.read_csv(each + "/" + j, encoding = 'euc-kr')
        if type(data.노선[0]) != np.int64:
            data = data[data.노선.str.contains('511')]
        data = data[data.이용자유형.str.contains('일반인')].reset_index().drop('index',axis=1)
        index = data.columns.tolist()[14]
        bus_quit = data.columns.tolist()[15]
        ans = data.loc[:, index] - data.loc[:, bus_quit]

        for k in range(0, len(ans)):
            print(ans[k])
            clean_values.append(ans[k])
    print(clean_values)
    clean_df = pd.Series(clean_values, index = clean_df)
    print(clean_df)