import time

# info arch
class Collection:
    def __init__(self):
        self.data = set()

    def find_or_create(self, cls, name, sys_type):
        obj = next((x for x in self.data if x.name == name), None)
        if obj is None:
            obj = cls(name,sys_type)
            # obj.name = name
            # obj.sys_type = sys_type
            self.data.add(obj)
        return obj

    @property
    def length(self):
        return len(self.data)

class System:
    data = Collection()
    @classmethod
    def find_or_create(cls, name, sys_type = "System" ):
        return cls.data.find_or_create(cls,name,sys_type)

    @classmethod
    def find_or_create2(cls, name, sys_type = "System" , external = False ):
        # print("find_or_create2: name : {} external:{}".format(name  , external))
        system = cls.data.find_or_create(cls,name,sys_type)
        system.external = external
        if external :
            system.sys_type = "ExternalSystem"
        return system;

    def __init__(self,name,sys_type):
        super().__init__()
        self.name = name
        self.sys_type = sys_type
        self.external = False
        self.operations = set()
        self.functions = set()
    
    def add_operation(self,name):
        operation = Operation.find_or_create(name)
        if operation not in self.operations:
            self.operations.add(operation)
        return operation

    def add_funcation(self,name,read_only):
        func = Function(name,read_only)
        self.functions.add(func)
        return func

    def set_operations(self,operations):
        self.operations = operations

    def set_funcations(self,functions):
        self.functions = functions
    
    def __str__(self):
        return "{} {}".format(self.name,self.sys_type)

class Function:
    data = Collection()
    @classmethod
    def find_or_create(cls, name):
        return cls.data.find_or_create(cls,name,"Function")

    @classmethod
    def get_or_create_function(cls,system,function,read_only, external):
        if external:
            sys = System.find_or_create(system,"ExternalSystem")
        else:
            sys = System.find_or_create(system)
        func = cls.find_or_create("{}_{}".format(system,function))
        func.read_only = read_only
        func.system = sys
        return func

    def __init__(self,name, read_only = True):
        super().__init__()
        self.name = name
        self.read_only = read_only
        self.system = None
        self.operations = []

class Span:
    data = Collection()
    def __init__(self,func,parent = None, request = None):
        self.parent = parent
        self.children = []
        self.func = func
        if request:
            self.request = request
        else:
            self.request = parent.request

    def span(self,system,function = None,read_only = True, external = False):
        if function is None:
            function = self.parent.func.name
        span = Span(Function.get_or_create_function(system,function,read_only, external),parent = self)
        self.children.append(span)
        return span

    def spanningtree(self,ret = []):
        ret.append(self)
        for i in self.children:
            i.spanningtree(ret)
        return ret

    def __str__(self):
        return "{} {}".format(self.func.system,self.func.name)

class Request:
    data = Collection()
    @classmethod
    def find_or_create(cls, role, name):
        name = "{}_{}".format(role,name)
        return cls.data.find_or_create(cls,name,"Request")

    def __init__(self,name,business,read_only = True):
        super().__init__()
        self.name = name
        self.trace = []
        self.business = business
        self.read_only = read_only
    
    def span(self,system,function = None,read_only = None, external = False):
        if function is None:
            function = self.name
        self.root = Span(Function.get_or_create_function(self.role.name,self.name,read_only=False,external=True),request=self)
        return self.root.span(system,function,read_only, external)
    
    def spanningtree(self):
        return self.root.spanningtree([])

class Journey:
    data = Collection()
    @classmethod
    def find_or_create(cls, name):
        return cls.data.find_or_create(cls,name)

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.operations = set()
        self.connections = []

        # node = self.nodes.append("root")
    def add_operation(self,operation,ops_from = [], ops_to = []):
        self.operations.add(operation)        
        for i in ops_from:
            self.connections.append((i,operation))
        for i in ops_to:
            self.connections.append((operation,i))

class Operation:
    data = Collection()
    @classmethod
    def find_or_create(cls, name):
        return cls.data.find_or_create(cls,name)

    def __init__(self,name,role = None, action = None):
        super().__init__()
        self.name = name
        self.role = role
        self.action = action
        self.functions = []

    def set_functions(self,functions):
        self.functions = functions

    def create_default_funcation(self, system, read_only = True):
        func = Function.find_or_create(self.name)
        func.system = system
        func.read_only = read_only
        func.operations = [self]
        self.functions.append(func)
        return func

    def is_read_only(self):
        for i in self.functions:
            if not i.read_only:
                return False
        return True

    def default_system(self):
        return self.functions[0].system
