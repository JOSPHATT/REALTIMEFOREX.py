import requests
import json
from lxml import html
import pandas as pd
from matplotlib import pyplot as plt


#SCRAPING PIVOT POINTS FROM DAILY FX
page=requests.get('https://www.dailyfx.com/pivot-points')
#print(page.text)
tree = html.fromstring(page.content)
currency_pair=tree.xpath('//a[@class="dfx-pivotPointsComponent__link text-black font-weight-bold"]/text()')
pivot_point_names = tree.xpath('//span[@class="d-md-none d-flex flex-fill col-3 px-0 text-muted text-black font-weight-bold"]/text()')
pivot_point_values=tree.xpath('//span[@class="dfx-pivotPointsComponent__value col d-flex flex-column justify-content-end px-0 flex-fill text-black"]/text()')


#EDITING DATA INTO ACCESSIBLE FORMAT FOR FURTHER ANALYSIS
count=0
#DIVIDE DATA INTO CHUNKS OF 7 ELEMENTS (FOR EACH CURRENCY/STOCK)

grouped_pivot_point_names= [pivot_point_names[i:i + 7] for i in range(0, len(pivot_point_names), 7)]
grouped_pivot_point_values= [pivot_point_values[i:i + 7] for i in range(0, len(pivot_point_values), 7)]
#print(grouped_pivot_point_values[0])
grouped_pivot_points=[]
#print(pivot_point_names[0:7])

pivot_points=[]
K=list(zip(grouped_pivot_point_names,grouped_pivot_point_values))
Data=[]
for item in K:
  N=(list(zip(item[0],item[1])))
  Data.append(N)
Pairs_wt_pivot_data=list(zip(currency_pair,Data))
#print(Pairs_wt_pivot_data)

Pairs_wt_pivot_data_dict={}
for data in Pairs_wt_pivot_data:
  Pairs_wt_pivot_data_dict[data[0]]=data[1]
#print(Pairs_wt_pivot_data_dict['\nAUD/CAD\n'])


#REMOVING NEWLINE SPECIAL CHARACTERS

Pairs_wt_pivot_data_dict_full={}
for k,v in Pairs_wt_pivot_data_dict.items():
  CURR=k.replace("\n", "")
  N_dict={}
  for val in v:
    P_name=val[0].replace("\n", "")
    P_val=val[1].replace("\n", "")
    P_val_float=P_val
    N_dict[P_name]=P_val_float
  Pairs_wt_pivot_data_dict_full[CURR]=N_dict
#print(Pairs_wt_pivot_data_dict_full)

#CONVERTING DATA TO PANDAS DATAFRAME while removing NAN values/columns

pivot_points_df=pd.DataFrame(Pairs_wt_pivot_data_dict_full)
n_pivot_points_df=pivot_points_df.T
n_pivot_points_df.dropna()
#print(n_pivot_points_df['S3'].astype(float))

#CONVERT DF VALUES FROM STR TO FLOAT DATATYPE
#FILTER OUT UNNECESSARY STOCKS
currencies_pairs_name=[]
for ind in n_pivot_points_df.index:  
  if "/" in ind:    
    currencies_pairs_name.append(ind)  
  else:    
    continue
#print(currencies_pairs_name)

#for curr in currencies_pairs_name:

currency_pairs_data=n_pivot_points_df.T[currencies_pairs_name]
n_currency_pairs_data=currency_pairs_data.dropna()
n_currency_pairs_data=n_currency_pairs_data.T

#print(n_pivot_points_df[col].index)

for col in n_currency_pairs_data.columns:
  n_currency_pairs_data[col] = n_currency_pairs_data[col].astype(float)
print(n_currency_pairs_data.dtypes)
