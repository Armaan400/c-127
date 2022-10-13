from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser=webdriver.Chrome("C:/Users/MY PC/Desktop/C-126/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

planet_data = []
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","eccentricity"] 

def scrap_more_data(hyperlink):
    try:
     page = requests.get(hyperlink)
      
     soup = BeautifulSoup(page.content, "html.parser")
     for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            hyperlink_li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,hyperlink_li_tags in enumerate(hyperlink_li_tags):
                if (index==0):
                    temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tags.find_all("a",href=True)[0])
                else:
                    try:
                        temp_list.append(hyperlink_li_tags.contents[0])
                    except:
                        temp_list.append("")
        
            planet_data.append(temp_list)

    except:
        time.sleep(1)
        scrap_more_data(hyperlink)
for data in planet_data:
    scrap_more_data(data[5])

def scrap():

    for i in range(1,5):
        while True:
            time.sleep(2)
            soup=BeautifulSoup(browser.page_source,"html.parser")
            current_pg_no=int(soup.find_all("input",attrs={"class","pg_no"})[0].get("value"))
            if current_pg_no <i:
                browser.find_element(By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a')
            
            elif current_pg_no>i:
                browser.find_element(By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()

            else:
                break


    


        
    
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("scrapper_2.csv", "w") as f: csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)


