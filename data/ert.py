import sys, csv , operator  
data = csv.reader(open('E:\\dataFinal_converted_final.csv'),delimiter=' ') 
csvfile2=open('E:\\dataFinal_convertedFinal.csv','w')
writer=csv.writer(csvfile2,delimiter=' ',lineterminator='\n')

dataList=[]
for row in data:
	dataList.append(row)
counter=0
for i in range(0,len(dataList)):
	#print(dataList[i][6])
	if int(dataList[i][6])==0:
		counter+=1
	else:
		if counter>0 and counter<25:
			for j in range(i-counter,i):
				writer.writerow(dataList[j])
		counter=0
		writer.writerow(dataList[i])