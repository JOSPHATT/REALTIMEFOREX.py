import streamlit as st
import requests

github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json

with open('realtimeforex.json') as f:
  github_jsonforex_dictionary = json.load(f)

import pandas as pd
from pandas import json_normalize
column_names=[i for i in github_jsonforex_dictionary.keys()]
def datagen():
  return pd.DataFrame(github_jsonforex_dictionary.values())
st.title('MY LIVE FOREX')
st.header('AUDJPY')
df=datagen()
st.dataframe(df)
AUDJPY_data=df['AUDJPY']
st.line_chart(AUDJPY_data)
