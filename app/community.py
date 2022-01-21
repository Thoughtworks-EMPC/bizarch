import json
from app.injector import Injector

class Community:
    def __init__(self):
        super().__init__()
        self.injector = Injector()

    def write(self,file):
        with open(file, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
            for i in data:
                self.injector.update_node(i["name"],{"community":i["communityId"]})

