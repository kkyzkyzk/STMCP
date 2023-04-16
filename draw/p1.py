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




plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=1200,xmin=0)
plt.ylim(ymax=1200,ymin=0)


plt.scatter(x, y, s=40,c='black',marker='o', alpha=0.3)


plt.legend()
plt.show()