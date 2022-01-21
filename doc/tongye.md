### 业务概览  

#### 客户管理部  
    * 同业客户引入  
#### 产品管理部  
    * 同业产品引入  
#### 组合管理部  
#### 另类投资管理部  
    * 产品投资  
#### 各地方分行金融同业事业部  
#### 渠道管理部  
    * 产品销售  
#### 网金部  
#### 平台开发及应用管理部   
    * 平台交易  
    * 运营数据分析  
#### 投后及销后管理部  
    * 同业项目合规  
#### 业务支持部  
    * 同业业务考核

### 同业客户引入业务  
#### 简介  
客户经理和理财/基金等同业机构洽谈，入驻行E通平台
#### 场景  
```
    dfd = DFD("同业客户引入")

    dfd.create_request("客户管理部","同业用户录入").span("BECIF").span("同业CRM子系统") 
    dfd.create_request("同业买方客户","注册行E通用户").span("行E通门户").span("行E通产品子系统").span("ODS")
    dfd.create_request("客户管理部","审核行E通用户").span("行E通产品子系统")
```

### 同业产品引入业务  
#### 简介  
客户经理和理财/基金等同业机构洽谈引入的产品
#### 场景  
```
    dfd = DFD("同业产品引入")

    dfd.create_request("产品管理部","债券同业产品引入").span("同业销售产品工厂")
    dfd.create_request("产品管理部","理财同业产品引入").span("行E通产品子系统").span("统一TA","产品同步")
    dfd.create_request("产品管理部","基金同业产品引入").span("行E通产品子系统").span("行E通产品代销子系统","产品同步")

    <!-- dfd.create_request("注册卖方","同业产品引入申请").span("行E通系统门户子系统").span("行E通产品子系统") -->
    dfd.create_request("产品管理部","同业产品引入审批").span("行E通系统门户子系统").span("行E通产品子系统")
    dfd.create_request("产品管理部" , "同业产品上下架").span("行E通产品子系统")
```

### 产品销售业务
#### 简介  
各地方分行金融同业事业部和渠道管理部的客户经理销售同业相关产品
#### 场景  
```
    dfd = DFD("同业产品销售")
    span = dfd.create_request("客户经理","查看产品").span("同E家")
    span.span("行E通产品子系统")
    span.span("同业销售产品工厂")

    dfd.create_request("各地方分行金融同业事业部","三方存管销售").span("第三方存管系统")
    dfd.create_request("各地方分行金融同业事业部","同业非标产品销售").span("TIMP").span("MUREX")

    dfd.create_request("各地方分行金融同业事业部","同业标准产品销售").span("第三方存管系统") #？
    dfd.create_request("渠道管理部","三方存管销售").span("第三方存管系统").span("行E通核心子系统")
    dfd.create_request("渠道管理部","银期存管").span("银期保证金存管子系统")
    dfd.create_request("渠道管理部","银衍存管").span("银衍保证金存管应用")

    dfd.create_request("产品经理","产品录入").span("智慧同业统一门户子系统","产品录入").span("同业销售产品工厂","产品录入")
    dfd.create_request("同业买方客户","查看资讯").span("行E通系统门户子系统").span("行E通产品子系统").span("同业资讯平台","产品资讯")
    dfd.create_request("同业买方客户","查看产品").span("行E通系统门户子系统").span("行E通产品子系统").span("同业销售产品工厂","产品列表")
    dfd.create_request("客户经理","录入报量和中标").span("智慧同业统一门户子系统").span("同业CRM子系统")

    dfd.create_request("同业买方客户","WOW").span("行E通电子交易市场").span("JET")
```

### 行E通代销业务  
#### 简介  
分行和渠道管理部的客户经理在行E通代销其他同业相关产品
#### 场景  
```
    dfd = DFD("行E通代销")

    #dfd.create_request("各地方分行金融同业事业部","行E通代销").span("行E通系统门户子系统").span("行E通产品子系统")
    #dfd.create_request("渠道管理部","行E通代销").span("行E通系统门户子系统").span("行E通产品子系统")
    dfd.create_request("同业买方客户" , "查看资讯").span("行E通系统门户子系统").span("同业资讯平台")
    dfd.create_request("同业买方客户","基金购买").span("行E通系统门户子系统").span("行E通产品子系统").span("行E通产品代销子系统").span("基金公司",external=True)    
```

### 同业销售线索业务  
#### 简介  
同业销售客户经理进行商机线索管理
#### 场景  
```
    dfd = DFD("同业销售线索")
    span = dfd.create_request("客户经理","工单创建").span("智慧同业统一门户子系统","创建工单").span("同业CRM子系统","创建工单")
    span.span("同业销售产品工厂","查询产品")
    dfd.create_request("客户经理","任务创建").span("智慧同业统一门户子系统","创建任务").span("同业CRM子系统","创建任务")
    dfd.create_request("业务员","任务更新").span("智慧同业统一门户子系统","更新任务").span("同业CRM子系统","更新任务")
    dfd.create_request("业务员","客户信息").span("智慧同业统一门户子系统","查看客户").span("同业CRM子系统","查看客户")
    dfd.create_system_request("同业CRM子系统","客户交易").span("行E通产品子系统","查询交易")
    dfd.create_system_request("同业CRM子系统","客户营销").span("推荐引擎","产品推荐",external=True)
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
    dfd.create_request("行E通","同业存款").span("行E通系统门户子系统").span("行E通产品子系统").span("TIMP")
    dfd.create_request("组合管理部","同业存款").span("TIMP").span("MUREX")
    dfd.create_request("另类投资部","同业非标产品投资").span("TIMP").span("MUREX")
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