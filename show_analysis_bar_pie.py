import csv
import numpy as np
import pandas as pd
from collections import Counter
from  matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")


data=pd.read_csv('tvshow.csv')
print(data )
sno=list(data['sno.'])
showname=list(data['show name'])
rating=list(data['rating'])
votes=list(data['votes'])


print(sno,showname,rating,votes,sep='\n')

plt.barh(showname[0:30],rating[0:30],label='show popularity',)
plt.legend(loc='best',)
plt.ylabel('showname')
plt.xlabel('rating')
plt.axis(xmax=10)
plt.subplots_adjust(left=0.27,right=0.96,bottom=0.08,top=1)

plt.show()
plt.pie(rating[0:20],labels=showname[0:20],autopct='%1.1f%%',rotatelabels=False)
plt.subplots_adjust(left=0.03,right=0.96,bottom=0,top=1)

plt.show()

