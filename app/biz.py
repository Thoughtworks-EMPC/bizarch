from app.model import Collection


class BizBlueprint:
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.root = Group.find_or_create(name, type="Head")

    def generate_nodes(self):
        for i in self.get_systems():
            self.injector.create_node(i.name, i.sys_type, {"name":i.name})

    def connect_nodes(self,start,end,properties={}):
        self.injector.create_edge(start,end,"Use",properties)
    
    @property
    def businesses(self):
        return self.root.biz_all()

    def generate_business(self,injector = None):
        self.injector = Injector() if injector is None else injector
        for i in self.businesses:
            self.injector.create_node(i.name, "Business", {"name":i.name,"groups":",".join(list(map(lambda x : x.name, i.groups)))})

    def generate_groups(self,injector = None):
        self.injector = Injector() if injector is None else injector
        tree = self.root.tree([])
        for i in tree:
            self.injector.create_node(i.name, i.sys_type, {"name": i.name})
            for j in i.businesses:
                self.injector.create_edge(i.name,j.name,"Operate",{})
            if i.parent is not None:
                self.injector.create_edge(i.parent.name,i.name,"Manage",{})

class Group:
    data = Collection()
    @classmethod
    def find_or_create(cls, name, type= "Group"):
        return cls.data.find_or_create(cls, name, sys_type = type)
    
    def __init__(self,name,sys_type):
        super().__init__()
        self.name = name
        self.children = set()
        self.businesses = set()
        self.parent = None
        self.sys_type = sys_type

    def child(self,name):
        ret = Group.find_or_create(name)
        ret.parent = self
        self.children.add(ret)
        return ret

    def tree(self,ret):
        ret.append(self)
        for i in self.children:
            i.tree(ret)
        return ret

    def bind_biz(self,name,biz_type = "ZIYING"):
        ret = Biz.find_or_create(name,biz_type)
        self.businesses.add(ret)
        ret.owner = self
        ret.groups.add(self)
        return ret

    def bind_bizs(self,names , biz_type = "ZIYING") :
        for x in names:
            self.bind_biz(x)

    def biz_all(self):
        ret = []
        for i in self.tree([]):
            ret.extend(i.businesses)
        return ret

class Biz:
    data = Collection()
    @classmethod
    def find_or_create(cls, name, biz_type):
        return cls.data.find_or_create(cls,name,biz_type)

    def __init__(self,name,biz_type):
        super().__init__()
        self.name = name
        self.biz_type = biz_type
        self.owner = None
        self.groups = set()

