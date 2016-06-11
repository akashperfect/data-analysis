import csv
# resultFile = open("output.csv",'wb')
resultFile = open("test.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerow(['id', 'hotel_cluster'])
i = 0
for i in range (0, ):
    if(len(prediction[i]) != 0):
        strh = ' '.join(str(x) for x in prediction[i])
        wr.writerow([str(target[i][0]), strh])
        i += 1
print i