#text2csv.py
"""
Taking the raw text file data and creating a csv file to represent the data in 
a tabular form
""" 
import os
import pandas as pd
from collections import defaultdict

directory = "/home/michael/Desktop/capstone_project_1/data"
data_dict = defaultdict(list)
with open(directory+"/sample.txt", encoding='Latin-1') as f:
    fieldnames = ['product/productId', 'review/userId', 'review/profileName',
                  'review/helpfulness', 'review/score', 'review/time', 
                  'review/summary', 'review/text']
    for line in f.readlines():
        if not line.strip():
            pass
        else:
            key, value = line.split(': ', 1)
            data_dict[key].append(value)
    df = pd.DataFrame.from_dict({fieldnames[0]: data_dict[fieldnames[0]], 
                          fieldnames[1]: data_dict[fieldnames[1]], 
                          fieldnames[2]: data_dict[fieldnames[2]],
                          fieldnames[3]: data_dict[fieldnames[3]],
                          fieldnames[4]: data_dict[fieldnames[4]],
                          fieldnames[5]: data_dict[fieldnames[5]],
                          fieldnames[6]: data_dict[fieldnames[6]],
                          fieldnames[7]: data_dict[fieldnames[7]]})
    df.to_csv(directory+'/sample.csv')