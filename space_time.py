#创建时空模型，其实就是列表的嵌套；空间模型说到底就是一个点的集合（列表）
#那么线性的时空模型，就是把空间模型放到一个列表里面
#核心是每一时间片上的空间模型，哪些地方不同

##2021.3.31 此模型为LTL时序逻辑模型，并非CTL
import load_graph
import topologic_node
import tree

#matrix为邻接矩阵，capacityname为容量表，apname为原子命题，timesum为时间步的总数，bslname为一个基站负载变化表
def tpmode(matrix,capacityname,apname,timesum,bslname):
    tplist = list()
    bs_end = load_graph.load_bsload(bslname)

    for i in range(timesum):
        tl1 = load_graph.load_bs(matrix,capacityname,apname)
        for j in range(len(tl1)-1):
            tl1[j].change_loadnow(bs_end[i][j])
        tplist.append(tl1)

    return tplist

##2021.4.12  以下为CTL时序逻辑模型，Kripke结构
#tree_txt   每行第一个为父节点，后续以空格间隔的每个值，都是子节点

def tpmode_ctl(matrix,capacityname,apname,tree_txt,bslname):
    bs_end = load_graph.load_bsload(bslname)

    tree1 = list()
    num = 0
    for i in range(len(bs_end)):
        tl1 = load_graph.load_bs(matrix, capacityname, apname)
        for j in range(len(tl1)):
            tl1[j].change_loadnow(bs_end[i][j])
        treenode = tree.Ctl_Tree(num,tl1)
        tree1.append(treenode)
        num = num + 1

    t = open(tree_txt)
    lines = t.readlines()
    t.close()

    for line in lines:
        list1 = line.strip('\n').split(' ')
        for i in range(1,len(list1)):
            tree1[int(list1[0])].insert_child(tree1[int(list1[i])])

    return tree1
















