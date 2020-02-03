#문자열 제거 테스트
import re
a=['asdf', '35w', 'asdsf','2w342','오늘도화이팅ㅋㅋ']
for i in a:
    if re.match('[ㄱ-ㅎ]*[가-힣]+', i) :
        z=a.index(i)

print(a[z:])
