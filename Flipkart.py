#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:51:38 2020

@author: hrishi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
#Search the product
product_search=input(str("Please enter the product you want to search for on flipkart:"))



def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

#To use it later in dataframe 
list_dataframe=[]



#Get the link
res=requests.get("https://www.flipkart.com/search?q="+product_search+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
#Create a beautifulsoup object
bs4=BeautifulSoup(res.text,"lxml")
#Getting the names of the products
name_list=bs4.find_all("div",{"class":"_3wU53n"})

original_price=bs4.find_all("div",{"class":"_3auQ3N"})
current_price=bs4.find_all("div",{"class":"_1vC4OE"})
    


#if list is zero try other class name and url else same
if len(name_list)==0:
    res=requests.get("https://www.flipkart.com/search?q="+product_search+"&sid=clo%2Cqfl%2Cszr%2C3xl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=underwear%7CMen%27s+Briefs+and+Trunks&requestId=04ac3bff-a2e3-492c-be56-232548a69781&as-backfill=on")
    name_list=bs4.find_all("a",{"class":"_2cLu-l"})
    for i,j,k in zip(name_list,original_price,current_price):
        flip_dict={"Name:":i.get_text(),"Original Price":strike(j.get_text()),"Current_price":k.get_text()}
        list_dataframe.append(flip_dict)
    #Creating the dataframe to display the final o/p to the user        
    df=pd.DataFrame(data=list_dataframe)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(df)    
else:    
    for i,j,k in zip(name_list,original_price,current_price):
        flip_dict={"Name:":i.get_text(),"Original Price":strike(j.get_text()),"Current_price":k.get_text()}
        list_dataframe.append(flip_dict)
    
    #Creating the dataframe to display the final o/p to the user        
    df=pd.DataFrame(data=list_dataframe)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(df)    
