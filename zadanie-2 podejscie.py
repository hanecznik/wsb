import os

with open(os.path.join(os.getcwd(), 'rozliczenie-1.csv')) as plik:
    data = plik.readlines()
for i in range(len(data)):
    # print(data[i])
    data[i] = data[i].split(',')
#     print(data[i])
# print(data[2][2])

total=0
for i in range(1, len(data)):
    total= total+int(data[i][1])
print(total)
average=total/(len(data)-1)
print(round(average, 2))

total=0
for i in range (1, len(data)):
    print(data[i])
    data[i][4] = data[i][4].replace('\n', '')
    if data [i][4] == 't' and data[i][3] == 'k':
        total += 1
print(total)