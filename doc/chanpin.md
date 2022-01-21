### 业务概览
#### 金融交易部  
    * 账户贵金属
    * 柜台债券
    * 对公利率
    * 债券回购    
    * 报价平盘/市场数据

#### 资金运营中心  
    * 个人外汇
    * 对公外汇
    * 报价平盘/市场数据

#### 离岸金融中心  
    * 对公外汇

#### 自贸试验区分行  
    * 对公外汇
    * 对公利率

#### 香港分行金融市场部  
    * 港行外汇
    * 港行利率

#### 资金托管事业部  
    * 基金资金托管

### 账户贵金属业务  
#### 简介  
我行为个人客户提供的，采用账户记载形式，以人民币或美元买卖贵金属份额的投资交易产品.我行向客户提供账户贵金属交易报价，根据市场情况对交易报价进行调整，交易报价包括银行买入价、银行卖出价和账户贵金属转换报价。  
#### 场景  
#### 1. 开户  
客户须指定借记卡作为资金账户，用于资金收付;交易账户，用于核算买卖账户贵金属数量的收付;保证金账户，用于交易保证金的收付和损益核算。
```
    dfd.create_request("个人客户","账户贵金属签约开户") \
        .span("口袋银行",external=True) \
        .span("账户贵金属")
        #TBC D+是否要检查？

    dfd.create_request("管理员","账户贵金属签约开户审核") \
        .span("账户贵金属")
```

#### 2. 行情
产品有实时交易、挂单交易、定投交易、转换交易等多种交易方式
```
    dfd.create_request("个人客户","账户贵金属询价") \
        .span("口袋银行",external=True) \
        .span("账户贵金属","询价") \
        .span("报价引擎")
```

#### 3.交易
系统接受客户委托进行出入金和开平仓操作，在开市期间根据客户保证金情况，对不足的份额进行强制平仓
```
    dfd.create_request("个人客户","账户贵金属保证金出入金") \
        .span("口袋银行",external=True) \
        .span("账户贵金属") \
        .span("D+",external=True)

    dfd.create_request("个人客户","账户贵金属开平仓") \
        .span("口袋银行",external=True) \
        .span("账户贵金属")

    dfd.create_system_request("账户贵金属","强制平仓") \
        .span("报价引擎")
```

#### 4.清算和持仓
```
TBC
```

#### 5. 产品敞口计算和平盘  
系统根据账户贵金属交易敞口，确定需要平盘的份额，在外部市场进行平盘交易
```
    dfd.create_system_request("账户贵金属","敞口计算") \
        .span("MUREX")
    dfd.create_system_request("账户贵金属","平盘") \
        .span("DIMPLE") #  由于实时性要求，此处走DIMPLE
    dfd.create_system_request("账户贵金属","数据归集") \
        span("ODS",external=True)
```    

#### 6. 交易产品管理  
业务管理员配置相关交易产品品种  
```
    dfd.create_system_request("管理员","账户贵金属产品管理") \
        .span("账户贵金属")
``` 

### 柜台债券业务  
#### 简介  
个人和企业客户可以通过该业务交易银行间市场债券，目前我行提供交易的品种为国债和国家开发银行债券，广东省地方政府债。
#### 场景  
#### 1. 开户  
个人和企业客户在我行开设债券账号，由我行负责份额登记，相关账户和份额报备中债登进行管理
```
    dfd.create_request("个人客户","债券开户").span("柜台债券子系统").span("中债登")
    dfd.create_request("企业客户","债券开户").span("柜台债券子系统").span("中债登")
```

#### 2. 行情  
```
    dfd.create_request("个人客户","网银债券询价").span("口袋银行",external=True).span("柜台债券子系统")
    dfd.create_request("个人客户","交易通债券询价").span("零售交易通APP",external=True).span("柜台债券子系统")
    dfd.create_request("企业客户","网银债券询价").span("企业网银",external=True).span("柜台债券子系统")
    dfd.create_request("企业客户","交易通债券询价").span("企业交易通APP",external=True).span("柜台债券子系统")
    
    dfd.create_request("柜台柜员","债券询价").span("AB端",external=True).span("柜台债券子系统")

    dfd.create_system_request("柜台债券子系统","债券询价").span("JET",external=True)
```

#### 2. 交易  
```
    dfd.create_request("个人客户","网银债券买入").span("口袋银行",external=True).span("柜台债券子系统").span("IFMS","风险等级").span("D+","出金")
    dfd.create_request("个人客户","交易通债券买入").span("零售交易通APP",external=True).span("柜台债券子系统").span("IFMS","风险等级").span("D+","出金")
    dfd.create_request("个人客户","网银债券卖出").span("口袋银行",external=True).span("柜台债券子系统").span("D+","入金")
    dfd.create_request("个人客户","交易通债券卖出").span("零售交易通APP",external=True).span("柜台债券子系统").span("D+","入金")

    dfd.create_request("企业客户","网银债券买入").span("企业网银",external=True).span("柜台债券子系统").span("D+","出金")
    dfd.create_request("企业客户","交易通债券买入").span("企业交易通APP",external=True).span("柜台债券子系统").span("D+","出金")
    # TBC 企业是否也要做风险等级    
    dfd.create_request("企业客户","网银债券卖出").span("企业网银",external=True).span("柜台债券子系统").span("D+","入金")
    dfd.create_request("企业客户","交易通债券卖出").span("企业交易通APP",external=True).span("柜台债券子系统").span("D+","入金")
```

#### 3. 清算和持仓
TBC：不用清算，我行负责登记
```
    dfd.create_system_request("柜台债券子系统","交易记录").span("CFETS","外汇交易备案") #就是需要备案，不知道为什么
    dfd.create_system_request("柜台债券子系统","交易记录").span("中债登")
```

#### 4. 产品敞口计算和平盘  
```
    dfd.create_system_request("柜台债券子系统","交易记录").span("MUREX")
    dfd.create_system_request("柜台债券子系统","额度信息").span("MUREX")
    # 没有平盘，控制卖出额度
```

### 债券回购业务  
#### 简介  
#### 场景  
#### 1.  

### 报价平盘/市场数据业务  
TBC 是否就是贵金属/国债/外汇的平盘业务
#### 简介  
#### 场景  
#### 1.  

### 个人外汇业务  
#### 简介  
平安交易通个人外汇买卖业务指个人客户通过银行提供的报价和交易平台，在事前开立保证金账户并存入一定金额的交易保证金后，实现做多与做空双向选择的外汇交易工具。
#### 场景  
TBC: 是否存在开户过程，like:客户须指定借记卡作为资金账户，用于资金收付;交易账户，用于核算买卖账户贵金属数量的收付;保证金账户，用于交易保证金的收付和损益核算。
#### 1.行情  
```
    dfd.create_request("个人客户","获取报价") \
        .span("交易通APP") \
        .span("平安交易通") \
        .span("报价引擎") \
        .span("前置机") \
        .span("UBS","行情",external=True)
```

#### 2.交易  
在开市期间根据客户保证金情况，对不足的份额进行强制平仓
```
    dfd.create_request("个人客户","交易通保证金出入金") \
        .span("交易通APP") \
        .span("平安交易通") \
        # .span("验密") \
        .span("D+")

    dfd.create_request("个人客户","开仓") \
        .span("交易通APP") \
        .span("平安交易通") \
        .span("零售风险评测") \
        .span("MUREX")

    dfd.create_request("个人客户","平仓") \
        .span("交易通APP") \
        .span("平安交易通") \
        .span("MUREX")

    dfd.create_system_request("平安交易通","强制平仓") \
        .span("报价引擎")
```

#### 3.清算和持仓  
```
    dfd.create_request("个人客户","外汇持仓") \
        .span("交易通APP") \
        .span("平安交易通") \
        .span("?")
```

#### 4. 产品敞口计算和平盘  
```
    dfd.create_system_request("平安交易通","平盘").span("平盘系统")
```

### 对公外汇业务  
#### 简介  
#### 场景  
#### 1.行情  
#### 2.交易  
#### 3.清算和持仓  

### 对公利率业务  
#### 简介  
#### 简介  
#### 场景  
#### 1.行情  
```
    dfd.create_system_request("市场数据服务平台","数据") \
        .span("前置机") \
        .span("同业利率和汇率接入")
    #TBC
```
#### 2.交易  
#### 3.清算和持仓  

