from app.model import System,Operation,Function,Request
from app.injector import Injector
from app.config import SystemConfig
class DFD:
    def __init__(self,name):
        self.name = name
        self.systems = set()
        self.requests = set()

    def create_request(self, role, name, read_only = True):
        _role = System.find_or_create(role, sys_type="Role")
        req = Request.find_or_create(_role.name,name)
        req.role = _role
        req.business = self.name
        req.read_only = read_only
        self.requests.add(req)
        return req

    # def create_system_request(self, system, name, read_only = True):
    #     _role = System.find_or_create(system, sys_type="System")
    #     req = Request.find_or_create(_role.name,name)
    #     req.role = _role
    #     req.read_only = read_only
    #     self.requests.add(req)
    #     return req

    def create_system_request(self, system, name, external = False, read_only = True):
        _role = System.find_or_create2(system, "System" , external)
        req = Request.find_or_create(_role.name,name)
        req.role = _role
        req.read_only = read_only
        req.business = self.name
        self.requests.add(req)
        return req

    def get_systems(self):
        return list(System.data.data)
    
    def plus(self,dfd):
        if dfd is not None:
            for i in dfd.requests:
                self.requests.add(i)
        return self

    def generate_app_graph(self,injector):
        self.injector = injector
        self.generate_nodes()
        for i in self.requests:
            if i.business != "Request":
                self.injector.create_node(i.business, "Business", {"name":i.business})
            for j in i.spanningtree():
                if j.func.system.sys_type not in ["Role", "Business"] and j.func.system.name != i.business:
                    self.injector.create_edge(i.business,j.func.system.name, "Supportedby", {})
                for m in j.children:
                    self.injector.create_edge(j.func.system.name,m.func.system.name,"Use" ,{"shorname":j.func.name.split("_")[-1],"request":i.name})

    def generate_app_network(self,injector):
        self.injector = injector
        self.injector.merge_relationship()

    def generate_nodes(self):
        config = SystemConfig()
        for i in self.get_systems():
            i.owner = "Unknown"
            if i.sys_type == "System":
                i.owner = config.get_owner_by_name(i.name)
            self.injector.create_node(i.name, i.sys_type, {"name":i.name, "owner" : i.owner})

    def connect_nodes(self,start,end,properties={}):
        self.injector.create_edge(start,end,"Use",properties)

    def generate_network(self):
        self.generate_nodes()
        edges = {}
        for i in self.requests:
            for j in i.spanningtree():
                for m in j.children:
                    edge = (j.func.system.name,m.func.system.name)
                    if  edge not in edges:
                        edges[edge] = 0
                    edges[edge] = edges[edge] + 1
        for i in edges:
            self.injector.create_edge(i[0],i[1],"Use",{"count":edges[i]})

    def generate_graph(self):
        self.generate_nodes()
        edges = {}
        for i in self.requests:
            for j in i.spanningtree():
                for m in j.children:
                    self.injector.create_edge(j.func.system.name,m.func.system.name,"Use" ,{"shorname":j.func.name.split("_")[-1],"request":i.name})