from app.model import System,Operation,Function,Request
from app.injector import Injector

class DDD:
    def __init__(self,name):
        self.name = name
        self.injector = Injector()
        self.connections = set()
        self.sub_connections = set()
        self.events = set()
        self.categories = set()

    def create_domain(self, domains):
        return [System.find_or_create(i, sys_type="Domain") for i in domains]

    def add_sub(self,root,name):
        self.sub_connections.add((System.find_or_create(root, sys_type="Domain"),System.find_or_create(name,sys_type="SubDomain")))

    def connect(self,up,down):
        self.connections.add((System.find_or_create(up, sys_type="Domain"), System.find_or_create(down, sys_type="Domain")))

    def dependent(self, up, down):
        self.connections.add((System.find_or_create(up, sys_type="Category"), System.find_or_create(down, sys_type="Category")))

    def bind_events(self,doman_name,events):
        domain = System.find_or_create(doman_name, sys_type="Domain")
        for i in events:
            self.events.add((domain, System.find_or_create(i, sys_type="Event")))

    def bind_event(self, doman_name, event):
        self.events.add((System.find_or_create(doman_name, sys_type="Domain"), System.find_or_create(event, sys_type="Event")))

    def category(self, group_name , domains):
        c = System.find_or_create(group_name, sys_type= "Category")
        for i in domains:
            self.categories.add((c,  System.find_or_create(i, sys_type="Domain")))

    def generate_graph(self,injector):
        for i in System.data.data:
            injector.create_node(i.name,i.sys_type,{})
        for i in self.connections:
            if i[0].sys_type == "Category":
                injector.create_edge(i[0].name,i[1].name,"DependentOn",{})
            else:
                injector.create_edge(i[0].name,i[1].name,"UseBy",{})
        for i in self.sub_connections:
            injector.create_edge(i[0].name,i[1].name,"Contains",{})
        for i in self.categories:
            injector.create_edge(i[1].name,i[0].name,"In",{})

        for i in self.events:
            injector.create_edge(i[0].name,i[1].name,"Binds", {})

        community = injector.graph("myGraph","Domain","UseBy")
        for i in community:
            injector.update_node(i[0],{"community":i[1]})

    def plus(self,ddd):
        if ddd is not None:
            for i in ddd.connections:
                self.connections.add(i)
        return self
