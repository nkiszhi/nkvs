import pandas as pd
import os
url='https://androzoo.uni.lu/api/download?apikey=527405107e220d29dcc813ab6ae0f6180fcf039bf35c4221f69aae91569424eb&sha256='
df = pd.read_csv('./latest.csv/latest.csv')
list_sha256 = list(df['sha256'])
with open('url_list.txt','wb') as f:
    for item in list_sha256:
        f.write(url+item+'\n')
print('file saved')
