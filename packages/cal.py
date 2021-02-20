from datetime import datetime, timedelta,date
import pandas as pd
import csv
import os
def avg_page_left(Goal_page,offdays_pr_week,char_now,deadline):
	#Calculate the number of charaters from the goal page
	Goal_char=Goal_page*2400
	#Calculate the number of charators left
	back_char = Goal_char-char_now
	#Calculate the number os pages left and round off with 2 dec
	back_page=round(back_char/2400,2)
	#Calculate the number of daye left until deadline
	today=date.today()
	daysuntill=(deadline- today).days
	#Calculate the total number of offdays 
	weeks =daysuntill/7
	offdays= weeks*offdays_pr_week
	#Calculate the total number of working days left
	Totalworkingdays =round(daysuntill-offdays,0)
	#Calculate the average number of pages that needs to be written given the working days
	avg_page=round(back_page/Totalworkingdays,2)
	return avg_page
deadline = date(2021, 5, 20)


def ETL(df):
	df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')
	df['day_of_week'] = df['Date'].dt.day_name()
	df['char_today']=df['Count'].subtract(df['Count'].shift()).fillna(0)
	df['pages_written']=round(df['char_today']/2400,2)
	df=df.sort_values('Date',ascending=False)
	return df



def check_csv(csvname):
	fields = ['Date', 'Count']
	if not os.path.exists(csvname):
		with open(csvname, 'a') as csvfile:
			writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=fields)
			writer.writeheader()
			csvfile.close()

def csv_insert_count(csvfilename,char):
	'''Inserts todays count in csv file, if the file is not created it will create the file
		Args: 
			csvfilename: the csv file name 
			char: todays number of charaters
	 '''
	today = date.today()
	#If there isn't any csv file with the name it will create it 
	check_csv(csvfilename)
	df = pd.read_csv(csvfilename, names=['Date', 'Count'], header=0, index_col='Date',sep=',')
	df.loc[str(today), 'Count'] =char
	df.to_csv(csvfilename)
