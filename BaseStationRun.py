import load_graph
import topologic_node
import numpy as np
import logic

import random
import space_time
import time_logic

stmode = space_time.tpmode('t2.csv','33.csv','44.txt',144,'t1.csv')
#stmode = space_time.tpmode_ctl('t2.csv','33.csv','44.txt','tree.txt','t1.csv')

stmode = logic.loadtrans_ltl(stmode)

nodelist = time_logic.X(stmode,0,'import logic\nnodelist = logic.p(allnode, "full")')
print(logic.obj_to_num(nodelist))


fulllist = time_logic.F(stmode,0,144,'import logic\nnodelist = logic.p(allnode, "full")')
clulist = time_logic.F(stmode,0,144,'import logic\nnodelist = logic.I(logic.p(allnode, "low"))')

clulist = time_logic.F(stmode,0,144,'import logic\nnodelist = logic.S(allnode,logic.p(allnode,"full"),logic.p(allnode,"normal"))')
for i in range(len(clulist)):
    print(clulist[i])

