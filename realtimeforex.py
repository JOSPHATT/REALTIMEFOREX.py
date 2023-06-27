import requests
import re  
import json
pairs=[['AUD','JPY'],['AUD','NZD'],['AUD','USD'],['CAD','JPY'],['EUR','JPY'],['EUR','USD'],['GBP','JPY'],['USD','JPY']]
str_url='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=TTNX3GCSG7Z5KVI3'
def data_gen(url):
    r = requests.get(url)
    data = r.json()
    return data

currencies_data={}                                    
from time import sleep
def pairer(pair):                                         
    global str_url
    P1=pair[0]                                            
    P2=pair[1]                                            
    #print(P1,P2)                                         
    start_url=str_url
    s=start_url.replace("USD",P1)
    s1=s.replace('JPY',P2)
    return s1
for currency_pair_lnk in pairs:
    lnk=str(pairer(currency_pair_lnk))
    currencypair=str(currency_pair_lnk[0])+str(currency_pair_lnk[1])                                            
    dta=data_gen(lnk)                                     
    currencies_data[currencypair]=dta
    sleep(20)                                         
#print(currencies_data)                               
fine_data={}                                          
for curr in currencies_data.keys():                       
    val=currencies_data[curr]                             
    #print(val)
    #print(curr)                                          
    prce=float(val['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    fine_data[curr]=prce
def final_data():
    return fine_data
#print(final_data())
#finaldata=final_data()
import time
#time_stamp=time.asctime()
import json
time_stamp=time.asctime()
Final_data={}  
Final_data[time_stamp]=final_data()
filename = 'realtimeforex.json'
entry = final_data()
import os
if os.stat(filename).st_size == 0:
    with open(filename, "w") as file:
        json.dump(Final_data, file)
else:
    with open(filename, "r+") as file:
        data = json.load(file)
        data[time_stamp]=entry
        file.seek(0)
        json.dump(data, file)


