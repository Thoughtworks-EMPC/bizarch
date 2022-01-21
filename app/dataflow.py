from app.model import System,Operation,Function,Request
from app.injector import Injector

class Node:
    data = Collection()
    @classmethod
    def find_or_create(cls, name):
        return cls.data.find_or_create(cls, name, sys_type = "NODE")
    
    def __init__(self,name,sys_type):
        super().__init__()
        self.name = name
        self.sys_type = sys_type
        self.next = set()
    
    def next(self,name):
        node = Node.find_or_create(name)
        self.next.add(node)

class Flow:
    data = Collection()
    @classmethod
    def find_or_create(cls, name):
        return cls.data.find_or_create(cls, name, sys_type = "FLOW")

    def __init__(self,name,sys_type):
        super().__init__()
        self.name = name
        self.sys_type = sys_type
        self.steps = []
        self.node = None
    
    def start(self,name):
        node = Node.find_or_create(name)
        self.node = node
        return self

    def next(self,name):
        node = Node.find_or_create(name)
        self.steps.append((self.node,node))
        self.node = node
        return self

class DFD:
    def __init__(self,name):
        self.name = name
        self.systems = set()
        self.requests = set()
        self.injector = Injector()

    def create_request(self, role, name, read_only = True):
        _role = System.find_or_create(role, sys_type="Role")
        req = Request.find_or_create(_role.name,name)
        req.role = _role
        req.read_only = read_only
        self.requests.add(req)
        return req
