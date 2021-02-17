from packages.cal import avg_page_left, ETL
from packages.WordCharacter import Character_Count
import pandas as pd
import datetime

char =Character_Count('C:/Users/ext-sda/Dropbox/Uni-handelskole/Business Intelligence - Uni/Speciale/Speciale.docx','Stop-python')

today=str(datetime.date.today())

fields = ['Date', 'Count']
df = pd.read_csv('count_logv2.csv', names=fields, header=0, index_col='Date',sep=',')
df.loc[today, 'Count'] =char
df.to_csv("count_logv2.csv")
