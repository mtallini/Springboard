#tokenize_csv.py

import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize

directory = "/home/michael/Desktop/capstone_project_1/data"
sample = pd.read_csv(directory + "/sample.csv")
