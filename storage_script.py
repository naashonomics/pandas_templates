import os,subprocess,re,sqlite3
import pandas as pd 

t1=subprocess.check_output("df -h".split()).split("\n")
t2=filter(Non,t1)
t3=[]
for t in t2:
	temp=(re.sub('\s+',',',t))
	t4=[]
	t4=temp.split(",")
	t3.append(t4)
	
t3.pop()
df=pd.DataFrame(t3,columns=["Filesystem","size","used","avail","use%","mounted_on"])

data_db=[]
for t in t3:
	dict={}
	dict['Filesystem']="NA"
	dict['size']="NA"
	dict['used']="NA"
	dict['avail']="NA"
	dict['use%']="NA"
	dict['mounted_on']="NA"
	dict['Filesystem']=t[0]
	dict['size']=t[1]
	dict['used']=t[2]
	dict['avail']=t[3]
	dict['use%']=t[4]
	dict['mounted_on']=t[5]
	data_db.append(dict)
	
for temp in data_db:
	print("\n")
	for k,v in temp.items():
		print(str(k) + " "  + str(v))