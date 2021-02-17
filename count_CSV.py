from packages.cal import check_csv
from packages.WordCharacter import Character_Count
import pandas as pd
import datetime
import os
import csv
char =Character_Count('C:/Users/ext-sda/Dropbox/Uni-handelskole/Business Intelligence - Uni/Speciale/Speciale.docx','Stop-python')
csvfilename= 'count_logv2.csv'

#If there isn't any csv file with the name it will create it 
check_csv(csvfilename)
df = pd.read_csv(csvfilename, names=['Date', 'Count'], header=0, index_col='Date',sep=',')
df.loc[str(datetime.date.today()), 'Count'] =char
df.to_csv(csvfilename)
