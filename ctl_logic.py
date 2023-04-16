import new_logic
import tree
import load_graph



def AX(ctl_tree,status_start,operational):
    next_status = ctl_tree[status_start].get_child()
    dot = []
    for i in range(len(next_status)):
        dic = {'model': next_status[i].get_graph(), 'nodelist': [],'status_start': next_status[i].get_number(),
               'allnodeNum': load_graph.obj_to_num(next_status[i].get_graph()),
               'ctl_tree': ctl_tree}
        exec(operational, dic)
        dot.append(dic['nodelist'])

    #交集
    return list_and(dot)



def EX(ctl_tree,status_start,operational):
    next_status = ctl_tree[status_start].get_child()
    dot = []
    for i in range(len(next_status)):
        dic = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
        exec(operational, dic)
        dot.append(dic['nodelist'])

    # 并集
    return list_or(dot)



def AF(ctl_tree,status_start,operational):
    dot1 = []
    dic = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational, dic)
    dot1.append(dic['nodelist'])

    dot2 = []
    next_status = ctl_tree[status_start].get_child()
    for i in range(len(next_status)):
        dot2.append(AF(ctl_tree,next_status[i].get_number(),operational))

    return list_or(dot1.append(list_and(dot2)))



def EF(ctl_tree,status_start,operational):
    dot = []
    dic = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational, dic)
    dot.append(dic['nodelist'])

    next_status = ctl_tree[status_start].get_child()
    for i in range(len(next_status)):
        dot.append(EF(ctl_tree, next_status[i].get_number(), operational))

    return list_or(dot)



def AG(ctl_tree,status_start,operational):
    dot = []
    dic = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational, dic)
    dot.append(dic['nodelist'])

    next_status = ctl_tree[status_start].get_child()
    for i in range(len(next_status)):
        dot.append(AG(ctl_tree, next_status[i].get_number(), operational))

    return list_and(dot)



def EG(ctl_tree,status_start,operational):
    dot1 = []
    dic = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational, dic)
    dot1.append(dic['nodelist'])

    dot2 = []
    next_status = ctl_tree[status_start].get_child()
    for i in range(len(next_status)):
        dot2.append(EG(ctl_tree, next_status[i].get_number(), operational))

    return list_and(dot1.append(list_or(dot2)))



def AU(ctl_tree,status_start,operational1,operational2):
    dot11 = []
    dot12 = []
    dic1 = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational1, dic1)
    dot11.append(dic1['nodelist'])

    dic2 = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational2, dic2)
    dot12.append(dic2['nodelist'])

    dot2 = []
    next_status = ctl_tree[status_start].get_child()
    for i in range(len(next_status)):
        dot2.append(AU(ctl_tree, next_status[i].get_number(), operational1,operational2))

    return list_or(dot12.append(list_and(dot11.append(list_and(dot2)))))


def EU(ctl_tree,status_start,operational1,operational2):
    dot11 = []
    dot12 = []
    dic1 = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational1, dic1)
    dot11.append(dic1['nodelist'])

    dic2 = {'model': ctl_tree[status_start].get_graph(), 'nodelist': [], 'status_start': ctl_tree[status_start].get_number(),
           'allnodeNum': load_graph.obj_to_num(ctl_tree[status_start].get_graph()),
           'ctl_tree': ctl_tree}
    exec(operational2, dic2)
    dot12.append(dic2['nodelist'])

    dot2 = []
    next_status = ctl_tree[status_start].get_child()
    for i in range(len(next_status)):
        dot2.append(AU(ctl_tree, next_status[i].get_number(), operational1, operational2))

    return list_or(dot12.append(list_and(dot11.append(list_or(dot2)))))



#列表与
def list_and(list):
    if(not list):
        return []
    lf = list[0]
    for i in range(1,len(list)):
        nf = []
        for j in range(len(lf)):
            if(lf[j] in list[i]):
                nf.append(lf[j])
        lf = nf

    return lf

#列表或
def list_or(list):
    if (not list):
        return []
    lf = list[0]
    for i in range(1,len(list)):
        for j in range(len(list[i])):
            if(list[i][j] not in lf):
                lf.append(list[i][j])

    return lf









