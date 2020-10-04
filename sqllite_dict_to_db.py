import sqlite3
import sys
import re 
import numpy as np 
import pandas as pd
from pandas import DataFrame
from datetime import datetime
import os,glob,subprocess,sys

l=[]
f = open("ouput.log", "r")
l=f.readlines()
f.close()

my_keys={}
my_keys["key1"]="NA"
my_keys["key2"]="NA"
my_keys["key3"]="NA"
my_keys["key4"]="NA"
my_keys["current_date_run"]=datetime.today().strftime('%Y%m%d')
for l1 in l:
    if "condition1:" in l1:
		my_keys["key1"]=<value1>
    if "condition2:" in l1:
		my_keys["key1"]=<value2>
    if "condition3:" in l1:
		my_keys["key1"]=<value3>
    if "condition4:" in l1:
		my_keys["key1"]=<value4>
t=[]
for k,v in my_keys.items():
    t.append(v)

connection = sqlite3.connect('logs.db')
cursor=connection.cursor()

cmd1 = """ 
CREATE TABLE IF NOT EXISTS 
test_history_test(key1 TEXT PRIMARY KEY, key2 TEXT,key3 TEXT, key4 TEXT , current_date_run TEXT)
"""
cursor.execute(cmd1)
if len(my_keys) == 23:
    cursor.execute("INSERT OR REPLACE INTO test_history_test(key1 , key2, key3 , key4 ,current_date_run) VALUES(?, ?, ?, ? ,?);",t)
else:
    pass
cursor.execute("SELECT * FROM test_history_test")
results=cursor.fetchall()

for r in results:
    print(r)
connection.commit()
connection.close()

