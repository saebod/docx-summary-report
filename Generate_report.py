# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta,date
import os
from packages.cal import avg_page_left, ETL,check_csv, csv_insert_count
from packages.Graph import *
from packages.WordCharacter import Character_Count
######################Needs to be fill out################################
#Deadline for when you want to be done (YYYY,M,DD)
deadline = date(2021, 5, 20)
 #how many pages du you want to write
Goal_page=50
 #how many days pr week du you except not to be working on this paper
offdays_pr_week=2
#where your word file is and if you have a stopword
char =Character_Count('C:/Users/ext-sda/Dropbox/Uni-handelskole/Business Intelligence - Uni/Speciale/Speciale.docx','Stop-python')
#Name of the log csv file in which the log of your charaters is saved.
# Don't worry if you don't have created such a file. the script will create the file if it cannot find it.
csvfilename= 'count_logv2.csv'
##########################################################################

csv_insert_count(csvfilename=csvfilename,char=char)
today = date.today()
df =pd.read_csv(csvfilename,sep=",")
df=ETL(df)
df=df.sort_values('Date',ascending=False)
#total count
Total_count = df.iloc[0]['Count']
Total_page = Total_count/2400
#Count from privous day
Total_count_P = df.iloc[1]['Count']
Total_page_P = Total_count_P/2400
avg_page=avg_page_left(Goal_page=Goal_page, offdays_pr_week=offdays_pr_week, char_now=Total_count, deadline=deadline)


## pdf creates ####
WIDTH = 210
HEIGHT = 297
def create_title(day, pdf):
  pdf.set_font('Arial', '', 24)  
  pdf.ln(10)
  pdf.write(5, f"Speciale skrivning")
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'{day}')
  pdf.ln(5)

def create_report(day=datetime.today(), filename="report.pdf"):
  pdf = FPDF() 
  #First page
  pdf.add_page()
  create_title(day, pdf)
  # create and prints gauge for number of pages
  plot_page_gauge(Total_page,Total_page_P,Goal_page)
  pdf.image("./tmp/page_gauge.png", 5, 40, WIDTH/3-10)
  # create and prints gauge for number of charaters
  plot_page_card(avg_page)
  pdf.image("./tmp/fig_card.png", WIDTH/3, 45, WIDTH/3-10)
  # create and prints lineplot for number of written charaters every day
  plot_count_gauge(Total_count,Total_count_P,Goal_page)
  pdf.image("./tmp/count_gauge.png", WIDTH/2+30, 40, WIDTH/3-10)
  
  # create and prints lineplot for number of written charaters every day
  plot_daily(df)
  pdf.image("./tmp/TS_daliy.png", 5, 90, WIDTH/2-10)
  # create and prints lineplot for number of written charaters every day
  plot_count(df)
  pdf.image("./tmp/TS_count.png", WIDTH/2, 90, WIDTH/2-10)

  #creates and print barplot for number of written charaters grouped by weekday
  plot_weekday(df)
  pdf.image("./tmp/weekday_bar.png", 5, 170, WIDTH/2-10)

  pdf.output(filename, 'F')
if __name__ == '__main__':
  create_report(today)