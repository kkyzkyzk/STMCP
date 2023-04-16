#空间节点
class Node:
    #初始化函数，给出节点编号，邻接关系表
    def __init__(self, num, nearnode):
        self.num = num
        self.nearnode = nearnode
        self.atomic_propositions = list()
        self.capacity = 0
        self.loadnow = 0
        self.ExternalLoad = 0

    #增加原子命题约束
    def append_atomic(self, atomic_proposition):
        self.atomic_propositions.append(atomic_proposition)

    #删除原子命题约束
    def delete_atomic(self, atomic_proposition):
        self.atomic_propositions.remove(atomic_proposition)

    #读取该节点所有原子命题约束
    def get_atomic(self):
        return self.atomic_propositions

    #验证该节点是否满足find_ap的原子命题
    def find_atomic(self,find_ap):
        if (find_ap in self.atomic_propositions):
            return True
        else:
            return False

    #读取该节点所有邻接关系
    def get_near(self):
        return self.nearnode

    #读取该节点编号
    def get_num(self):
        return self.num

    #修改当前负载
    def change_loadnow(self,loadnow):
        self.loadnow = loadnow

    #读取当前负载
    def get_loadnow(self):
        return self.loadnow

    #修改容量
    def change_capacity(self,capacity):
        self.capacity = capacity

    #读取容量
    def get_capacity(self):
        return self.capacity

    #读取外部负载
    def get_ExternalLoad(self):
        return self.ExternalLoad

    #修改外部负载
    def change_ExternalLoad(self,ExternalLoad):
        self.ExternalLoad = self.ExternalLoad + ExternalLoad