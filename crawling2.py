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
import re
import csv

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

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

for i in range(int(totalCount)):
    time.sleep(1)
    try:
        data = driver.find_element_by_css_selector('.C7I1f.X7jCj')
        tag_raw = data.text
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tags).replace("#", " ")

        tag_data = tag.split()

        for tag_one in tag_data:
            instagram_tags.append(tag_one)
        #print(instagram_tags)

        date = driver.find_element_by_css_selector("time.FH9sR.Nzb55").text  # 날짜 선택
        date = date[:-1]
        #print(date)
        if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1:
            instagram_tag_dates.append('0주')
        else:
            instagram_tag_dates.append(date)

    except:
        instagram_tags.append("error")
        instagram_tag_dates.append('error')
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow')))
        driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()

    except:
        driver.close()
    time.sleep(2)
instagram_date_dic={}
for i in range(len(instagram_tag_dates)):
    if int(instagram_tag_dates[i]) in instagram_date_dic:
        instagram_date_dic[int(instagram_tag_dates[i])]+=1
    else:
        instagram_date_dic[int(instagram_tag_dates[i])]=1
print(instagram_tag_dates)
#instagram_date_dic_sort={}
instagram_date_dic_sort = sorted(instagram_date_dic.items())
xlabel=[]
y=[]
print(instagram_date_dic_sort)
for i in instagram_date_dic_sort:
    xlabel.append(str(i[0])+"주")
    y.append(i[1])
#for key, value in instagram_date_dic_sort.items():
#    x.append(str(key)+"주")
#    y.append(value)

x=np.arange(len(y))

plt.title("마라스팸 주 별 게시물 개수")
plt.bar(x,y)
plt.xticks(x, xlabel)
plt.yticks(y)
plt.xlabel("주")
plt.ylabel("게시물 수")
plt.show()
driver.close()