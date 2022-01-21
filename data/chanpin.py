from app.dfd import DFD
from app.ddd import DDD


def biz():
    dfd = DFD("外汇自营")
    dfd.create_request("交易员", "交易").span(
        "平盘系统").span("UBS", "交易", external=True)

    dfd = DFD("账户贵金属").plus(dfd)  # 伦敦金
    dfd.create_request("个人客户", "账户贵金属签约开户").span(
        "口袋银行", external=True).span("账户贵金属子系统")
    # 自动建保证金
    # dfd.create_request("管理员", "账户贵金属签约开户审核").span("账户贵金属子系统")
    dfd.create_request("管理员", "账户贵金属产品管理").span("账户贵金属子系统")
    dfd.create_request("个人客户", "账户贵金属市价查询").span(  # 市价查询
        "口袋银行", external=True).span("账户贵金属子系统").span("报价引擎")
    dfd.create_request("个人客户", "账户贵金属开平仓").span(
        "口袋银行", external=True).span("账户贵金属子系统").span("D+", "出入金")
    # 自动
    # dfd.create_request("个人客户", "账户贵金属保证金出入金").span(
    #     "口袋银行", external=True).span("账户贵金属子系统")

    dfd.create_system_request("账户贵金属子系统", "贵金属敞口").span("MUREX")
    dfd.create_system_request("账户贵金属子系统", "外汇敞口").span("MUREX")
    dfd.create_system_request("账户贵金属子系统", "平盘").span("DIMPLE", external=True)
    dfd.create_system_request("账户贵金属子系统", "数据归集").span("ODS", external=True)
    dfd.create_system_request("账户贵金属子系统", "追保").span("报价引擎").span("D+")
    dfd.create_system_request("账户贵金属子系统", "强制平仓").span("报价引擎")

    dfd = DFD("柜台债券").plus(dfd)
    span = dfd.create_request("个人客户", "口袋银行债券开户").span(
        "口袋银行", external=True).span("柜台债券子系统").span("中债登")
    span = dfd.create_request("个人客户", "交易通债券开户").span(
        "零售交易通APP", external=True).span("柜台债券子系统").span("中债登")
    span = dfd.create_request("柜员", "个人AB端债券开户").span(
        "AB端", external=True).span("柜台债券子系统").span("中债登")

    dfd.create_request("个人客户", "债券市价查询").span("口袋银行", external=True).span(
        "柜台债券子系统").span("JET")
    dfd.create_request("个人客户", "债券买入").span("口袋银行", external=True).span(
        "柜台债券子系统").span("IFMS", "风险等级").span("D+", "出金")
    dfd.create_request("个人客户", "债券卖出").span("口袋银行", external=True).span(
        "柜台债券子系统").span("D+", "入金")

    dfd.create_request("柜员", "AB端债券开户").span("AB端").span("柜台债券子系统").span("中债登")
    dfd.create_request("企业客户", "企业网银债券开户").span(
        "企业网银").span("柜台债券子系统").span("中债登")
    dfd.create_request("企业客户", "交易通债券开户").span(
        "企业交易通APP").span("柜台债券子系统").span("中债登")

    dfd.create_request("企业客户", "市价询价").span("企业网银", external=True).span(
        "柜台债券子系统").span("JET")
    dfd.create_request("企业客户", "债券买入").span("企业网银", external=True).span(
        "柜台债券子系统").span("D+", "出金")
    dfd.create_request("企业客户", "债券卖出").span("企业网银", external=True).span(
        "柜台债券子系统").span("D+", "入金")

    dfd.create_request("柜台柜员", "债券询价").span("AB端", external=True).span(
        "柜台债券子系统").span("JET", external=True)
    dfd.create_request("柜台柜员", "债券买入").span("AB端", external=True).span(
        "柜台债券子系统").span("IFMS", "风险等级").span("D+", external=True)
    dfd.create_request("柜台柜员", "债券卖出").span(
        "AB端", external=True).span("柜台债券子系统").span("D+", external=True)
    dfd.create_system_request("柜台债券子系统", "债券买入").span("MUREX", external=True)
    dfd.create_system_request("柜台债券子系统", "债券卖出").span("MUREX")
    dfd.create_system_request("柜台债券子系统", "交易记录").span("MUREX").span(
        "中债登").span("CFETS", "外汇交易备案")  # todo: TBC 就是需要备案，不知道为什么
    dfd.create_system_request("柜台债券子系统", "额度信息").span("MUREX")

    dfd.create_request("个人客户", "份额转让").span(
        "AB端", external=True).span("柜台债券子系统")
    dfd.create_request("企业客户", "份额转让").span(
        "AB端", external=True).span("柜台债券子系统")

    dfd = DFD("外汇代客交易").plus(dfd)
    # 个人外汇
    dfd.create_request("个人客户", "获取报价").span("零售交易通APP").span("平安交易通系统").span(
        "做市交易及报价引擎").span("前置机").span("UBS", "行情", external=True)
    dfd.create_request("个人客户", "交易通保证金出入金").span(
        "零售交易通APP").span("平安交易通系统").span("D+")
    dfd.create_request("个人客户", "开仓").span("零售交易通APP").span(
        "平安交易通系统").span("零售风险评测").span("MUREX")
    dfd.create_request("个人客户", "平仓").span(
        "零售交易通APP").span("平安交易通系统").span("MUREX")
    dfd.create_system_request("平安交易通系统", "强制平仓").span("做市交易及报价引擎")
    dfd.create_request("个人客户", "外汇持仓").span("零售交易通APP").span("平安交易通系统")
    dfd.create_system_request("平安交易通系统", "平盘").span("交易通自动平盘子系统")

    # 企业外汇
    dfd.create_request("企业客户", "获取报价").span("对公交易通APP").span("平安交易通系统").span(
        "做市交易及报价引擎").span("前置机").span("UBS", "行情", external=True)
    # dfd.create_request("企业客户", "交易通保证金出入金").span(
    #     "对公交易通APP").span("平安交易通系统").span("D+")
    dfd.create_request("企业客户", "开仓").span("对公交易通APP").span(
        "平安交易通系统").span("D+").span("MUREX")
    dfd.create_request("企业客户", "平仓").span(
        "对公交易通APP").span("平安交易通系统").span("MUREX")
    dfd.create_system_request("平安交易通系统", "追保报警").span("做市交易及报价引擎")
    # dfd.create_system_request("平安交易通系统", "强制平仓").span("做市交易及报价引擎")
    dfd.create_request("企业客户", "外汇持仓").span("对公交易通APP").span("平安交易通系统")
    dfd.create_system_request("平安交易通系统", "平盘").span("交易通自动平盘子系统")

    dfd = DFD("港行-外汇交易").plus(dfd)
    # 只有AB柜面，客户临柜，交易员处理
    dfd.create_request("个人客户", "获取报价").span("港行AB端").span("平安交易通系统（香港）").span(
        "做市交易及报价引擎").span("前置机").span("UBS", "行情", external=True)
    dfd.create_request("个人客户", "交易通保证金出入金").span(
        "港行AB端").span("平安交易通系统（香港）").span("D+")
    dfd.create_request("个人客户", "开仓").span("港行AB端").span(
        "平安交易通系统（香港）").span("零售风险评测").span("MUREX")
    dfd.create_request("个人客户", "平仓").span(
        "港行AB端").span("平安交易通系统（香港）").span("MUREX")
    dfd.create_system_request("平安交易通系统（香港）", "强制平仓").span("做市交易及报价引擎")
    dfd.create_request("个人客户", "外汇持仓").span("港行AB端").span("平安交易通系统（香港）")
    dfd.create_system_request("平安交易通系统", "平盘").span("交易通自动平盘子系统")

    # 企业外汇
    # 只有AB柜面，客户临柜，交易员处理
    dfd.create_request("企业客户", "获取报价").span("平安交易通系统（香港）").span(
        "做市交易及报价引擎").span("前置机").span("UBS", "行情", external=True)
    dfd.create_request("企业客户", "交易通保证金出入金").span("平安交易通系统（香港）").span("D+")
    dfd.create_request("企业客户", "开仓").span(
        "平安交易通系统（香港）").span("零售风险评测").span("MUREX")
    dfd.create_request("企业客户", "平仓").span("平安交易通系统（香港）").span("MUREX")
    dfd.create_system_request("平安交易通系统（香港）", "强制平仓").span("做市交易及报价引擎")
    dfd.create_request("企业客户", "外汇持仓").span("平安交易通系统（香港）")
    dfd.create_system_request("平安交易通系统（香港）", "平盘").span("交易通自动平盘子系统")

    # dfd = DFD("对公利率").plus(dfd)

    # dfd = DFD("利率交易").plus();

    dfd = DFD("外汇报价").plus(dfd)
    dfd.create_request("个人客户", "获取报价").span("零售交易通APP").span(
        "平安交易通系统").span("做市交易及报价引擎").span("前置机").span("同业利率和汇率接入")
    # 只有外汇报价？为何
    dfd.create_system_request("平安交易通系统", "平盘").span("平盘系统")
    span = dfd.create_system_request("市场数据服务平台", "数据").span("前置机")
    span.span("UBS", "行情", external=True)
    span.span("同业利率和汇率接入")

    dfd = DFD("报价平盘").plus(dfd)
    dfd.create_request("外汇交易团队交易员", "获取报价").span(
        "做市交易及报价引擎").span("前置机").span("同业利率和汇率接入")
    dfd.create_system_request("平安交易通系统", "平盘").span("平盘系统")

    return dfd

def ddd_bak():
    ddd = DDD("chanpin")
    ddd.connect("产品种类", "产品")

    ddd.connect("产品种类", "交易品种开通合同")
    ddd.connect("客户", "交易品种开通合同")
    ddd.connect("客户", "风评")

    # ddd.add_sub("委托单", "委托价")
    # ddd.add_sub("委托单", "成交价")
    ddd.connect("委托单", "风控")

    ddd.connect("产品", "委托单")
    ddd.connect("客户", "委托单")
    ddd.connect("保证金账户", "委托单")

    ddd.connect("委托单", "交割单")
    ddd.connect("交割单", "保证金账户")

    ddd.connect("交割单", "资金账户")
    ddd.connect("交割单", "产品账户")

    ddd.connect("产品", "每日份额")

    ddd.connect("客户", "保证金账户")
    ddd.connect("客户", "资金账户")
    ddd.connect("客户", "产品账户")

    ddd.add_sub("报价", "市场")
    ddd.connect("产品", "报价")
    ddd.connect("报价", "委托单")  # 确定报价可以成交？ 可能没有这一根线

    return ddd

def ddd():
    return ddd_to_be();

def ddd_as_is():
    ddd = DDD("chanpin")

    # 账户贵金属
    ddd.connect("产品", "账户贵金属行情")
    ddd.add_sub("账户贵金属行情", "行情任务")
    ddd.add_sub("账户贵金属行情", "优惠价")

    ddd.connect("产品", "持仓")
    ddd.connect("客户", "持仓")

    ddd.add_sub("客户", "风险等级")
    ddd.add_sub("客户", "纸黄金协议")
    ddd.add_sub("客户", "保证金账户")

    ddd.connect("委托单", "账户贵金属行情")
    ddd.connect("客户", "委托单")

    ddd.connect("委托单", "成交单")
    ddd.connect("成交单", "资金划转流水")
    ddd.connect("成交单", "敞口")

    # 柜台债
    ddd.connect("产品", "持仓")
    ddd.add_sub("持仓", "在途持仓")

    ddd.connect("客户", "持仓")
    ddd.add_sub("客户", "资金账户")
    ddd.add_sub("客户", "托管账户")
    ddd.add_sub("客户", "签约流水")

    ddd.connect("客户", "交易流水")
    ddd.connect("交易流水", "账务明细")
    ddd.connect("产品", "交易流水")
    ddd.connect("产品", "柜台债行情")

    return ddd


def ddd_to_be():
    ddd = DDD("chanpin")

    # 账户贵金属
    ddd.connect("产品", "行情")
    ddd.add_sub("行情", "行情任务")
    ddd.add_sub("行情", "优惠价")

    ddd.connect("产品", "持仓")
    ddd.connect("客户", "持仓")

    ddd.add_sub("客户", "风险等级")
    ddd.add_sub("客户", "纸黄金协议")
    ddd.add_sub("客户", "保证金账户")

    ddd.connect("委托单", "行情")
    ddd.connect("客户", "委托单")

    ddd.connect("委托单", "成交单")
    ddd.connect("成交单", "资金划转流水")
    ddd.connect("成交单", "敞口")

    # 柜台债
    ddd.connect("产品", "持仓")
    ddd.add_sub("持仓", "在途持仓")

    ddd.connect("客户", "持仓")
    ddd.add_sub("客户", "资金账户")
    ddd.add_sub("客户", "托管账户")
    ddd.add_sub("客户", "签约流水")

    ddd.connect("客户", "交易流水")
    ddd.connect("交易流水", "账务明细")
    ddd.connect("产品", "交易流水")

    ddd.connect("产品" , "行情")

    return ddd
