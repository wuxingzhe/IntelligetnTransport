import sys, csv , operator  
data = csv.reader(open('E:\\dataFinal_converted.csv'),delimiter=' ')
csvfile2=open('E:\\dataFinal_converted_final.csv','w')
writer=csv.writer(csvfile2,delimiter=' ',lineterminator='\n')

for row in data:
	if len(row)>12:
		row.pop()
	ss=str(row[2])
	num=(int(ss[0:2])-9)*60+int(ss[3:5])-23
	row.append(num)
	writer.writerow(row)
	