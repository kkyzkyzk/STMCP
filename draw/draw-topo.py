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


f1 = open('topo.csv')
lines1 = f1.readlines()
f1.close()
topo =[]
for line in lines1:
    list3 = line.strip('\n').split(',')
    topo.append(list3)


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=1200,xmin=0)
plt.ylim(ymax=1200,ymin=0)


for i in range(len(topo)):
    for j in range(len(topo)):
        if topo[i][j]=='mainCode' and i!=j:
            x1 = [x[i],x[j]]
            y1 = [y[i],y[j]]
            plt.plot(x1, y1, color='r')




plt.scatter(x, y, c='navy', alpha=0.4, label='BS')



plt.legend()
plt.show()