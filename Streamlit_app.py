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
pairs=["AUDJPY","AUDNZD","AUDUSD","CADJPY","EURJPY","EURUSD","GBPJPY","USDJPY"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([i for i in pairs])
tab1.subheader("AUDJPY")
tab1.line_chart(datagen()['AUDJPY'])

tab2.subheader("AUDUSD")
tab2.write(datagen()['AUDUSD'])
