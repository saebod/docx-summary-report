import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import importlib
import matplotlib as mpl

def plot_daily(df):
	plt.figure()
	sns.set()
	sns.lineplot(x=df['Date'],y=df['char_today']).set_title('Antal tegn skrevet pr. dag')
	plt.xlabel('Dato')
	plt.ylabel('Antal tegn')
	plt.xticks(rotation=-45)
	plt.tight_layout()
	plt.savefig('./tmp/TS_daliy.png',dpi=400)
	importlib.reload(mpl); importlib.reload(plt); importlib.reload(sns)
	return

def plot_count(df):
	plt.figure()
	sns.set()
	sns.lineplot(x=df['Date'],y=df['Count']).set_title('Akkumuleret antal tegn')
	plt.xlabel('Dato')
	plt.ylabel('Akk. tegn')
	plt.xticks(rotation=-45)
	plt.tight_layout()
	plt.savefig('./tmp/TS_count.png',dpi=400)
	importlib.reload(mpl); importlib.reload(plt); importlib.reload(sns)
	return

def plot_weekday(df):
	df=df.sort_values('char_today',ascending=False)
	plt.figure()
	weekday_bar=sns.barplot(x='day_of_week',y="char_today",data=df)
	plt.xlabel('Dag i ugen')
	plt.ylabel('Antal tegn')
	plt.tight_layout()
	weekday_bar.figure.savefig('./tmp/weekday_bar.png',dpi=400)
	importlib.reload(mpl); importlib.reload(plt); importlib.reload(sns)

def plot_count_gauge(Total_count,Total_count_P,Goal_page):
	fig_char = go.Figure(go.Indicator(
	    domain = {'x': [0, 1], 'y': [0, 1]},
	    value = Total_count,
	    mode = "gauge+number+delta",
	    title = {'text':"<span style='font-size:2em'>Antal tegn </span>"},
	    delta = {'reference': Total_count_P},
	    gauge = {'axis': {'range': [None, 132000]},
	    'bar': {'color': "green"},
	             'steps' : [
	                 {'range': [0, 48000], 'color': "lightgray"},
	                 {'range': [48000, 96000], 'color': "gray"}],
	             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': Goal_page*2400}}))
	fig_char.write_image("./tmp/count_gauge.png")

def plot_page_gauge(Total_page,Total_page_P,Goal_page):
	fig_page = go.Figure(go.Indicator(
	    domain = {'x': [0, 1], 'y': [0, 1]},
	    value = Total_page,
	    mode = "gauge+number+delta",
	    title = {'text':"<span style='font-size:2em'>Antal sider </span>"},
	    delta = {'reference': Total_page_P},
	    gauge = {'axis': {'range': [None, 55]},
	             'steps' : [
	                 {'range': [0, 20], 'color': "lightgray"},
	                 {'range': [20, 40], 'color': "gray"}],
	             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': Goal_page}}))
	fig_page.write_image("./tmp/page_gauge.png")

def plot_page_card(avg_page):
	fig_card = go.Figure(go.Indicator(
	    domain = {'x': [0, 1], 'y': [0, 1]},
	    mode = "number",
	    value = avg_page,
	    title = {"text": "<span style='font-size:2em'>Antal sider du skal skrive</span> <br><br><span style='font-size:1.5em;color:gray'>pr arbejdsdag</span><br><span style='font-size:1.5em;color:gray'>Før deadline d. 20 maj</span>"},
	    ))
	fig_card.write_image("./tmp/fig_card.png")

#plot_page_card(400)
#plot_count(df)
#plot_daily(df)
#plot_weekday(df)
#plot_count_gauge(df)
#plot_page_gauge(df)
