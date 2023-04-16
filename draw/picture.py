import matplotlib.pyplot as plt

f = open('../resource/point.csv')
lines = f.readlines()
f.close()
x = []
y = []
for line in lines:
    list2 = line.strip('\n').split(',')
    x.append(float(list2[0]))
    y.append(float(list2[1]))

x1 = x[0:180]
x2 = x[180:183]
y1 = y[0:180]
y2 = y[180:183]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=1200,xmin=0)
plt.ylim(ymax=1200,ymin=0)

colors1 = '#00CED1'
colors2 = '#DC143C'

plt.scatter(x1, y1, c=colors1, alpha=0.4, label='微基站')
plt.scatter(x2, y2, c=colors2, alpha=0.4, label='宏基站')


plt.legend()
plt.show()