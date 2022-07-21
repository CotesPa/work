import click
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

url = 'https://referendum.2021.nat.gov.tw/pc/zh_TW/01/63000000000000000.html'
s = Service('C:/Users/shitb/OneDrive/Desktop/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(url)

def tool(URL):
    res = requests.get(URL)
    dfs = pd.read_html(URL)
    sheet = dfs[0]
    sheet.drop([0,5,6,7], inplace=True)
    sheet.drop([4,5,6],axis=1,inplace=True)
    sheet.columns = sheet.loc[1]
    sheet.drop([1],inplace=True)

    soup = BeautifulSoup(res.text, 'lxml')
    zone = soup.select_one('b').text
    sheet['投票地區'] = zone

    print(sheet)

for i in range(2,393):
    n = 'itemTextLink'+str(i)
    driver.find_element(By.ID, n).click()
    url1 = str(driver.current_url)
    # print(url1)
    tool(url1)
