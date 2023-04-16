import matplotlib.pyplot as plt

f = open('point.csv')
lines = f.readlines()
f.close()
x = []
y = []
for line in lines:
    list2 = line.strip('\n').split(',')
    x.append(float(list2[0]))
    y.append(float(list2[1]))


###  shrinking
f = open('result/shrinking.csv')
lines = f.readlines()
f.close()
list1 = []
for i in range(1,len(lines)):
    list2 = lines[i].strip('\n').split(',')
    list1.append(int(list2[1]))

x1 = []
y1 = []
for i in range(1,len(list1)):
    x1.append(x[list1[i]])
    y1.append(y[list1[i]])


###  growing
f = open('result/growing.csv')
lines = f.readlines()
f.close()
list3 = []
for i in range(1,len(lines)):
    list2 = lines[i].strip('\n').split(',')
    list3.append(int(list2[1]))

x2 = []
y2 = []
for i in range(1,len(list3)):
    x2.append(x[list3[i]])
    y2.append(y[list3[i]])

###  50low
f = open('result/50low.csv')
lines = f.readlines()
f.close()
list4 = []
for i in range(1,len(lines)):
    list2 = lines[i].strip('\n').split(',')
    list4.append(int(list2[1]))

x3 = []
y3 = []
for i in range(1,len(list4)):
    x3.append(x[list4[i]])
    y3.append(y[list4[i]])


###  other
x4 = []
y4 = []
for i in range(0,183):
    if((i not in list1) and (i not in list3) and (i not in list4)):
        x4.append(x[i])
        y4.append(y[i])


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=1200,xmin=0)
plt.ylim(ymax=1200,ymin=0)


plt.scatter(x1, y1, s=40,c='black',marker='s', alpha=1, label='shrinking')
plt.scatter(x3, y3, s=20,c='black',marker='x', alpha=1, label='lowCluster')
plt.scatter(x2, y2, s=40,c='black',marker='^', alpha=1, label='growing')
plt.scatter(x4, y4, s=1,c='black',marker='o', alpha=1, label='normal')

plt.legend()
plt.show()