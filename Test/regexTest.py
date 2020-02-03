import re
text="ㅋㅋㅋ대박대박 짱 맛있다 ㅎㅎ 맛있겠네용"
test = re.compile("[가-힣]+").findall(text)
print(test)