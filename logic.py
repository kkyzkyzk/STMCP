import load_graph


#输出函数
def print_num(list1):
    for i in range(len(list1)):
        print(list1[i].get_num())

def find_num(list1,key):
    for i in range(len(list1)):
        if(list1[i].get_num() == key):
            return True
    return False

#永真：直接返回当前所有节点
def T(allnode):
    return allnode

#原子命题：返回符合所传入的原子命题的节点
def p(nodelist, ap):
    new_nodelist = list()
    for i in range(len(nodelist)):
        if (nodelist[i].find_atomic(ap)):
            new_nodelist.append(nodelist[i])
    return new_nodelist

#非：输出当前节点列表以外的节点
def no(allnode, nodelist):
    new_nodelist = list()
    for i in range(len(allnode)):
        if (allnode[i] not in nodelist):
            new_nodelist.append(allnode[i])
    return new_nodelist

#与：两个集合的交集
def _and_(nodelist1, nodelist2):
    new_nodelist = list()
    for i in range(len(nodelist1)):
        if (nodelist1[i] in nodelist2):
            new_nodelist.append(nodelist1[i])
    return new_nodelist

#或：两个集合的并集
def _or_(nodelist1, nodelist2):
    new_nodelist = list()
    for i in range(len(nodelist1)):
        new_nodelist.append(nodelist1[i])
    for i in range(len(nodelist2)):
        if (nodelist2[i] not in new_nodelist):
            new_nodelist.append(nodelist2[i])
    return new_nodelist

#附近：得到与目标集合相邻的所有节点,包括其本身
def N(allnode, nodelist):
    new_nodelist = list()
    for i in range(len(nodelist)):
        new_nodelist.append(nodelist[i])
    for i in range(len(nodelist)):
        nearlist = nodelist[i].get_near()
        for j in range(len(nearlist)):
            for k in range(len(new_nodelist)):
                if (nearlist[j] == new_nodelist[k].get_num()):
                    break
            else:
                for h in range(len(allnode)):
                    if(nearlist[j] == allnode[h].get_num()):
                        new_nodelist.append(allnode[h])
    return new_nodelist

#传播：返回空间直到
def P(nodelist1, nodelist2):
    new_nodelist = list()
    for i in range(len(nodelist1)):
        new_nodelist.append(nodelist1[i])
    while (True):
        flag = 0
        for i in range(len(new_nodelist)):
            nearlist = new_nodelist[i].get_near()
            for j in range(len(nearlist)):
                for k in range(len(new_nodelist)):
                    if (nearlist[j] == new_nodelist[k].get_num()):
                        break
                else:
                    for h in range(len(nodelist2)):
                        if (nearlist[j] == nodelist2[h].get_num()):
                            new_nodelist.append(nodelist2[h])
                            flag = 1
        if(flag == 0):
            break

    return new_nodelist

#包围：返回空间包围
def S(allnode, nodelist1, nodelist2):
    new_nodelist = list()
    other_nodelist = no(no(N(allnode, nodelist2), nodelist2), nodelist1)
    while (True):
        flag = 0
        for i in range(len(other_nodelist)):
            nearlist = other_nodelist[i].get_near()
            for j in range(len(nearlist)):
                flag1 = 0
                for k in range(len(other_nodelist)):
                    if (nearlist[j] == other_nodelist[k].get_num()):
                        flag1 = 1
                        break
                if(flag1 == 0):
                    for h in range(len(nodelist1)):
                        if (nearlist[j] == nodelist1[h].get_num()):
                            other_nodelist.append(nodelist1[h])
                            flag = 1
        if (flag == 0):
            break

    new_nodelist = no(nodelist1, other_nodelist)
    return new_nodelist

#内部
def I(nodelist):
    new_nodelist = []
    for i in range(len(nodelist)):
        new_nodelist.append(nodelist[i])

    for i in range(len(nodelist)):
        nearlist = nodelist[i].get_near()
        for j in range(len(nearlist)):
            if(not find_num(nodelist,nearlist[j])):
                new_nodelist.remove(nodelist[i])
                break

    return new_nodelist


