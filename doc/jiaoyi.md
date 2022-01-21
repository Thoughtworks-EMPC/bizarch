### 业务概览
#### 资产负债部  
    * 资金预报

#### 另类投资部  
    * 资产证券化
    * 非标产品投资
    * 票据业务
    * 资管计划

### 资金预报  
#### 简介  
资金管理室根据合规要求，根据当日交易的资金余额对备用金进行差额计算，对于产生的差额进行资金调拨，以满足监管要求

#### 场景  
#### 1. 资金预报  
```
    dfd.create_request("资金管理员","资金预报") \
        .span("FMS")  
```

### 另类投资  
#### 简介  
#### 场景  
#### 1. 另类投资  
```
    dfd.create_request("交易员","资产证券化交易") \
        .span("TIMP") \
        .span("MUREX")  

    dfd.create_request("交易员","非标产品投资") \
        .span("TIMP") \
        .span("MUREX")  

    dfd.create_request("交易员","资产证券化交易") \
        .span("TIMP") \
        .span("MUREX")  

    dfd.create_request("交易员","票据业务") \
        .span("TIMP") \
        .span("MUREX")  
```
