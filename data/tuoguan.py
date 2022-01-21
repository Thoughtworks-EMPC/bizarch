from app.dfd import DFD
from app.ddd import DDD
from app.model import System, Operation, Function, Request


def biz():
    dfd = DFD("托管服务")

   # 1.签约 客户经理申请合作基金产品签约，经资产托管部审批后创建客户和产品账户信息
    span = dfd.create_request("客户经理", "托管服务")\
        .span("资产托管综合E管理子系统") \
        .span("BECIF", external=True) \
        .span("OA", external=True) \
        .span("资产托管智慧运营子系统")
    span.span("托管网银子系统")

    # 2.交易指令
    # dfd = DFD("交易指令").plus(dfd)
    dfd.create_request("管理人", "交易指令").span("托管网银子系统")

    # 2.资金清算
    dfd = DFD("资金清算").plus(dfd)
    dfd.create_system_request("资产托管智慧运营子系统", "资金清算").span("证券资金清算子系统（上海）")
    dfd.create_system_request("资产托管智慧运营子系统", "资金清算").span("证券资金清算子系统（深圳）")

    # 3.会计核算与估值
    dfd = DFD("估值核算").plus(dfd)
    span = dfd.create_request("管理人", "估值管理") \
        .span("资产托管智慧运营子系统").span("托管网银子系统")
    span.span("交易所", external=True)
    span.span("CFETS", external=True)
    span.span("EWS系统/邮件", external=True)
    span.span("深证通", external=True)

    dfd = DFD("资金清算").plus(dfd)
    dfd.create_request("管理人", "资金清算") \
        .span("资产托管智慧运营子系统")

    # 4.交易监督
    dfd = DFD("交易监督").plus(dfd)
    dfd.create_request("客户经理", "交易监督") \
        .span("资产托管智慧运营子系统")

    # 信息披露

    # 5.资讯服务 TBC
    dfd = DFD("资讯服务").plus(dfd)
    dfd.create_request("客户经理?", "资讯服务") \
        .span("智能数据管理平台")

    ############################################
    # 证券资金清算
    dfd = DFD("证券资金清算代理").plus(dfd)
    dfd.description = "面向证券公司总部及其营业机构，证券公司法人证券资金清算，通过设立单一总账户为基础实现资金的全面管理，通过此账户即可实现上海证券交易所和深圳证券交易所的证券资金快速收付"
    # 中登收款
    span = dfd.create_request("管理人", "中登收款").span("托管网银子系统")
    span.span("D+", "资金划转", external=True)
    span.span("证券资金清算子系统（上海）", "传递收款信息") \
        .span("PROP（前置机）", "传递收款信息", external=True) \
        .span("上中登", "收拉收款信息", external=True)
    span.span("证券资金清算子系统（深圳）", "传递收款信息") \
        .span("DCOM（前置机）", "传递收款信息", external=True) \
        .span("深中登", "收拉收款信息", external=True)

    # 上中登付款
    span1 = dfd.create_request("上中登", "头寸调拨-上中登") \
        .span("PROP（前置机）", "传递付款信息", external=True) \
        .span("证券资金清算子系统（上海）", "接收付款信息")

    span1.span("D+", "行内转账", external=True)
    span1.span("支付系统", "行外转账", external=True)

    # 深中登付款
    span2 = dfd.create_request("深中登", "头寸调拨-深中登") \
        .span("DCOM（前置机）", "传递付款信息", external=True) \
        .span("证券资金清算子系统（深圳）", "接收付款信息")

    span2.span("D+", "行内转账", external=True)
    span2.span("支付系统", "行外转账", external=True)

    dfd = DFD("基金服务").plus(dfd)
    dfd.create_request("客户经理", "签约估值").span("托管运营估值核算子系统", "开户")
    dfd.create_request("客户经理", "签约TA").span("托管运营TA", "开户")
    dfd.create_request("管理人", "份额管理").span(
        "管理人服务平台").span("托管运营TA")  # todo: TBC 管理人服务平台

    span = dfd.create_request("管理人", "估值管理").span(
        "管理人服务平台").span("托管运营估值核算子系统")
    span.span("深中登", external=True)
    span.span("上中登", external=True)
    dfd.create_request("销售机构", "募集赎回").span(
        "托管运营TA", "资金管理").span("托管运营资金清算子系统")
    dfd.create_request("投资者", "份额管理").span("管理人服务平台")
    dfd.create_request("投资者", "估值管理").span("管理人服务平台")

    # 资讯服务
    dfd = DFD("资讯服务").plus(dfd)
    dfd.create_request("客户经理", "获取资讯信息").span("智能数据管理平台")

    # 资金托管
    return dfd


def wiki():
    dfd = DFD("托管")

    sys = ["托管网银子系统", "资产托管智慧运营子系统", "资产托管非标业务子系统", "资产托管综合E管理子系统", "数据管理平台"]
    for i in sys:
        system = System.find_or_create(i)
        system.sys_type = "System"
    sys = ["行E通理财", "托管微信", "三方存管", "TIMP", "D+", "信息交换中心", "ODS", "邮件"]
    for i in sys:
        system = System.find_or_create(i)
        system.sys_type = "Corp"
    sys = ["电子传真", "深证通MR", "上清所", "外汇中心CFETS", "银企直连",
           "登记公司PROD/DCOM/CCNET", "交易所", "深证通文件网关", "资讯系统 ", "基金外包服务系统群"]
    for i in sys:
        system = System.find_or_create(i)
        system.sys_type = "External"

    return dfd

# 前期设计，以托管产品为核心


def ddd_bak():
    ddd = DDD("tuoguan")
    ddd.add_sub("报价", "市场")
    ddd.add_sub("投资产品账户", "份额")

    ddd.connect("TA清算户", "托管产品")
    ddd.connect("募集资金账户", "托管产品")
    ddd.connect("投资产品账户", "托管产品")
    ddd.connect("交易指令", "托管产品")

    ddd.connect("托管产品", "基金服务合约")
    ddd.connect("托管产品", "托管合约")
    ddd.connect("托管产品", "资金清算")
    ddd.connect("托管产品", "估值报告")
    ddd.connect("托管产品", "公告")
    ddd.connect("托管产品", "投资者份额")
    ddd.connect("托管产品", "托管资金帐户")

    ddd.connect("投资者", "投资者份额")

    ddd.connect("报价", "估值报告")

    ddd.connect("客户", "托管合约")

    ddd.connect("估值报告", "监督报告")
    ddd.connect("托管合约", "监督报告")

    return ddd


def ddd1():
    ddd = DDD("tuoguan")

    # ddd.add_sub("托管产品", "托管合约")
    # ddd.add_sub("托管产品", "基金服务")

    ddd.connect("托管产品", "投资者份额")
    ddd.connect("投资者份额", "投资者")

    ddd.connect("托管产品", "募集资金账户")
    ddd.connect("托管产品", "TA清算户")
    ddd.connect("客户", "托管产品")
    ddd.connect("托管产品", "托管资金帐户")

    ddd.connect("托管资金帐户", "交易指令")
    ddd.connect("投资产品账户", "交易指令")
    # ddd.add_sub("市场价", "市场")
    ddd.connect("托管资金帐户", "估值报告")
    ddd.connect("投资产品账户", "估值报告")
    ddd.connect("市场价", "估值报告")

    ddd.connect("估值报告", "监督报告")
    ddd.connect("托管产品", "投资产品账户")
    # ddd.connect("托管产品" , "交易指令")
    ddd.connect("对账单", "交易指令")

    ddd.connect("投资者", "募集资金账户")
    return ddd


def ddd():
    ddd = DDD("tuoguan")

    ddd.connect("产品立项", "托管产品")
    ddd.add_sub("产品立项", "托管户")

    ddd.connect("托管产品", "交易指令")
    ddd.add_sub("交易指令", "划款指令")
    ddd.add_sub("交易指令", "清核指令")

    ddd.connect("托管产品", "待办事项")
    ddd.connect("托管产品", "投资监督结果")

    ddd.connect("交易指令", "核算凭证")
    ddd.add_sub("核算凭证", "核算数据")

    ddd.connect("核算凭证", "估值表")
    ddd.connect("核算凭证", "余额表")

    ddd.connect("估值表", "投资监督结果")
    ddd.connect("估值表", "对账报告")
    ddd.connect("估值表", "实例文件")

    ddd.connect("余额表", "对账报告")

    # Event
    ddd.bind_events("产品立项", ["产品立项已录入", "产品立项已审批", "产品立项已删除", "产品立项已修改"])
    ddd.bind_events("托管产品", ["托管产品已创建", "托管产品已修改", "托管产品运营权限已分配", "托管产品已上线", "托管产品已作废", "托管产品其它信息已录入", "托管产品已封账",
                             "托管户已录入", "托管户已修改", "托管户已审批", "托管户已销户"])
    ddd.bind_events(
        "待办事项", ["投资监督待办事项已生成", "估值待办事项已生成", "网银待办事项已生成", "托管产品封账待办事项"])
    ddd.bind_events("交易指令", ["交易指令已接收", "交易指令已审批", "划款指令已发送", "清核指令已发送"])
    ddd.bind_events("核算凭证", ["核算数据已生成", "核算凭证已生成", "行情数据已接收"])
    ddd.bind_event("估值表", "估值表已生成")
    ddd.bind_event("余额表", "余额表已生成")
    ddd.bind_event("对账报告", "对账报告已生成")

    ddd.bind_events("划款指令", ["托管费划款指令已生成", "划款指令已发送"])
    ddd.bind_event("投资监督结果", "投资监督结果已生成")
    ddd.bind_events("实例文件", ["信息披露文件已接收", "信息披露文件已核对", "信息披露文件已反馈"])

    return ddd
