import sys
import importlib
import json
from app.injector import Injector
from app.biz import BizBlueprint
from data.biz import BizAll
from app.community import Community
import os

def get_arg(key,default_value = None, args = None):
    if key in os.environ:
        return os.environ[key]
    if args and key in args:
        return args[key]
    return default_value

if __name__ == "__main__":
    host = get_arg("host","localhost")
    injector = Injector(host = host)

    command = sys.argv[1]
    if command == "biz":
        BizAll(injector).generate_graph()
        sys.exit()

    if command == "clear":
        injector.clear()
        sys.exit()


    if command == "ddd":
        data = sys.argv[2].split(',')
        modules =  list(map(lambda x: importlib.import_module("data.{}".format(x)),data))
        ddd = None
        for i in modules:
            ddd = i.ddd().plus(ddd)
        ddd.generate_graph(injector)
        sys.exit()

    if command == "community":
        Community().write("records.json")
        sys.exit()

    data = sys.argv[2].split(',')
    modules =  list(map(lambda x: importlib.import_module("data.{}".format(x)),data))
    dfd = None
    for i in modules:
        dfd = i.biz().plus(dfd)

    if command == "network":
        dfd.generate_app_network(injector)
        sys.exit()
    if command == "graph":
        dfd.generate_app_graph(injector)
        sys.exit()

    print("unknown command {}".format(command))
