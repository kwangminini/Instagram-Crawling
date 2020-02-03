import requests
from bs4 import BeautifulSoup
from pexpect import searcher_string
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib import rc
import re
import csv
import sys
import pandas as pd
keyword = "마라스팸"

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

instagram_tags = []
instagram_tag_dates = []
path = "/Users/kwangmin/Downloads/chromedriver"

options = wd.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = wd.Chrome(path, options=options)

driver.get(url)
time.sleep(3)

# 게시물 개수 정보를 가져온다
totalCount = driver.find_element_by_class_name('g47SY').text
totalCount = totalCount.replace(",","")

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
commentList=[]
for i in range(int(totalCount)):
    forCount=i
    time.sleep(1)
    try:
        data = driver.find_element_by_css_selector('.XQXOT') #게시물과 댓글
        tag_raw = data.text
        postList = tag_raw.split("\n")
        #print(postList)
        for i in postList:
            if re.match('[0-9]*w$', i):
                idx=postList.index(i)
                #print(postList.index(i))
                break
        #print(postList[idx+1:])

        for i in postList[idx+1:]:
            comment = re.compile("[ㅜ]*[ㅠ]*[?]*[!]*[ㄱ-ㅎ]*[0-9]*[가-힣]+[ㅜ]*[ㅠ]*[?]*[!]*[ㄱ-ㅎ]*").findall(i)
            if len(comment)>=1:  #댓글 있는것만 가져옴
                print(' '.join(comment))
                commentList.append(' '.join(comment))
        #comment = re.compile("[가-힣]+").findall(postList[idx+1:])
        #print("comment::::" + comment)
        #commentList.append(comment)


        #tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        #tag = ''.join(tags).replace("#", " ")

        #tag_data = tag.split()



    except:
        instagram_tags.append("error")
        instagram_tag_dates.append('error')
    try:
        #print("forCount::::"+str(forCount)+"totalCount::::::"+totalCount)
        if forCount==(int(totalCount)-1):
            driver.close()
            break
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow')))
        driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()

    except:
        driver.close()
    time.sleep(2)
dataframe = pd.DataFrame(commentList)
dataframe.to_csv("/Users/kwangmin/pycharmprojects/untitled/Test/comment.csv",header=False,index=True)
print(commentList)
driver.close()