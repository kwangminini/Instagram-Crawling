import requests
from bs4 import BeautifulSoup

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib import rc,font_manager
import re
import csv
import sys
import pandas as pd
#keyword = "뚜레쥬르브라우니"

#url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

instagram_tags = []
instagram_tag_dates = []
commentList = []
path = "/Users/User/chromedriver"
font_path = "C:/Users/User/Desktop/ONLYONEFAIR/CJ_ONLYONE_NEW_FONT/TTF/CJ ONLYONE NEW body Light.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
options = wd.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = wd.Chrome(path, options=options)

#driver.get(url)
#time.sleep(3)
def createTestList(keyword):
    url = "https://www.instagram.com/explore/tags/{}/".format(keyword)
    #path = "/Users/User/chromedriver"
    #options = wd.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('disable-gpu')
    #driver = wd.Chrome(path, options=options)
    driver.get(url)
    time.sleep(3)
    # 게시물 개수 정보를 가져온다
    totalCount = 50
    driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

    for i in range(totalCount):
        forCount = i
        time.sleep(1)
        try:
            data = driver.find_element_by_css_selector('.XQXOT')  # 게시물과 댓글
            tag_raw = data.text
            postList = tag_raw.split("\n")
            # print(postList)
            for i in postList:
                if re.match('[0-9]*w$|[0-9]*d$|[0-9]*h$|[0-9]*m$', i):
                    idx = postList.index(i)
                    # print(postList.index(i))
                    break
            # print(postList[idx+1:])

            for i in postList[idx + 1:]:
                comment = re.compile("[ㅜ]*[ㅠ]*[?]*[!]*[ㄱ-ㅎ]*[0-9]*[가-힣]+[ㅜ]*[ㅠ]*[?]*[!]*[ㄱ-ㅎ]*").findall(i)
                if len(comment) >= 1:  # 댓글 있는것만 가져옴
                    print(' '.join(comment))
                    commentList.append(' '.join(comment))
            # comment = re.compile("[가-힣]+").findall(postList[idx+1:])
            # print("comment::::" + comment)
            # commentList.append(comment)

            # tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
            # tag = ''.join(tags).replace("#", " ")

            # tag_data = tag.split()



        except:
            instagram_tags.append("error")
            instagram_tag_dates.append('error')
        try:
            # print("forCount::::"+str(forCount)+"totalCount::::::"+totalCount)
            if forCount == (totalCount - 1):
                driver.close()
                break
            WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow')))
            driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()

        except:
            driver.close()
        time.sleep(2)
def createBadTestList(keyword):
    url = "https://www.instagram.com/explore/tags/{}/".format(keyword)
    #path = "/Users/User/chromedriver"
    #options = wd.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('disable-gpu')
    #driver = wd.Chrome(path, options=options)
    driver.get(url)
    time.sleep(3)
    # 게시물 개수 정보를 가져온다
    totalCount = 50
    driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

    for i in range(totalCount):
        forCount = i
        time.sleep(1)
        try:
            data = driver.find_element_by_css_selector('.C7I1f.X7jCj')  # 게시물내용
            tag_raw = data.text
            postList = tag_raw.split("\n")
            print(postList)

            for i in postList:
                comment = re.compile("[ㅜ]*[ㅠ]*[?]*[!]*[ㄱ-ㅎ]*[0-9]*[가-힣]+[ㅜ]*[ㅠ]*[?]*[!]*[ㄱ-ㅎ]*").findall(i)
                if len(comment) >= 1:  # 댓글 있는것만 가져옴
                    print(' '.join(comment))
                    commentList.append(' '.join(comment))


        except:
            instagram_tags.append("error")
            instagram_tag_dates.append('error')
        try:
            # print("forCount::::"+str(forCount)+"totalCount::::::"+totalCount)
            if forCount == (totalCount - 1):
                driver.close()
                break
            WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow')))
            driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()
        except:
            driver.close()
        time.sleep(2)
createTestList("뚜레쥬르브라우니")
time.sleep(2)
print("----------------뚜레쥬르브라우니 완료-------------------")
driver = wd.Chrome(path, options=options)
createTestList("노맛")
time.sleep(2)
print("----------------노맛 완료-------------------")
driver = wd.Chrome(path, options=options)
createTestList("고메함박스테이크")
time.sleep(2)
print("----------------고메함박스테이크 완료-------------------")
driver = wd.Chrome(path, options=options)
createBadTestList("진짜맛없다")
time.sleep(2)
print("----------------진짜맛없다 완료-------------------")
driver = wd.Chrome(path, options=options)
createTestList("진짜맛없다")
time.sleep(2)
print("----------------진짜맛없다 댓글 완료-------------------")
dataframe = pd.DataFrame(commentList)
dataframe.to_csv("C:/cj/testData2.csv",header=False,index=True,encoding='utf-8-sig')
print(len(commentList))
driver.close()