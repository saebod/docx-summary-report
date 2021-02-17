from datetime import datetime, timedelta,date
import pandas as pd

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
	return df
