
# docx-summary-report
![](https://github.com/saebod/docx-summary-report/raw/master/tmp/report_readme.png)
I have created docx-summary-report with the purpose of giving me a overview of my progress writing my master thesis. 
The repo is used for collecting the number of characters i have written each day to measure my progress.

## Usage

### count_CSV.py
the file count_CSV.py is used for colecting data from my docx file.  Using a function i have created called **Character_Count** i can calculate the number of characters in my word file. The function needs two arguments:

| Argument|Description  |
|--|--|
|filepath|the path of where your docx file is saved|
 |stopword| if only want to gather the number of charaectors untill a ceratin place you can include a stopword for it to know when to stop.| 


The stop word is removing elements i don't need to measure. Such as referencelist and Appendix.
When the data is colleted the script  saves it in a CSV file with the input of date and number of characters

###Example 

```python
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
)
```
## Generate_report. py
Generate_report is used to create a pdf file with data visualization that gives a overview of the progress.
The file needs three inputs:

| Argument|Description  |
|--|--|
|deadline|The deadline of your report|
 |Goal_page|The goal of how many pages you want to write in total| 
 |offdays_pr_week|how many offdays do you except to have pr week

###End
