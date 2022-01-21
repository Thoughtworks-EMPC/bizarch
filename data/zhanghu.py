from app.dfd import DFD

def biz():
    dfd = DFD("资金产品账户")
    dfd.create_request("个人客户","账户贵金属签约开户").span("口袋银行",external=True).span("账户贵金属子系统")
    dfd.create_request("管理员","账户贵金属签约开户审核").span("账户贵金属子系统")

    dfd.create_request("个人客户","柜台债券开户").span("口袋银行").span("柜台债券子系统").span("中债登",external=True)
    dfd.create_request("企业客户","柜台债券开户").span("企业网银").span("柜台债券子系统").span("中债登",external=True)
    dfd.create_request("个人客户","交易通开户").span("口袋银行").span("平安交易通系统")
    dfd.create_request("企业客户","交易通开户").span("企业网银").span("平安交易通系统")

    dfd = DFD("贵金属账户").plus(dfd)
    dfd.create_request("个人客户","黄金账户开户").span("口袋银行",external=True).span("黄金账户子系统")
    dfd.create_request("个人客户", "二级开户") .span("贵金属线上交易子系统").span("黄金二级交易子系统").span("金交所",external=True)
    dfd.create_request("企业客户", "二级开户").span("黄金二级交易子系统").span("金交所",external=True)

    dfd = DFD("托管账户").plus(dfd)
    dfd.create_request("客户经理", "确认客户").span("BECIF", "确认客户", external=True)
    span = dfd.create_request("客户经理", "托管协议").span("行E通综合金融商城子系统", "提交申请").span("OA", "审批", external=True).span("资产托管智慧运营子系统" , "接收账户信息")
    dfd.create_request("客户经理","签约估值").span("托管运营估值核算子系统","开户")
    dfd.create_request("客户经理","签约TA").span("托管运营TA","开户")

    dfd = DFD("行E通账户").plus(dfd)
    dfd.create_request("客户","注册").span("行E通系统门户子系统").span("同业CRM子系统")
    dfd.create_request("客户经理","用户审批").span("同E家").span("同业CRM子系统")
    dfd.create_request("客户经理","账户开通").span("BECIF", external=True)

    return dfd