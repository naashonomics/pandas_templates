import pandas as pd
from flask import Flask 
app=Flask(__name__)
@app.route("/")
def pandas_to_csv():
	#df=pd.read_excel("C:\\datatest\\Mall_Customers.csv")
	df=pd.read_csv("C:\\datatest\\Mall_Customers.csv")
	return df.to_html()

if __name__=='__main__':
	app.run()