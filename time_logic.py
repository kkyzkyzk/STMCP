import logic

def X(stmode,status,operational):
    dict = {'allnode' : stmode[status+1],'nodelist' : []}
    exec(operational,dict)
    return dict['nodelist']

def F(stmode,status_start,status_end,operational):
    endlist = []
    outlist = []
    for i in range(status_start,status_end):
        dict = {'allnode' : stmode[i],'nodelist' : []}
        exec(operational,dict)
        endlist.append(dict['nodelist'])

    for list in endlist:
        for i in range(len(list)):
            if(list[i].get_num() not in outlist):
                outlist.append(list[i].get_num())

    return outlist



def G(stmode,status_start,status_end,operational):
    endlist = []
    outlist = []
    for i in range(status_start, status_end):
        dict = {'allnode': stmode[i], 'nodelist': []}
        exec(operational, dict)
        endlist.append(dict['nodelist'])

    for i in range(len(endlist)):
        inlist = []
        delete_list = []
        if(i == 0):
            for j in range(len(endlist[i])):
                outlist.append(endlist[i][j].get_num())
        else:
            for j in range(len(endlist[i])):
                inlist.append(endlist[i][j].get_num())
            for j in range(len(outlist)):
                if(outlist[j] not in inlist):
                    delete_list.append(outlist[j])
            for j in range(len(delete_list)):
                outlist.remove(delete_list[j])

    return outlist


def U(stmode,status_start,status_end,operational1,operational2):
    endlist = []
    outlist = []
    for i in range(status_start,status_end):
        dict2 = {'allnode': stmode[i], 'nodelist': []}
        exec(operational2, dict2)
        endlist.append(dict2['nodelist'])

    for i in range(len(endlist)):
        inlist = []
        for j in range(len(endlist[i])):
            inlist.append(endlist[i][j].get_num())
        glist = G(stmode,status_start,i,operational1)
        for j in range(len(glist)):
            if(glist[j] in inlist):
                outlist.append(glist[j])

    return outlist