from realtimeforex import *
import json


#finaldata=final_data()
time_stamp=timerer()

Final_data={}                                              
Final_data[time_stamp]=finaldata
#print(Final_data)

#Final_data_dictionary[time_stamp]

filename = 'realtimeforex.json'
# Old JSON File:
# [{"alice": 24, "bob": 27}]
entry = final_data()

import os

if os.stat('forex.json').st_size == 0:
    with open(filename, "w") as file:
        json.dump(Final_data, file)
else:
    with open(filename, "r+") as file:
        data = json.load(file)
        data[time_stamp]=entry
        file.seek(0)
        json.dump(data, file)
