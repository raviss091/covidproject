# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:10:32 2020

@author: Ravi shankar sharma
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import datetime
import matplotlib.pyplot  as plt

#below is biggest and important function for extraction from web and storing in csv

# 1 extracting table using beautiful soup
def resource():
    url="https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv"
    r=requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')

    for mytable in soup.find_all('table','js-csv-data csv-data js-file-line-container'):
        for trs in mytable.find_all('tr'):
            ths=trs.find_all('th')
            tds = trs.find_all('td')
            row = [elem.text.strip().encode('utf-8') for elem in tds]
        
        
# 2  web scraping and then writing in  covid_global an csv file
        
        file="C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\covid_global.csv"
  
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['s.no','date','country','confirm','recover','death'])
        for mytable in soup.find_all('table','js-csv-data csv-data js-file-line-container'):
            for trs in mytable.find_all('tr'):
            
                tds = trs.find_all('td')
                row = [elem.text.strip() for elem in tds]
            
                writer.writerow(row)
    
   # with open('mycsvfile.csv', 'a') as f:
    #    wri = csv.writer(f)
     
            
                
def HIGH_RISK_TRAVEL_AREA(m):
    
# 3 attempting first question
  
    resource()
    df=pd.read_csv("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\covid_global.csv")
    print(df)

# for parsing  the whole data i think

    df.date = pd.to_datetime(df.date, format="%Y-%m-%d")
    

    for column in df[['date']]:
    # if(df.loc[df['death']==0]='True')=='True':  wrong item but still useful
        print(df.date)

        newdf=df.loc[df['death']/df['confirm']>0.04]    
        print(newdf.country.drop_duplicates().head(50))  #half of question 1 is done
       
        co=input("enter the name of the country")    #for grapghing purpose
        mdf=df.loc[df['country']==co]
        print(mdf)
   
    plt.plot(mdf['date'],mdf['death'])
    return 1
    
   
   
   
#4 attempting second qustion
def HIGH_RISK_age_group(n):
    
    print("\n Table for  number of death in rannge of age 15-25 in differnet countries\n")
    
    fp="C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\cov_dat.csv" 
    mc=pd.read_csv("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\cov_dat.csv")
    print(mc)

# attempting third question
     
def avg():
    
    print("\nAvg timetaken for death and recovery by country\n")
    
    to=pd.read_csv("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\avg_time.csv")
    to['sno'] = to.sno.astype(float)
    to['country'] = to['country'].astype(str)
    for column in to[['sno']]:
        cot=input("enter country name for data ")
        mof=to.loc[to['country']==cot]
        print(mof)
#  main program for covid19

x=int(input("enter your choice \n1.HIGH RISK TRAVEL AREA\n2.HIGH RISK age group\n3.avg timetaken for death and recovery by country:"))
if(x==1):
    
    print("test 1")
    HIGH_RISK_TRAVEL_AREA(x)
if(x==2):
    
    HIGH_RISK_age_group(x)
        
if(x==3):
    avg()


















    


        
        


      
