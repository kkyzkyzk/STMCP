import numpy as np
import topologic_node

#读取txt文件内的邻接矩阵，返回np.array格式的二维数组
def load_g(txtname,apname):
    f = open(txtname)
    lines = f.readlines()
    f.close()
    point_number = len(lines)
    graph_m = np.zeros((point_number, point_number), dtype=int)
    graph_m_row = 0
    for line in lines:
        list1 = line.strip('\n').split(' ')
        graph_m[graph_m_row] = list1
        graph_m_row += 1

    nodelist = list()  # nodelist是节点总表
    for i in range(len(graph_m)):
        nearlist = list()
        for j in range(len(graph_m[i])):
            if (graph_m[i][j] == 1):
                nearlist.append(j)

        node = topologic_node.Node(i, nearlist)
        nodelist.append(node)

    ap = load_ap(apname)
    for i in range(len(ap)):
        nodelist[ap[i][0]].append_atomic(ap[i][1])

    return nodelist
#    return graph_m

#读取txt文件内的原子命题
def load_ap(txtname):
    f = open(txtname)
    lines = f.readlines()
    f.close()
    ap_list = list()
    for line in lines:
        list1 = line.strip('\n').split(' ')
        list1[0] = int(list1[0])
        ap_list.append(list1)
    return ap_list



def load_bsload(txtname):
    f = open(txtname)
    lines = f.readlines()
    f.close()
    bs_list = list()
    for line in lines:
        list1 = line.strip('\n').split(',')
        for i in range(len(list1)):
            list1[i] = int(list1[i])
        bs_list.append(list1)

    bs_end = list()  #最终的总表
    for i in range(len(lines)):
        bs_in = [0]*183
        for j in range(len(bs_list[i])):
            bs_in[bs_list[i][j]-1] += 1    ##@有问题
        bs_end.append(bs_in)


    return bs_end

def load_capacity(txtname):
    f = open(txtname)
    line1 = f.readline()

    capacity_list = line1.strip('\n').split(',')
    f.close()
    for i in range(0,len(capacity_list)):
        capacity_list[i] = int(capacity_list[i])
    return capacity_list

def load_bs(matrix,capacityname,apname):
    f = open(matrix)
    lines = f.readlines()
    f.close()
    point_number = len(lines)
    graph_m = np.zeros((point_number, point_number), dtype=int)
    graph_m_row = 0
    for line in lines:
        list1 = line.strip('\n').split(',')
        graph_m[graph_m_row] = list1
        graph_m_row += 1

    nodelist = list()  # nodelist是节点总表
    for i in range(len(graph_m)):
        nearlist = list()
        for j in range(len(graph_m[i])):
            if (graph_m[i][j] == 1):
                nearlist.append(j)

        node = topologic_node.Node(i, nearlist)
        nodelist.append(node)

    ap = load_ap(apname)
    for i in range(len(ap)):
        nodelist[ap[i][0]].append_atomic(ap[i][1])

    capacity = load_capacity(capacityname)
    for i in range(len(capacity)):
        nodelist[i].change_capacity(capacity[i])

    return nodelist

#编号和对象类的转换
def obj_to_num(nodelist):
    numlist = []
    for i in range(len(nodelist)):
        numlist.append(nodelist[i].get_num())

    return numlist

def num_to_obj(allnode,numlist):
    new_nodelist = []
    for i in range(len(numlist)):
        for j in range(len(allnode)):
            if(numlist[i] == allnode[j].get_num()):
                new_nodelist.append(allnode[j])

    return new_nodelist

def loadtrans_ctl(stmode):
    #先对满载站点进行负载转移
    for i in range(len(stmode)):
        graph = stmode[i].get_graph()
        for j in range(len(graph)):
            loadnow = graph[j].get_loadnow()
            capacity = graph[j].get_capacity()
            if(loadnow >= capacity):
                outload = loadnow - capacity
                near = graph[i].get_near()
                add_externalLoad = outload/len(near)
                for k in range(len(near)):
                    graph[near[k]].change_ExternalLoad(add_externalLoad)
        stmode[i].change_graph(graph)

    #离散化负载，转化为低中高三档
    for i in range(len(stmode)):
        graph = stmode[i].get_graph()
        for j in range(len(graph)):
            loadnow = graph[j].get_loadnow()
            capacity = graph[j].get_capacity()
            externalLoad = graph[j].get_ExternalLoad()
            if(loadnow + externalLoad >= capacity):
                graph[j].append_atomic('full')
            elif(loadnow + externalLoad < graph[j].get_capacity() and loadnow + externalLoad >= capacity/5):
                graph[j].append_atomic('normal')
            else:
                graph[j].append_atomic('low')
        stmode[i].change_graph(graph)

    return stmode

def loadtrans_ltl(stmode):
    for i in range(len(stmode)):
        for j in range(len(stmode[i])):
            if(stmode[i][j].get_loadnow() >= stmode[i][j].get_capacity()):
                stmode[i][j].append_atomic('full')
            elif(stmode[i][j].get_loadnow() < stmode[i][j].get_capacity() and stmode[i][j].get_loadnow() >= stmode[i][j].get_capacity()/3):
                stmode[i][j].append_atomic('normal')
            else:
                stmode[i][j].append_atomic('low')

    return stmode