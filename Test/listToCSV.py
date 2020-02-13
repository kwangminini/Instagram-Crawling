import csv
data = [[1,2,3,4],[5,6,7,8]]
csvfile=open("저장할 csv 파일 경로","w",newline="")
csvwriter=csv.writer(csvfile)
for row in data:
    csvwriter.writerow(row)
csvfile.close();