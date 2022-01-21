from app.dfd import DFD
from app.ddd import DDD


def biz():
    ######################################################################
    # 黄金自营
    # 询价，定价，期权，即远掉： 金交所会服系统
    ######################################################################
    dfd = DFD("黄金自营")
    dfd.create_request("交易员", "开仓").span("黄金自营子系统").span("MUREX", "日间推送")
    dfd.create_request("交易员", "平仓").span("黄金自营子系统").span("MUREX", "日间推送")

    dfd.create_request("交易员", "现货买入").span("黄金自营子系统").span("MUREX", "日间推送")
    dfd.create_request("交易员", "现货卖出").span("黄金自营子系统").span("MUREX", "日间推送")

    dfd.create_request("交易员", "询价，定价，期权，即远掉").span(
        "金交所会服系统").span("黄金自营子系统", "日终推送").span("MUREX")

    dfd.create_request("交易员", "期货").span(
        "上期所").span("黄金自营子系统", "日终推送").span("MUREX")

    dfd.create_request("交易员", "询价").span("MUREX")

    # dfd.create_request("交易员", "买入申请").span("黄金自营子系统", "申请买入")
    # dfd.create_request("交易员", "卖出申请").span("黄金自营子系统", "申请卖出")
    # dfd.create_request("交易员", "交易查看").span("黄金自营子系统", "查看交易")
    # dfd.create_request("交易员", "持仓查看").span("黄金自营子系统", "查看持仓")

    # dfd.create_request("分行经理", "交易审批").span("黄金自营子系统", "审批交易")
    dfd.create_system_request("黄金自营子系统", "保证金归集").span(
        "黄金清算子系统").span("金交所", "保证金归集", external=True)

    # 做市团队
    span = dfd.create_system_request("黄金量化交易子系统", "黄金量化交易").span("黄金自营子系统")

    # span.span("上期所", "贵金属期货",external=True)
    span.span("金交所", "贵金属交易", external=True)

    # dfd = DFD("黄金期权").plus(dfd)
    # dfd.create_request("个人客户", "查看黄金期权").span(
    #     "口袋银行").span("黄金账户子系统").span("黄金二级交易子系统")
    # dfd.create_request("个人客户", "查看黄金期权").span(
    #     "壹钱包").span("黄金账户子系统").span("黄金二级交易子系统")
    # dfd.create_request("个人客户", "查看黄金期权").span(
    #     "陆金所").span("黄金账户子系统").span("黄金二级交易子系统")
    # dfd.create_request("个人客户", "购买黄金期权").span("口袋银行").span(
    #     "黄金账户子系统").span("黄金二级交易子系统").span("黄金清算子系统")
    # dfd.create_request("个人客户", "购买黄金期权").span("壹钱包").span(
    #     "黄金账户子系统").span("黄金二级交易子系统").span("黄金清算子系统")
    # dfd.create_request("个人客户", "购买黄金期权").span("陆金所").span(
    #     "黄金账户子系统").span("黄金二级交易子系统").span("黄金清算子系统")

    # dfd.create_request("企业客户", "查看黄金期权").span(
    #     "陆金所", external=True).span("黄金账户子系统").span("黄金二级交易子系统")
    # dfd.create_request("企业客户", "购买黄金期权").span("陆金所", external=True).span(
    #     "黄金账户子系统").span("黄金二级交易子系统").span("黄金清算子系统")

    ######################################################################
    # 黄金账户
    ######################################################################
    dfd = DFD("黄金账户").plus(dfd)
    dfd.create_request("个人客户", "黄金份额认购") .span("口袋银行").span(
        "黄金账户子系统").span("D+")

    dfd.create_request("个人客户", "黄金份额赎回") .span("口袋银行").span(
        "黄金账户子系统").span("D+")

    dfd.create_request("个人客户", "黄金份额定投签约") .span("口袋银行").span("黄金账户子系统")
    dfd.create_request("个人客户", "黄金份额定投交易") .span("黄金账户子系统")

    dfd.create_system_request("黄金二级交易子系统", "平仓").span("D+")

    # todo: move to business 金生金
    dfd.create_request("个人客户", "黄金定存") .span("黄金账户子系统")
    # todo: TBC 黄金定存是不是金生金

    # 补充金生金业务
    # dfd = DFD("金生金").plus(dfd)
    # dfd.create_request("个人客户", "")
    # dfd.create_request("个人客户")

    ######################################################################
    # 黄金交易业务？？
    ######################################################################
    # dfd = DFD("贵金属线上交易").plus(dfd)
    # dfd.create_request("个人客户", "签约黄金定投").span(
    #     "口袋银行", "签约黄金定投", external=True).span("黄金账户子系统", "签约定投")
    # dfd.create_request("个人客户", "黄金定存").span(
    #     "口袋银行", "黄金定存", external=True).span("黄金账户子系统", "黄金定存")
    # todo: TBC
    # dfd.create_request("个人客户", "代理开户").span("贵金属线上交易子系统").span("黄金二级交易子系统")

    dfd = DFD("保价金条").plus(dfd)
    dfd.create_request("个人客户", "保价金条").span("贵金属线上交易子系统").span("实物金销售子系统")
    dfd = DFD("黄金回购").plus(dfd)
    dfd.create_request("个人客户", "黄金回购").span("贵金属线上交易子系统").span("实物金销售子系统")

    ######################################################################
    # 黄金租赁
    ######################################################################
    dfd = DFD("黄金租赁").plus(dfd)
    dfd.create_request("客户经理", "黄金租赁签约申请") .span("贵金属管理门户").span(
        "黄金租赁子系统").span("CMS", "确认授信", external=True)
    dfd.create_request("黄金租赁产品", "黄金租赁份额划拨") .span(
        "贵金属管理门户").span("黄金租赁子系统").span("黄金账户子系统")
    # .span("D+") \ #清算TBC/ with murex

    dfd.create_system_request("黄金租赁子系统", "租赁费").span("D+")
    dfd.create_system_request("黄金租赁子系统", "估算保证金").span("MUREX")

    # dfd.create_system_request("黄金租赁子系统", "融黄金租赁到期")
    dfd.create_system_request("黄金租赁子系统", "融现金租赁到期").span("黄金账户子系统")

    # todo: .span("D+") \ #清算TBC/ with murex
    # dfd.create_request("客户经理", "租赁清算").span("黄金租赁子系统")

    # dfd.create_request("客户经理", "贵金属账号创建").span(
    #     "贵金属管理门户").span("黄金租赁子系统", "账号创建")
    # dfd.create_request("客户经理", "黄金租赁合约登记").span("贵金属管理门户").span(
    #     "黄金租赁子系统", "登记合约").span("CMS", "确认授信", external=True)
    # dfd.create_request("分行经理", "黄金租赁合约审批").span(
    #     "贵金属管理门户").span("黄金租赁子系统", "审批合约")
    # dfd.create_request("集中作业部", "黄金租赁合约份额划拨确认").span(
    #     "贵金属管理门户").span("黄金租赁子系统", "合约份额划拨确认")
    # dfd.create_system_request("黄金租赁子系统", "黄金租赁保证金计算").span(
    #     "CMS", "确认授信", external=True)
    # dfd.create_system_request("黄金租赁子系统", "黄金租赁追加保证金").span("邮件", "追加保证金",external=True)
    # dfd.create_system_request("黄金租赁子系统", "租金划拨").span("核心账务", "划拨租金",external=True)
    # dfd.create_request("客户经理", "黄金租赁归还登记").span(
    #     "贵金属管理门户").span("黄金租赁子系统", "登记归还")
    # dfd.create_request("分行经理", "黄金租赁归还审批").span(
    #     "贵金属管理门户").span("黄金租赁子系统", "审批归还")
    # dfd.create_request("集中作业部", "黄金租赁合约归还确认").span(
    #     "贵金属管理门户").span("黄金租赁子系统", "合约归还确认")
    # dfd.create_system_request("黄金租赁子系统", "对公客户租借").span("黄金账户子系统")

    ######################################################################
    # 实物金
    ######################################################################
    dfd = DFD("实物金").plus(dfd)
    dfd.create_request("个人客户", "实物金购买").span("口袋银行").span(
        "实物金销售子系统").span("黄金二级交易子系统", "日终清算")  # todo: .span("D+") \ #TBC
    # TODO: 黄金二级在贵金属当中为报价入口,交易时间为上金所，非交易时间从报价引擎（伦敦金）过来
    dfd.create_request("个人客户", "询价").span("口袋银行", "黄金报价", external=True).span(
        "实物金销售子系统", "实物金报价").span("黄金二级交易子系统", "黄金实时报价")

    dfd.create_request("柜台柜员", "柜员AB端").span("实物金销售子系统")

    dfd.create_request("柜台柜员", "提领", read_only=False).span(
        "AB端", "黄金提领", external=True).span("实物金销售子系统", "实物金提取")
    dfd.create_request("柜台柜员", "退货", read_only=False).span(
        "AB端", "黄金退货", external=True).span("实物金销售子系统", "实物金反向订")

    dfd.create_request("客户经理", "订单导入", read_only=False).span(
        "贵金属管理门户", "实物金订单").span("实物金销售子系统", "实物金订单 - 日终")

    dfd.create_request("实物金供应商", "订单审核").span("企业网银").span("实物金销售子系统")

    # TODO 订单导入后，从客户的账户当中直接扣款，日终生成，供应商审核
    # 与供应商的结算为月结： 总行产品经理发起供应商月结 - > 集中作业部（审批，划款） -> 供应商

    # todo: TBC
    # dfd.create_request("贵金属采购经理", "采购",read_only = False).span("实物金销售子系统", "实物金采购")
    # dfd.create_request("贵金属采购经理", "入库",read_only = False).span("实物金销售子系统", "实物金入库")
    ######################################################################
    # 金交所交易
    ######################################################################
    dfd = DFD("金交所代理").plus(dfd)
    dfd.create_request("柜员", "企业用户二级开户").span("AB端").span(
        "黄金二级交易子系统").span("金交所")  # todo: TBC 保证金

    dfd.create_request("个人客户", "黄金二级开户").span("贵金属线上交易子系统").span(
        "黄金二级交易子系统", "开户").span("金交所")  # todo: .span("D+") \ #TBC 保证金
    dfd.create_request("个人客户", "黄金二级开户").span("易金通", external=True).span(
        "黄金二级交易子系统", "开户").span("金交所")  # todo: .span("D+") \ #TBC 保证金

    dfd.create_request("企业客户", "黄金二级交易行情").span(
        "贵金属智能代客交易子系统").span("黄金二级交易子系统")

    dfd.create_request("企业客户", "黄金二级交易").span(
        "聚金宝").span("黄金二级交易子系统").span("金交所")
    dfd.create_request("个人客户", "黄金二级交易").span(
        "易金通").span("黄金二级交易子系统").span("金交所")
    dfd.create_request("个人客户", "黄金二级交易").span(
        "聚金宝").span("黄金二级交易子系统").span("金交所")

    dfd.create_request("交易所", "企业出金").span("黄金清算子系统").span("金交所")
    dfd.create_request("柜员", "企业出入金").span("AB端").span("黄金清算子系统").span("金交所")
    dfd.create_request("企业客户", "企业出入金").span("聚金宝").span(
        "黄金二级交易子系统").span("黄金清算子系统").span("金交所")

    ######################################################################
    # 期货
    ######################################################################
    dfd = DFD("贵金属套期保值").plus(dfd)
    dfd.create_request("客户经理", "代客贵金属询价").span("贵金属管理门户").span(
        "代客贵金属交易子系统", "合约询价").span("金交所", "询价", external=True)
    # dfd.create_request("客户经理", "代客贵金属现货交易").span(
    #     "贵金属管理门户").span("代客贵金属交易子系统").span("黄金账户子系统")
    dfd.create_request("客户经理", "代客贵金属延期交易").span(
        "代客贵金属交易子系统").span("CMS", "确认授信", external=True)

    ######################################################################
    # 贵金属代客交易
    ######################################################################
    dfd = DFD("贵金属代客交易").plus(dfd)
    dfd.create_request("对公客户", "智能代客行情").span(
        "贵金属智能代客交易子系统").span("金交所", external=True)
    dfd.create_request("对公客户", "智能代客买入卖出").span("贵金属智能代客交易子系统", "交易").span(
        "黄金二级交易子系统", "交易").span("金交所", "交易", external=True)

    # dfd.create_request("个人客户", "黄金二级行情").span("口袋银行", "黄金二级行情",external=True).span("黄金二级", "行情").span("金交所", "行情", external=True)
    # dfd.create_request("个人客户", "黄金二级交易").span("口袋银行", "黄金二级交易",external=True).span("黄金二级", "交易").span("金交所", "行情", external=True)
    dfd.create_system_request("贵金属智能代客交易子系统", "同步代客上金所账号").span(
        "黄金二级交易子系统", "同步账号").span("金交所", "同步账号", external=True)

    ######################################################################
    # 理财及贵金属清算&核算
    ######################################################################
    dfd = DFD("理财及贵金属清算&核算").plus(dfd)
    # dfd.create_request("理财及贵金属业务组", "个人清算&核算").span(
    #     "贵金属智能代客交易子系统").span("黄金二级交易子系统")
    # dfd.create_request("理财及贵金属业务组", "企业清算&核算").span(
    #     "贵金属智能代客交易子系统").span("黄金二级交易子系统")

    dfd = DFD("衍生品交易").plus(dfd)
    # dfd.create_request("交易团队", "获取")
    return dfd


def ddd_bak():
    ddd = DDD("guijinshu")
    ddd.connect("交易员", "报盘")
    ddd.connect("市场数据", "报盘")
    ddd.connect("产品", "报盘")

    ddd.connect("报盘", "对帐单")

    ddd.connect("对帐单", "自营资金账户")

    ddd.add_sub("报价", "市场")
    ddd.connect("产品", "报价")

    ddd.connect("客户", "资金账户")
    ddd.connect("客户", "保证金账户")
    ddd.connect("客户", "产品账户")
    ddd.connect("产品", "委托单")
    ddd.connect("客户", "委托单")
    # ddd.connect("报价", "委托单")

    ddd.connect("产品", "实物金订单")
    ddd.connect("客户", "实物金订单")
    # ddd.connect("报价", "实物金订单")
    ddd.connect("实物金订单", "提取单")

    # ddd.connect("客户", "实物金订单")
    # ddd.connect("客户", "清算单")

    ddd.connect("产品", "租赁合约")
    ddd.connect("客户", "租赁合约")

    ddd.connect("仓储", "提取单")

    ddd.connect("产品", "采购单")
    ddd.connect("供应商", "采购单")
    # ddd.connect("采购单", "仓储")

    ddd.connect("授信额度", "租赁合约")

    # ddd.connect("清算单", "销售单")

    return ddd


def ddd():
    return ddd_to_be()


def ddd_as_is():
    ddd = DDD("guijinshu")

    # # 黄金账号 & 金交所代理
    # ddd.connect("产品", "委托流水")
    # ddd.connect("产品", "黄金帐户行情")
    # ddd.connect("黄金账户客户", "委托流水")
    # # ddd.connect("黄金帐户行情", "委托流水")

    # ddd.connect("定投计划", "委托流水")
    # ddd.connect("定投计划", "黄金账户客户")
    # ddd.connect("定投计划", "产品")

    # ddd.add_sub("委托流水", "成交回报")

    # ddd.add_sub("黄金帐户行情", "市场价")
    # ddd.add_sub("黄金帐户行情", "销售价")

    # ddd.connect("金交所代理客户", "金交所代理资金台账")
    # ddd.connect("金交所代理客户", "金交所代理库存台账")
    # ddd.connect("金交所代理客户", "金交所代理持仓台账")
    # ddd.connect("黄金账户客户", "黄金账户黄金份额")
    # ddd.connect("黄金账户客户", "黄金账户资金台账")

    # ddd.connect("金交所代理客户", "开仓单")
    # ddd.connect("金交所代理客户", "平仓单")

    # ddd.connect("开仓单", "代理交易品种")
    # ddd.connect("平仓单", "代理交易品种")

    # ddd.connect("代理交易品种", "代理行情")

    # ddd.connect("清算文件", "金交所代理资金台账")
    # ddd.connect("清算文件", "金交所代理库存台账")
    # ddd.connect("清算文件", "金交所代理持仓台账")

    # ddd.add_sub("计息引擎", "利息")

    # ddd.connect("计息引擎", "黄金账户资金台账")
    # ddd.connect("计息引擎", "黄金账户黄金份额")

    # ddd.connect("黄金账户资金台账", "计息引擎")
    # ddd.connect("黄金账户黄金份额", "计息引擎")

    # ddd.bind_events("黄金账户客户", ["客户已签约", "客户已销户", "黄金交易编码已设置"])
    # ddd.bind_events("黄金账户黄金份额", ["黄金份额已创建", "黄金份额已分配", "黄金份额已冻结"])
    # ddd.bind_events("黄金帐户行情", ["市场已更新", "销售价已更新"])
    # ddd.bind_events("委托流水", ["委托流水已生成", "开仓单已生成", "平仓单已生成", "成交回报已接收"])
    # ddd.bind_events("计息引擎", ["计息引擎已设置", "利息已分配"])

    # ddd.bind_events("产品", ["产品已创建", "产品已成立", "产品已到期", "资金已募集"])
    # ddd.bind_events("黄金账户资金台账", ["资金已分配"])

    # ddd.bind_events("黄金账户资金台账", ["资金台账已生成", "资金台账已更新",
    #                          "资金台账已入金", "资金台账已冻结", "资金台账已解冻", "资金台账已出金"])
    # ddd.bind_events("金交所代理持仓台账", ["持仓台账已生成", "持仓台账已更新"])
    # ddd.bind_events("金交所代理库存台账", ["库存台账已生成", "库存台账已更新"])

    # ddd.bind_events("清算文件", ["清算文件已接收"])
    # ddd.bind_events("定投计划", ["定制计划已设置"])

    # # 黄金自营 & 黄金贷款
    # ddd.connect("用户", "持仓库存")
    # ddd.connect("结算文件", "持仓库存")
    # ddd.connect("委托单", "持仓库存")
    # ddd.connect("委托单", "保证金")

    # ddd.connect("交易品种", "黄金自营行情")
    # ddd.connect("交易品种", "交易策略")

    # ddd.connect("交易策略", "委托单")
    # ddd.connect("交易品种", "委托单")

    # ddd.add_sub("委托单", "成交单")

    # ddd.connect("放款流水", "租赁申请单")
    # ddd.connect("租赁申请单", "租赁归还单")
    # ddd.connect("租赁申请单", "租赁费")
    # ddd.connect("租赁归还单", "租赁费")

    # # 黄金自营
    # ddd.bind_events("保证金", ["保证金入金指令已发送", "保证金出金指令已发送"])
    # ddd.bind_events("委托单", ["委托单已生成", "委托单已发送", "委托单已撤销", "委托单已更新", "成交单已生成"])
    # ddd.bind_events("持仓库存",["持仓库存已更新"])
    # ddd.bind_events("结算文件", ["结算文件已接收"])
    # ddd.bind_events("用户", ["用户已维护"])

    # # 黄金租赁
    # ddd.bind_events("放款流水", ["放款流水已接收"])
    # ddd.bind_events("租赁申请单", ["租赁申请单已提交", "租赁申请单已确认", "租赁申请单费用已更新", "租赁申请单流水号已补充", "租赁申请单已更新"])
    # ddd.bind_events("租赁归还单", ["租赁归还单已提交", "租赁归还单已确认", "租赁归还单已更新"])
    # ddd.bind_events("租赁费", ["租赁费已收取"])

    # #量化
    # ddd.bind_events("交易策略", ["交易策略已启动", "交易策略已停止"])

    # 黄金回购
    ddd.connect("黄金回购物流单", "回购单")
    ddd.connect("检测报告", "回购单")
    ddd.connect("精炼商", "检测报告")
    ddd.connect("回购单", "黄金回购支付流水")

    ddd.add_sub("精炼商", "清算户")

    # 保价金条
    ddd.add_sub("期权合约", "期权交易流水")

    ddd.connect("保价金条产品", "期权合约")
    ddd.connect("保价金条产品", "保价金认购单")

    ddd.add_sub("保价金认购单", "保证金账户")

    ddd.connect("保价金认购单", "实物金交易流水")

    # 代理开户
    ddd.connect("风险测评", "客户信息")
    ddd.connect("客户信息", "黄金二级户")

    # 实物金
    ddd.connect("产品", "仓库")
    ddd.connect("产品", "实物金交易流水")
    ddd.connect("客户", "实物金交易流水")

    ddd.add_sub("实物金交易流水", "发票")

    ddd.connect("实物金交易流水", "采购单")
    ddd.connect("供应商", "采购单")
    ddd.connect("供应商", "供应商支付流水")

    ddd.connect("采购单", "实物金物流单")

    return ddd


def ddd_to_be():
    ddd = DDD("guijinshu")

    # 黄金账号 & 金交所代理
    # ddd.connect("产品", "委托流水")
    ddd.connect("客户", "委托流水")
    # ddd.connect("行情", "委托流水")

    ddd.connect("客户", "定投计划")
    # ddd.connect("产品", "定投计划")
    # ddd.connect("定投计划", "委托流水")

    ddd.add_sub("委托流水", "开仓单")
    ddd.add_sub("委托流水", "平仓单")
    ddd.add_sub("委托流水", "成交单")

    ddd.connect("委托流水", "支付流水")

    ddd.add_sub("行情", "市场价")
    ddd.add_sub("行情", "销售价")

    ddd.connect("客户", "资金台账")
    ddd.connect("客户", "库存台账")
    ddd.connect("客户", "持仓台账")
    ddd.connect("客户", "黄金份额")

    # ddd.connect("清算文件", "资金台账")
    # ddd.connect("清算文件", "库存台账")
    # ddd.connect("清算文件", "持仓台账")
    # ddd.connect("清算文件", "黄金份额")

    # ddd.add_sub("计息引擎", "利息")

    # ddd.connect("计息引擎", "资金台账")
    # ddd.connect("计息引擎", "黄金份额")

    # ddd.connect("资金台账", "利息")
    # ddd.connect("黄金份额", "利息")

    ddd.bind_events("客户", ["客户已签约", "客户已销户", "黄金交易编码已设置"])
    ddd.bind_events("黄金份额", ["黄金份额已创建", "黄金份额已分配", "黄金份额已冻结"])
    ddd.bind_events("行情", ["市场已更新", "销售价已更新"])
    ddd.bind_events("委托流水", ["委托流水已生成", "开仓单已生成", "平仓单已生成", "成交回报已接收"])
    # ddd.bind_events("利息", ["计息规则已设置", "利息已分配"])

    ddd.bind_events("产品", ["产品已创建", "产品已成立", "产品已到期", "资金已募集"])
    ddd.bind_events("资金台账", ["资金已分配"])

    ddd.bind_events("资金台账", ["资金台账已生成", "资金台账已更新",
                             "资金台账已入金", "资金台账已冻结", "资金台账已解冻", "资金台账已出金"])
    ddd.bind_events("持仓台账", ["持仓台账已生成", "持仓台账已更新"])
    ddd.bind_events("库存台账", ["库存台账已生成", "库存台账已更新"])

    # ddd.bind_events("清算文件", ["清算文件已接收"])
    ddd.bind_events("定投计划", ["定制计划已设置"])

    # 黄金自营 & 黄金贷款
    ddd.connect("用户", "库存台账")
    # ddd.connect("委托流水", "保证金")

    # ddd.connect("产品", "行情")
    # ddd.connect("产品", "交易策略")

    ddd.connect("交易策略", "委托流水")
    # ddd.connect("产品", "委托流水")

    ddd.add_sub("委托流水", "成交单")

    ddd.connect("放款流水", "租赁申请单")
    ddd.connect("租赁申请单", "租赁归还单")
    ddd.connect("租赁申请单", "租赁费")
    ddd.connect("租赁归还单", "租赁费")

    # 黄金自营
    # ddd.bind_events("保证金", ["保证金入金指令已发送", "保证金出金指令已发送"])
    ddd.bind_events("委托流水", ["委托单已生成", "委托单已发送", "委托单已撤销", "委托单已更新", "成交单已生成"])
    # ddd.bind_events("持仓库存",["持仓库存已更新"])
    # ddd.bind_events("清算文件", ["结算文件已接收"])
    ddd.bind_events("用户", ["用户已维护"])

    # 黄金租赁
    ddd.bind_events("放款流水", ["放款流水已接收"])
    ddd.bind_events("租赁申请单", ["租赁申请单已提交", "租赁申请单已确认",
                              "租赁申请单费用已更新", "租赁申请单流水号已补充", "租赁申请单已更新"])
    ddd.bind_events("租赁归还单", ["租赁归还单已提交", "租赁归还单已确认", "租赁归还单已更新"])
    ddd.bind_events("租赁费", ["租赁费已收取"])

    # 量化
    ddd.bind_events("交易策略", ["交易策略已启动", "交易策略已停止"])

    # 黄金回购
    ddd.connect("物流单", "回购单")
    ddd.connect("检测报告", "回购单")
    ddd.connect("精炼商", "检测报告")
    ddd.connect("回购单", "支付流水")

    ddd.add_sub("精炼商", "清算户")

    ddd.bind_events("回购单", ["回购单已发起", "回购单金额已确认", "回购单客户已确认", "回购款已转账"])
    ddd.bind_events("物流单", ["物流单已提交", "物流详情已更新", ""])
    ddd.bind_events("检测报告", ["检测视频已上传", "检测报告已接收", "检测函已发送"])

    # 保价金条
    ddd.add_sub("期权合约", "期权交易流水")
    ddd.connect("客户", "保价金条认购单")

    ddd.connect("产品", "期权合约")
    ddd.connect("产品", "保价金条认购单")

    ddd.add_sub("保价金条认购单", "保证金账户")

    ddd.connect("保价金条认购单", "实物金交易流水")

    ddd.bind_events("产品", ["产品已添加", "产品已成立", "产品已到期"])
    ddd.bind_events("保价金条认购单", ["认购单已生成", "认购金额已冻结", "认购金额已解冻", "认购单已提取"])
    ddd.bind_events("保证金账户", ["保证金账户已入账", "保证金账户已扣款", "保证金账户已销户"])
    ddd.bind_events("实物金交易流水", ["实物金订单已生成"])

    # 代理开户
    ddd.connect("风险测评", "客户")
    ddd.connect("客户", "黄金二级户")

    ddd.bind_events("风险测评", ["风险测评已提交", "投资经验已提交",
                             "投资适合度已提交", "风险提示书已提交", "贵金属投资协议已提交"])
    ddd.bind_events("客户", ["客户信息已生成"])
    ddd.bind_events("黄金二级户", ["黄金二级户已开通", "黄金二级户已销户"])

    # 实物金
    # ddd.connect("产品", "仓库")
    ddd.connect("产品", "实物金交易流水")
    ddd.connect("客户", "实物金交易流水")

    ddd.add_sub("实物金交易流水", "发票")
    ddd.add_sub("仓库", "实物金交易流水")

    ddd.connect("实物金交易流水", "采购单")
    ddd.connect("供应商", "采购单")
    ddd.connect("供应商", "支付流水")
    ddd.connect("物流单", "采购单")

    ddd.bind_events("产品", ["产品已创建", "产品已上架"])
    ddd.bind_events("实物金交易流水", ["交易流水已生成"])
    ddd.bind_events("采购单", ["采购单已生成", "采购单已更新",
                            "采购订单已发货", "发票信息已接收", "发票邮件已发送"])
    ddd.bind_events("物流单", ["物流单已录入", "物流单商品已入仓库"])

    # 分Category（子域）
    ddd.category("行情子域", ["行情"])
    ddd.category("委托子域", ["委托流水", "交易策略"])
    ddd.category("支付子域", ["支付流水"])
    ddd.category("实物金销售子域", ["精炼商", "检测报告", "回购单", "物流单",
                             "供应商", "采购单", "实物金交易流水", "仓库", "产品", "期权合约", "保价金条认购单"])
    ddd.category("客户子域", ["风险测评", "黄金二级户", "定投计划", "客户",
                          "资金台账", "持仓台账", "黄金份额", "库存台账"])

    ddd.dependent("委托子域", "支付子域")
    ddd.dependent("委托子域", "行情子域")
    ddd.dependent("委托子域", "客户子域")
    ddd.dependent("实物金销售子域", "支付子域")
    ddd.dependent("实物金销售子域", "行情子域")
    ddd.dependent("实物金销售子域", "客户子域")

    return ddd