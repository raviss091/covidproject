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
import xlrd
import matplotlib.pyplot  as plt

#below is biggest and important function for extraction from web and storing in csv

# 1 extracting table using beautiful soup
def resource():
    url="https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv"
    r=requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')

    for mytable in soup.find_all('table'):
        for trs in mytable.find_all('tr'):
            ths=trs.find_all('th')
            tds = trs.find_all('td')
            row = [elem.text.strip().encode('utf-8') for elem in tds]
        
        
# 2  web scraping and then writing in  covid_global an csv file
        
    file="C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\covid_global.csv"
  
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['s.no','date','country','confirm','recover','death'])
        for mytable in soup.find_all('table'):
            for trs in mytable.find_all('tr'):
            
                tds = trs.find_all('td')
                row = [elem.text.strip() for elem in tds]
            
                writer.writerow(row)
    
     
            
''' function for first question'''          
def HIGH_RISK_TRAVEL_AREA(m):
    
# 3 attempting first question
    x=int(input("enter your choice\n1.latest data(from web sites)(may not work due to websites issues)\n2,saved data(recommended)"))
    if(x==1):
        c=1
        resource()
        df=pd.read_csv('C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\covid_global.csv',index_col=0,skiprows=1,names=['Date', 'Country','Confirmed', 'Recoverd', 'Deaths'])
        
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
    else:
        print("\n\nyou may encounter some garbage in this method sorry!!!")
        path="C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\offline.csv"
        df=pd.read_csv(path,error_bad_lines=False)
        print(df)
        df.date = pd.to_datetime(df.date, format="%Y-%m-%d")
        
        print(" top 20 countries in death rate")
        for column in df[['date']]:
        
            print(df.date)
    
            newdf=df.loc[df['death']/df['confirm']>0.04]    
            print(newdf.country.drop_duplicates().head(20))  #half of question 1 is done
           
            co=input("enter the name of the country")    #for grapghing purpose
            mdf=df.loc[df['country']==co]
            print(mdf)
             
            plt.plot(mdf['date'],mdf['death'])
            plt.xlabel('Time(date)')
            plt.ylabel('deaths')
            plt.show()
            print(co +" death rate graph")
        
    
   
''' function for second question'''  
   
#4 attempting second qustion
def HIGH_RISK_age_group(n):
    print("\npress 1 for global data and 2 for american cities after this query\n")
    x=int(input("stastics global or american for  risk of age group"))
    if(x==1):
        print("\n Table for  number of death in rannge of age 15-25 in differnet countries\n")
        
        fp="C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\cov_dat.csv" 
        mc=pd.read_csv("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\cov_dat.csv")
        print(mc)
    elif(x!=1):
        loc="C:\\Users\\Ravi shankar sharma\Downloads\\americanstates (1).xlsx"
        wb=xlrd.open_workbook(loc)
        sheet=wb.sheet_by_index(0)
        print("These are the states where you must be likeing to to study")
        print(sheet.col_values(0))
        r=sheet.nrows
        c=sheet.ncols
        n=int(input("Enter the number which has been asigned to the state where you want to study. "))
        print("These are the details of deaths of the selected state")
        for i in range (1,c):
            print("Deaths in" ,sheet.cell_value(0,i),"years age gaps are",sheet.cell_value(n,i))
        print("This is the graph of age vs death of the selected state")
        x=[sheet.cell_value(0,i) for i in range (1,c)]
        y=[sheet.cell_value(n,i) for i in range (1,c)]
        fig = plt.figure(figsize = (10, 5)) 
        plt.plot(x,y)
        plt.xlabel('age gaps')
        plt.ylabel('deaths')
        plt.title(' state age vs death graph')
        plt.show()
        print (" list of top 10 states acording for the deaths in USA")
        for i in range (1,16):
            print(sheet.cell_value(i,0))
        

''' function for third question'''  
# attempting third question
     
def avg():
    
    print("\nAvg timetaken for death and recovery by country\n")
    
    to=pd.read_csv("C:\\Users\\Ravi shankar sharma\\OneDrive\\Desktop\\covid 19\\avg_time.csv")
    to['sno'] = to.sno.astype(float)
    print("country data accesible 1.india 2.us 3.italy 4.france 5.germany 6. britain 7. cannada 8. china 9 .sweden 10. japan")
    to['country'] = to['country'].astype(str)
    for column in to[['sno']]:
        cot=input("enter country name for data :")
        mof=to.loc[to['country']==cot]
        print(mof)
    print("total data compiled")
    print(to)
    
    
    
#  main program for covid19

print(" our program is highly reliable as for first part we have used data of 20,0000 line")
x=int(input("enter your choice \n1.HIGH RISK TRAVEL AREA\n2.HIGH RISK age group\n3.avg timetaken for death and recovery by country:"))
if(x==1):
    
    print("test 1")
    HIGH_RISK_TRAVEL_AREA(x)
if(x==2):
    
    HIGH_RISK_age_group(x)
        
if(x==3):
    avg()


















    


        
        


      
