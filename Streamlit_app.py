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

tab2.subheader("AUDNZD")
tab2.line_chart(datagen()['AUDNZD'])

tab3.subheader("AUDUSD")
tab3.line_chart(datagen()['AUDUSD'])

tab4.subheader("CADJPY")
tab4.line_chart(datagen()['CADJPY'])

tab5.subheader("EURJPY")
tab5.line_chart(datagen()['EURJPY'])

tab6.subheader("EURUSD")
tab6.line_chart(datagen()['EURUSD'])

tab7.subheader("GBPJPY")
tab7.line_chart(datagen()['GBPJPY'])

tab8.subheader("USDJPY")
tab8.line_chart(datagen()['USDJPY'])






