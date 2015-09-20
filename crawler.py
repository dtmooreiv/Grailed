__author__ = 'phillipblack'
from bs4 import BeautifulSoup
import requests

import pandas as pd
from pandas import Series,DataFrame

url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2013-14-legislative-session.html'

#Request content from webpage
result = requests.get(url)
c = result.content

#Set as Beautiful Soup Object
soup = BeautifulSoup(c)

#Go to the section of interest
summary = soup.find("div",{'class':'list-land','id':'content'})

# Find the tables in the HTML
tables = summary.find_all('table')

#set up empty data list
data = []

#set rows as first indexed object in tables with a raw
rows = tables[0].findAll('tr')

#grab every HTML cell in every row
for tr in rows:
    cols = tr.findAll('td')
    #check to see if text is in the row
    for td in cols:
        text = td.find(text =True)
        print text
        data.append(text)
data

#set up empty lists
reports = []
date = []

#se tindex counter
index = 0

#go find the pdf cells
for item in data:
    if 'pdf' in item:
        #add the date and reports
        data.append(data[index-1])

    #get rid of \xa0
    reports.append(item.replace(u'\ax0',u' '))

index += 1

date = Series(date)
reports = Series(reports)

# Concatenate into a DataFrame
legislative_df = pd.concat([date,reports],axis=1)

# Set up the columns
legislative_df.columns = ['Date','Reports']

#show the data.frame
legislative_df


