# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import load_graph
import topologic_node
import numpy as np
import logic

import random
import space_time
import time_logic

if __name__ == '__main__':


    #nodelist是节点总表
    nodelist = load_graph.load_g('mainCode.txt','ap.txt')
    list1 = logic.I(logic.p(nodelist,'yellow'))
    logic.print_num(list1)


  #  list1 = list()
  #  list1.append(nodelist[mainCode])
  #  list2 = list()
  #  list2.append(nodelist[0])
  #  newlist = logic.P(list1,list2)

  #  print(newlist[mainCode].get_num())

  #  logic.S(nodelist, logic.p(nodelist, 'yellow'), logic.p(nodelist, 'red'))
  #  newlist = logic.P(logic.p(nodelist, 'red'), logic.p(nodelist, 'yellow'))
  #  logic.print_num(newlist)

  #  stmode = space_time.tpmode('mainCode.txt','rongliang.txt','ap.txt',5,'fuzai.txt')
  #  stmode[4][0].delete_atomic('yellow')
  #  stmode[4][0].append_atomic('red')
  #  nodelist = time_logic.U(stmode,0,5,'import logic\nnodelist = logic.p(allnode, "yellow")','import logic\nnodelist = logic.p(allnode, "red")')
  #  print(nodelist)
    #print(mainCode)
