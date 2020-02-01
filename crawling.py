from selenium import webdriver
from PIL import Image
from collections import Counter
import time
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import numpy as np
import matplotlib
# 검색할 태그명
tag = '마라스팸'

# 인스타그램 태그 페이지 URL 
url = 'https://www.instagram.com/explore/tags/' + tag

instagram_tags = []

path = "/Users/kwangmin/Downloads/chromedriver"
options = webdriver.ChromeOptions() 
options.add_argument('headless') 
options.add_argument('disable-gpu') 
driver = webdriver.Chrome(path, options=options)


# 암시적으로 최대 5초간 기다린다
driver.implicitly_wait(5)

# url에 접근한다
driver.get(url)

# 게시물 개수 정보를 가져온다
totalCount = driver.find_element_by_class_name('g47SY').text

# 게시물 클릭했을 때의 정보를 가져온다.
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

for i in range(int(totalCount)):
 #   time.sleep(1)
    data = driver.find_element_by_css_selector('.C7I1f.X7jCj')
   #print(data.text)
    tag_raw = data.text
    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
    tag = ''.join(tags).replace("#"," ") # "#" 제거

    tag_data = tag.split()
    for tag_one in tag_data:
        instagram_tags.append(tag_one)
    #print(instagram_tags)
    #instagram_tags=[]
    if i!=int(totalCount)-1:
        driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()

   # time.sleep(2)

driver.close()


instagram_tags = [word for word in instagram_tags]
print(instagram_tags)
#count=Counter(instagram_tags)
#common_tag_200=count.most_common(200)

spwords=set(STOPWORDS)
spwords.add('마라스팸')
spwords.add('SPAM')
spwords.add('스팸')
spwords.add('마라')
spwords.add('스팸마라')
spwords.add('마라스팸체험단')
spwords.add('스팸신제품')

#wc = WordCloud(font_path='C:/Users/User/Desktop/ONLYONEFAIR/CJ_ONLYONE_NEW_FONT/TTF/CJ ONLYONE NEW body Light.ttf',background_color="white", width=800, height=600)
#cloud = wc.generate_from_frequencies(dict(common_tag_200))
wordcloud = WordCloud(max_font_size=200, font_path='/Users/kwangmin/Downloads/D2Coding-Ver1.3.2-20180524/D2Coding/D2Coding-Ver1.3.2-20180524.ttf',
                     stopwords=spwords,
                     background_color='#FFFFFF',
                     width=1200,height=800).generate(' '.join(instagram_tags))

plt.figure(figsize = (20, 16))
plt.axis('off')
#plt.imshow(cloud)
plt.imshow(wordcloud)
plt.show()






# 게시물 개수를 출력한다
##print("totalCount :", totalCount) 

# 열어둔 webdriver를 종료한다
# (종료하지 않고 반복 실행하면 메모리 누수의 원인이 된다)
##driver.quit()
