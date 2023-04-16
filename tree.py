
class Ctl_Tree():
    def __init__(self,num,graph):
        self.num = num
        self.graph = graph
        self.child = list()

    def get_number(self):
        return self.num

    def get_graph(self):
        return self.graph

    def insert_child(self,child):
        self.child.append(child)

    def insert_init_child(self,num,graph):
        t = Ctl_Tree(num,graph)
        self.child.append(t)

    def get_child(self):
        return self.child

    def change_graph(self,graph):
        self.graph = graph

