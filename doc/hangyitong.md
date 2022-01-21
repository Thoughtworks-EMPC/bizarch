### 业务概览  

#### 客户管理部  
    * 同业买方客户引入  
#### 产品管理部  
    * 同业卖方产品引入  
#### 渠道管理部  
    * 同业买方客户引入  
#### 另类投资管理部  
    * 非持牌买方客户引入  
#### 平台开发及应用管理部   
    * 平台交易  
#### 网金部  
    * 运营数据分析  
#### 投后及销后管理部  
    * 同业项目合规  
#### 业务支持部  
    * 同业业务考核

### 同业买方客户引入业务  
#### 简介  
客户经理和理财/基金等同业机构洽谈，入驻行E通平台
#### 场景  
```
    dfd = DFD("同业客户引入")

    dfd.create_request("客户管理部","同业用户录入").span("BECIF").span("同业CRM子系统") 
    dfd.create_request("同业买方客户","注册行E通用户").span("行E通门户").span("行E通产品子系统").span("ODS"）
    dfd.create_request("客户管理部","审核行E通用户").span("行E通产品子系统")
```

### 同业产品引入业务  
#### 简介  
客户经理和理财/基金等同业机构洽谈引入的产品
#### 场景  
```
    dfd = DFD("同业产品引入")

    dfd.create_request("产品管理部","同业产品引入").span("同业销售产品工厂")
    dfd = DFD("同业产品行E通管理")
    dfd.create_request("注册卖方","同业产品引入申请").span("行E通门户").span("行E通产品子系统)
    dfd.create_request("产品管理部","同业产品引入审批").span("行E通门户").span("行E通产品子系统)
    dfd.create_request("产品管理部" , "同业产品上下架").span("行E通产品子系统)
```

### 产品销售业务
#### 简介  
分行和渠道管理部的客户经理销售同业相关产品
#### 场景  
```
    dfd = DFD("同业产品销售")

    dfd.create_request("各地方分行金融同业事业部","三方存管销售").span("三方存管")
    dfd.create_request("各地方分行金融同业事业部","同业非标产品销售").span("TIMP").span("MUREX")
    dfd.create_request("各地方分行金融同业事业部","同业标准产品销售").span("三方存管") #？
    dfd.create_request("渠道管理部","三方存管销售").span("三方存管")
```

### 产品投资业务
#### 简介  
组合管理部和另类投资部的交易员进行同业资金投资
#### 场景  
```
    dfd = DFD("同业标准产品投资")

    dfd.create_request("组合管理部","同业标准产品投资").span("TIMP").span("MUREX")
    dfd.create_request("另类投资部","同业非标产品投资").span("TIMP").span("MUREX")
```

### 同存业务
#### 简介  
组合管理部进行同存业务的存放和存款
#### 场景  
```
    dfd = DFD("同业存放")

    dfd.create_request("组合管理部","同业存放").span("TIMP").span("MUREX")
    dfd = DFD("同业存款")
    dfd.create_request("组合管理部","同业存款产品管理").span("行E通产品子系统")
    dfd.create_request("行E通","同业存款").span("行E通门户").span("行E通产品子系统").span("TIMP")
    dfd.create_request("组合管理部","同业存款").span("TIMP").span("MUREX")
    dfd.create_request("另类投资部","同业非标产品投资").span("TIMP").span("MUREX")
```

### 行E通代销业务
#### 简介  
分行和渠道管理部的客户经理在行E通代销其他同业相关产品
#### 场景  
```
    dfd = DFD("行E通代销")

    dfd.create_request("各地方分行金融同业事业部","行E通代销").span("行E通")
    dfd.create_request("渠道管理部","行E通代销").span("行E通")
    dfd.create_request("同业买方客户" , "查看资讯").span("行E通门户").span("同业资讯")
```

### 同业业务考核业务  
#### 简介  
同业业务客户经理考核业务
#### 场景  
```
    dfd = DFD("同业业务考核")

    dfd.create_request("业务支持部","同业业务考核").span("PMS")
```

### 同业项目合规业务  
#### 简介  
产品销售或者投资完成后的风控和合规管理
#### 场景  
```
    dfd = DFD("同业项目合规")

    dfd.create_request("投后及销后管理部","同业项目合规").span("TIMP")
```