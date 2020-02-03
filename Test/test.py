#문자열 제거 테스트
import re
a=['asdf', '35w', 'asdsf','2w342']
for i in a:
    if re.match('[0-9]*w$', i) :
        z=a.index(i)

print(a[z:])
