from app.dfd import DFD

def biz():
    dfd = DFD("敞口监控") # TBC目前只加到”总行派驻金融交易部暨资金运营中心风险团队“业务团队当中
    dfd.create_request("行外交易渠道","TRADEWEB").span("TRADEWEB",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","Bloomberg").span("Bloomberg",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","FXT").span("FXT",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","FX2017").span("FX2017",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","CFETS").span("CFETS",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","上交所").span("上交所",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","深交所").span("深交所",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","金交所").span("金交所",external=True).span("MUREX")
    dfd.create_request("行外交易渠道","期交所").span("期交所",external=True).span("MUREX")

    dfd.create_request("行内交易渠道","FBS").span("FBS",external=True).span("MUREX")
    dfd.create_request("行内交易渠道","国债系统").span("国债系统？").span("MUREX")
    dfd.create_request("行内交易渠道","交易通").span("平安交易通系统（香港）").span("MUREX")
    dfd.create_request("行内交易渠道","柜台债券").span("柜台债券子系统").span("MUREX")
    dfd.create_request("行内交易渠道","交易通").span("平安交易通系统").span("MUREX")
    dfd.create_request("行内交易渠道","黄金账户").span("黄金账户子系统").span("MUREX")
    dfd.create_request("行内交易渠道","代客贵金属").span("代客贵金属交易子系统").span("MUREX")
    dfd.create_request("行内交易渠道","纸黄金").span("贵金属线上交易子系统").span("MUREX")
    dfd.create_request("行内交易渠道","代客平盘").span("交易通自动平盘子系统").span("MUREX")
    dfd.create_request("行内交易渠道","黄金租赁").span("黄金自营子系统").span("MUREX")
    dfd.create_request("行内交易渠道","实物金").span("实物金销售子系统").span("MUREX")
    # dfd.create_request("行内交易渠道","黄金二级").span("黄金二级").span("MUREX")
    # dfd.create_request("行内交易渠道","资管投组").span("资管投组").span("MUREX")

    # dfd = DFD("行情数据").plus(dfd)
    dfd.create_system_request('WIND',"资金交易市场数据", external=True).span('MUREX')
    dfd.create_system_request('Reuters',"资金交易市场数据",  external=True).span('MUREX')
    dfd.create_system_request('Bloomberg',"资金交易市场数据", external=True).span('MUREX')
    dfd.create_system_request("做市交易及报价引擎", "资金交易市场数据").span('MUREX')
    dfd.create_system_request('JET', "资金交易市场数据").span('MUREX')
    dfd.create_system_request("中债估值", "资金交易市场数据").span('MUREX')
        

    # dfd = DFD("压力测试").plus(dfd)
    dfd = DFD("风险管控").plus(dfd)
    dfd.create_request("风险团队" , "风险管控").span("MUREX")
    
    dfd = DFD("额度调整").plus(dfd)
    dfd.create_system_request("MUREX", "额度调整").span("CMS")

    dfd = DFD("会计分录").plus(dfd)
    dfd.create_system_request("MUREX", "会计核算").span("D+")

    dfd = DFD("资金预报").plus(dfd)
    dfd.create_system_request("MUREX", "资金预报").span("FMS")

    dfd = DFD("资金清算核算").plus(dfd)
    dfd.create_request("集中作业部", "资金清算大额").span("MUREX").span("大额支付中心", external=True)
    dfd.create_request("集中作业部", "资金清算上清所").span("MUREX").span("上清所", external=True)
    dfd.create_request("集中作业部", "资金清算中债").span("MUREX").span("中债登", external=True)

    dfd = DFD("港行交易").plus(dfd)
    dfd.create_system_request("MUREX", "交易数据").span("NUMERIX")
    dfd.create_system_request("HK-TIMP", "HK-OPICS").span("HK-OPICS").span("MUREX")


    dfd = DFD("流动性").plus(dfd)
    span = dfd.create_request("资金交易团队交易员", "流动性控制").span("TIMP").span("MUREX")
    span.span("D+")
    span.span("大额支付")

    span = dfd.create_request("资金交易团队交易员", "HK流动性控制").span("HK-TIMP").span("MUREX")
    span.span("D+")
    span.span("大额支付")


    dfd = DFD("结构化产品").plus(dfd)
    dfd.create_request("产品经理" , "设计结构化产品").span("MUREX").span("TIMP")

    dfd = DFD("结构融资").plus(dfd)
    span = dfd.create_request("销售经理", "对外销售").span("MUREX")
    span.span("TIMP")
    span.span("HK-TIMP")

    dfd = DFD("固收自营").plus(dfd)
    span = dfd.create_request("固收团队", "固收").span("MUREX")

    dfd = DFD("衍生品做市").plus(dfd)
    span = dfd.create_request("衍生品做市交易员" , "衍生品做市").span("MUREX")

    dfd = DFD("固收做市").plus(dfd)
    span = dfd.create_request("固收做市团队" , "固收做市").span("MUREX")

    dfd = DFD("市场风险监督").plus(dfd)
    span = dfd.create_request("风险团队", "风险监督").span("MUREX")

    return dfd
