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


###growing
f = open('result/growing.csv')
lines = f.readlines()
f.close()
list1 = []
for i in range(1,len(lines)):
    list2 = lines[i].strip('\n').split(',')
    list1.append(int(list2[1])-1)

x1 = []
y1 = []
for i in range(0,len(list1)):
    x1.append(x[list1[i]])
    y1.append(y[list1[i]])


###shrinking
f = open('result/shrinking.csv')
lines = f.readlines()
f.close()
list3 = []
for i in range(1,len(lines)):
    list2 = lines[i].strip('\n').split(',')
    list3.append(int(list2[1])-1)

x2 = []
y2 = []
for i in range(0,len(list3)):
    x2.append(x[list3[i]])
    y2.append(y[list3[i]])


###  other
x3 = []
y3 = []
for i in range(0,183):
    if((i not in list1) and(i not in list3)):
        x3.append(x[i])
        y3.append(y[i])


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=1200,xmin=0)
plt.ylim(ymax=1200,ymin=0)

colors1 = '#00CED1'
colors2 = '#DC143C'

plt.scatter(x1, y1, s=20,c='black',marker='x', alpha=1, label='growing')
plt.scatter(x2, y2, s=20,c='black',marker='s', alpha=1, label='shrinking')
plt.scatter(x3, y3, s=1,c='black',marker='o', alpha=1, label='normal')

plt.legend()
plt.show()