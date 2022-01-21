import yaml

class SystemConfig:
    def __init__(self):
        with open('systems.yml', encoding='utf-8') as f: 
            self.org_data = yaml.safe_load(f)
            self.data = self.get_dict_by_group_name("tongye")
            self.data = self.merge(self.data, self.get_dict_by_group_name("tuoguan"))
            self.data = self.merge(self.data, self.get_dict_by_group_name("guijinshu"))
            self.data = self.merge(self.data, self.get_dict_by_group_name("jiaoyi"))
            self.data = self.merge(self.data, self.get_dict_by_group_name("chanpin"))
    
    def get_dict_by_group_name(self , name):
        systems = self.org_data[name]['systems'] 
        return dict(zip(systems, [name] * len(systems)))

    def get_owner_by_name(self, name):
        if name not in self.data:
            return "Unkown"
        return self.data[name]

    def merge(self, dict1, dict2): 
        return {**dict1, **dict2} 

# if __name__ == "__main__":
#     print(SystemConfig().get_owner_by_name("行E通产品代销子系统"))
#     print(SystemConfig().get_owner_by_name("证券资金清算子系统（上海）"))
# if __name__ == "__main__":
#     print(SystemConfig().get_owner_by_name("行E通产品代销子系统"))
#     print(SystemConfig().get_owner_by_name("证券资金清算子系统（上海）"))