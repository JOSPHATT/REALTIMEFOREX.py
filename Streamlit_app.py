import streamlit as st
import requests

github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json

import pandas as pd
def datagen():
  with open('realtimeforex.json') as f:
    github_jsonforex_dictionary = json.load(f)
  return pd.DataFrame(github_jsonforex_dictionary.values())

st.title('MY LIVE FOREX')
st.header('AUDJPY')
st.line_chart(datagen()['AUDJPY'])
