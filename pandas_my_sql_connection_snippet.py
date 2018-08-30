"""
Snippet to connect any mysql database and port it to dataframe
"""

import sys
import os
import pandas as pd
import re
import numpy as np
from IPython.display import display, HTML
from datetime import datetime
from pytz import timezone
import glob
import MySQLdb
conn = MySQLdb.connect(host="hostname", user="username", passwd="password", db="databasename")
cursor = conn.cursor()
cursor.execute("enter your Query")
rows = cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows], columns =["Name of Columns"])



