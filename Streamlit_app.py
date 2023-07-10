import streamlit as st
import requests

github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json
p = requests.get(github_url)
github_jsonforex_dictionary=json.loads(p.text)

import pandas as pd
from pandas import json_normalize
column_names=[i for i in github_jsonforex_dictionary.keys()]
df = pd.DataFrame(github_jsonforex_dictionary.values())
"""Timeseries=pd.DataFrame(github_jsonforex_dictionary.keys())
times=Timeseries.values.tolist()
Tyms=[]
for tym in times:
    s=tym[0]
    p=[' '.join(s.split())]
    n_p=p[0].split()
    r=n_p[3].split(":")
    f=r[0]+r[1]+r[2]
    d=n_p[2]+f
    Tyms.append(int(d))
Timestamps=pd.DataFrame(Tyms)
DF=df.T
DF.columns=column_names
DF=DF.rename_axis(['currency_pair']).reset_index()"""
st.title('MY LIVE FOREX')
st.header('AUDJPY')
st.line_chart(df['AUDJPY'])
