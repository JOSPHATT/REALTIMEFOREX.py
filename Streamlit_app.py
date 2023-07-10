import streamlit as st
import requests

github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json
p = requests.get(github_url)
p.text
github_jsonforex_dictionary=json.loads(p.text)
Total_entries=print(len(github_jsonforex_dictionary.values()))github_url="https://raw.githubusercontent.com/JOSPHATT/REALTIMEFOREX.py/main/realtimeforex.json"
import json
p = requests.get(github_url)
p.text
github_jsonforex_dictionary=json.loads(p.text)
#Total_entries=print(len(github_jsonforex_dictionary.values()))
