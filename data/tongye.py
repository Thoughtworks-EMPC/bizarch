from app.dfd import DFD
from app.ddd import DDD


def biz():
    dfd = DFD("同业客户引入")
    dfd.create_request("客户管理部", "同业用户录入").span("BECIF").span("同业CRM子系统")
    dfd.create_request("同业买方客户", "注册行E通用户").span(
        "行E通系统门户子系统").span("行E通产品子系统").span("ODS")
    dfd.create_request("客户管理部", "审核行E通用户").span("行E通产品子系统")

    dfd = DFD("同业产品引入").plus(dfd)
    dfd.create_request("产品经理", "债券同业产品引入").span("同业销售产品工厂")
    dfd.create_request("产品经理", "理财同业产品引入").span(
        "行E通产品子系统").span("统一TA", "产品同步")
    dfd.create_request("产品经理", "基金同业产品引入").span(
        "行E通产品子系统").span("行E通产品代销子系统", "产品同步")
    dfd.create_request("注册卖方", "同业产品引入申请").span("行E通系统门户子系统").span("行E通产品子系统")
    dfd.create_request("产品经理", "同业产品引入审批").span("行E通系统门户子系统").span("行E通产品子系统")
    dfd.create_request("产品经理", "同业产品上下架").span("行E通产品子系统")

    dfd = DFD("同业产品销售").plus(dfd)
    dfd.create_request("客户经理", "三方存管销售").span("第三方存管系统")
    dfd.create_request("客户经理", "同业非标产品销售").span("TIMP").span("MUREX")
    dfd.create_request("客户经理", "同业标准产品销售").span("第三方存管系统")  # ？
    dfd.create_request("客户经理", "三方存管销售").span("第三方存管系统").span("行E通核心子系统")
    dfd.create_request("客户经理", "银期存管").span("银期保证金存管子系统")
    dfd.create_request("客户经理", "银衍存管").span("银衍保证金存管应用")
    dfd.create_request("产品经理", "产品录入").span(
        "智慧同业统一门户子系统", "产品录入").span("同业销售产品工厂", "产品录入")
    dfd.create_request("同业买方客户", "查看资讯").span(
        "行E通系统门户子系统").span("行E通产品子系统").span("同业资讯平台", "产品资讯")
    dfd.create_request("同业买方客户", "查看产品").span(
        "行E通系统门户子系统").span("行E通产品子系统").span("同业销售产品工厂", "产品列表")
    dfd.create_request("客户经理", "录入报量和中标").span("智慧同业统一门户子系统").span("同业CRM子系统")
    dfd.create_request("同业买方客户", "WOW").span("行E通电子交易市场").span("JET")

    dfd = DFD("行E通代销").plus(dfd)
    # todo: TBC
    # dfd.create_request("客户经理","行E通代销").span("行E通系统门户子系统").span("行E通产品子系统")
    # dfd.create_request("客户经理","行E通代销").span("行E通系统门户子系统").span("行E通产品子系统")
    dfd.create_request("同业买方客户", "查看资讯").span("行E通系统门户子系统").span("同业资讯平台")
    dfd.create_request("同业买方客户", "基金购买").span("行E通系统门户子系统").span(
        "行E通产品子系统").span("行E通产品代销子系统").span("基金公司", external=True)

    dfd = DFD("同业销售线索").plus(dfd)
    span = dfd.create_request("客户经理", "创建任务").span(
        "智慧同业统一门户子系统").span("同业CRM子系统")
    span.span("同业销售产品工厂", "查询产品")
    dfd.create_request("客户经理", "创建工单").span("智慧同业统一门户子系统").span("同业CRM子系统")
    dfd.create_request("业务员", "更新工单").span("智慧同业统一门户子系统").span("同业CRM子系统")
    dfd.create_request("业务员", "客户信息").span(
        "智慧同业统一门户子系统", "查看客户").span("同业CRM子系统", "查看客户")
    dfd.create_system_request("同业CRM子系统", "客户交易").span("行E通产品子系统", "查询交易")
    dfd.create_system_request("同业CRM子系统", "客户营销").span(
        "推荐引擎", "产品推荐", external=True)

    # todo: TBC 交易员角色是否同时负责投资和融资
    dfd = DFD("同业产品投资").plus(dfd)
    dfd.create_request("交易员", "同业标准产品投资").span("TIMP").span("MUREX")
    dfd.create_request("投资经理", "同业非标产品投资").span("TIMP").span("MUREX")

    dfd = DFD("同业存放").plus(dfd)
    dfd.create_request("交易员", "同业存放").span("TIMP").span("MUREX")

    dfd = DFD("同业存款").plus(dfd)
    dfd.create_request("交易员", "同业存款产品管理").span("行E通产品子系统")
    dfd.create_request("行E通", "同业存款").span(
        "行E通系统门户子系统").span("行E通产品子系统").span("TIMP")
    dfd.create_request("交易员", "同业存款").span("TIMP").span("MUREX")
    dfd.create_request("投资经理", "同业非标产品投资").span("TIMP").span("MUREX")

    dfd = DFD("同业业务考核").plus(dfd)
    dfd.create_request("部门经理", "同业业务考核").span("PMS")

    dfd = DFD("同业项目合规").plus(dfd)
    dfd.create_request("客户经理", "同业项目合规").span("TIMP")

    # dfd = DFD("智慧同业")
    # dfd.create_request("客户经理","工单创建").span("智慧同业门户","创建工单").span("同业CRM","创建工单").span("同业销售产品工厂","查询产品")
    # dfd.create_request("客户经理","任务创建").span("智慧同业门户","创建任务").span("同业CRM","创建任务")
    # dfd.create_request("业务员","任务更新").span("智慧同业门户","更新任务").span("同业CRM","更新任务")
    # dfd.create_request("业务员","客户信息").span("智慧同业门户","查看客户").span("同业CRM","查看客户")
    # dfd.create_system_request("同业CRM","客户交易").span("行E通产品子系统","查询交易")
    # dfd.create_system_request("同业CRM","客户营销").span("推荐引擎","产品推荐",external=True)

    # dfd = DFD("电子交易").plus(dfd)
    # dfd.create_request("企业客户","查看行情").span("电子交易","查看行情")
    # dfd.create_request("企业客户","IRSBond交易").span("电子交易","IRSBond交易").span("JET","IRSBond交易",external=True)

    # dfd = DFD("行E通债券").plus(dfd)
    # dfd.create_request("产品经理","产品录入").span("智慧同业门户","产品录入").span("同业销售产品工厂","产品录入")
    # dfd.create_request("产品经理","产品上架申请").span("智慧同业门户","产品上架申请").span("同业销售产品工厂","产品上架")
    # dfd.create_request("产品经理","产品下架").span("智慧同业门户","产品下架").span("同业销售产品工厂","产品下架")
    # dfd.create_request("部门总","产品上架审批").span("智慧同业门户","产品上架审批").span("同业销售产品工厂","产品上架审批")
    # dfd.create_request("企业客户","查看资讯").span("行E通系统门户子系统","查询产品资讯").span("行E通产品子系统","产品资讯").span("同业资讯","产品资讯")
    # dfd.create_request("企业客户","查看产品").span("行E通系统门户子系统","查看产品").span("行E通产品子系统","产品列表").span("同业销售产品工厂","产品列表")
    # dfd.create_request("客户经理","录入报量").span("智慧同业门户","录入报量").span("同业CRM","录入报量")
    # dfd.create_request("客户经理","录入中标").span("智慧同业门户","录入中标").span("同业CRM","录入中标")

    # dfd = DFD("行E通同业存款").plus(dfd)
    # dfd.create_request("产品经理","同存上架申请").span("行E通系统门户子系统","同存上架申请").span("行E通产品子系统","同存上架")
    # dfd.create_request("产品经理","同存定价").span("行E通系统门户子系统","同存定价").span("行E通产品子系统","同存定价")
    # dfd.create_request("企业客户","产品浏览").span("行E通系统门户子系统","查看产品").span("行E通产品子系统","产品列表")
    # dfd.create_request("企业客户","同存发起").span("行E通系统门户子系统","发起同存").span("行E通产品子系统","发起同存")
    # dfd.create_request("客户经理","调息申请").span("行E通系统门户子系统","调息申请").span("行E通产品子系统","调息申请")
    # dfd.create_request("产品经理","同存审批").span("行E通系统门户子系统","审批同存").span("行E通产品子系统","审批同存").span("TIMP","创建同存")
    # dfd.create_request("企业客户","同存持仓查看").span("行E通系统门户子系统","查看持仓").span("行E通产品子系统","查看持仓")
    # dfd.create_request("企业客户","存款证打印").span("行E通系统门户子系统","打印存款证").span("行E通产品子系统","打印存款证")
    # dfd.create_request("企业客户","同存支取").span("行E通系统门户子系统","支取同存").span("行E通产品子系统","支取同存").span("TIMP","支取同存")

    # dfd = DFD("行E通理财").plus(dfd)
    # dfd.create_system_request("行E通产品子系统","理财产品导入").span("统一TA","产品同步")
    # dfd.create_system_request("行E通产品子系统","代销理财产品导入").span("行E通产品代销","产品同步").span("理财子","产品同步")
    #
    # dfd.create_request("产品经理","理财上架申请").span("行E通系统门户子系统","产品上架申请").span("行E通产品子系统","产品上架")
    # dfd.create_request("企业客户","查看理财").span("行E通系统门户子系统","查看产品").span("行E通产品子系统","产品列表")
    # dfd.create_request("企业客户","理财购买").span("行E通系统门户子系统","购买理财").span("行E通产品子系统","购买理财").span("统一TA","购买理财")
    # dfd.create_request("企业客户","理财赎回").span("行E通系统门户子系统","理财赎回").span("行E通产品子系统","赎回理财").span("统一TA","赎回理财")
    # dfd.create_system_request("行E通产品子系统","购买理财").span("行E通产品代销","购买理财").span("理财子","购买理财",external=True)
    # dfd.create_system_request("行E通产品子系统","赎回理财").span("行E通产品代销","赎回理财").span("理财子","赎回理财",external=True)
    # dfd.create_request("企业客户","理财持仓查看").span("行E通系统门户子系统","查看持仓").span("行E通产品子系统","查看持仓")

    # dfd = DFD("行E通基金").plus(dfd)
    # dfd.create_system_request("行E通产品子系统","基金产品导入").span("行E通产品代销","产品同步").span("基金公司","产品同步",external=True)
    # dfd.create_request("产品经理","基金产品上架申请").span("行E通系统门户子系统","产品上架申请").span("行E通产品子系统","产品上架")
    # dfd.create_request("企业客户","查看基金").span("行E通系统门户子系统","查看产品").span("行E通产品子系统","产品列表")
    # dfd.create_request("企业客户","基金购买").span("行E通系统门户子系统","购买基金").span("行E通产品子系统","购买基金").span("行E通产品代销","购买基金").span("基金公司","基金购买",external=True)
    # dfd.create_request("企业客户","基金赎回").span("行E通系统门户子系统","赎回基金").span("行E通产品子系统","赎回基金").span("行E通产品代销","赎回基金").span("基金公司","基金赎回",external=True)
    # dfd.create_request("企业客户","基金持仓查看").span("行E通系统门户子系统","查看持仓").span("行E通产品子系统","查看持仓")

    # dfd = DFD("三方存管").plus(dfd)
    # dfd.create_request("个人客户","个人客户银证转账").span("口袋银行","客户保证金转账",external=True).span("三方存管","券商保证金转账")
    # dfd.create_request("企业客户","企业客户银证转账").span("企业网银","客户保证金转账",external=True).span("三方存管","券商保证金转账")
    # dfd.create_request("券商","银证转账").span("三方存管","券商保证金转账").span("行E通核心","资金划转").span("他行","资金划转",external=True)

    # dfd = DFD("银期存管").plus(dfd)
    # dfd.create_request("企业客户","企业客户银期转账").span("企业网银","客户保证金转账",external=True).span("银期存管","期货客户保证金转账")
    # dfd.create_request("期货公司","期货客户银期转账").span("银期存管","期货客户保证金转账")
    # dfd.create_request("期货中心","期货公司银期转账").span("银期存管","期货公司保证金转账")
    #
    # dfd = DFD("银衍存管").plus(dfd)
    # dfd.create_request("券商","银衍转账").span("银衍存管","保证金转账")

    return dfd


def ddd_bak():
    ddd = DDD("tongye")
    # ddd.create_domain(["客户","资金账户","保证金账户","产品交易框架合同","业务员","任务","风评","产品代销合同","产品","资讯","价格","商品","产品代销合同","集中户","对账"])
    ddd.connect("客户", "工单")

    ddd.connect("客户", "资金账户")

    ddd.connect("销售团队", "工单")
    ddd.connect("产品", "工单")
    ddd.connect("产品", "资讯")
    ddd.connect("产品", "产品资金账户")
    ddd.connect("产品", "产品代销合同?")
    ddd.connect("产品", "代销合同?")

    ddd.add_sub("报价", "市场")

    ddd.connect("产品", "报价")
    # ddd.connect("产品","商品")
    # ddd.connect("价格","商品")

    ddd.connect("销售团队", "申购/赎回交易订单")
    ddd.connect("产品", "申购/赎回交易订单")
    ddd.connect("客户", "申购/赎回交易订单")

    ddd.connect("产品交易框架合同", "申购/赎回交易订单")
    # ddd.connect("产品交易框架合同", "赎回")

    ddd.connect("资金账户", "申购/赎回交易订单")
    # ddd.connect("资金账户", "赎回")

    ddd.connect("申购/赎回交易订单", "对账")
    ddd.connect("申购/赎回交易订单", "清算")
    ddd.connect("资金账户", "清算")
    ddd.connect("产品资金账户", "清算")
    # ddd.connect("赎回", "对账")

    ddd.add_sub("客户", "行E通用户")
    ddd.add_sub("客户", "风评")
    ddd.add_sub("任务", "工单")
    ddd.add_sub("产品", "产品描述文件")

    # ddd.add_sub("申购", "申购回执")
    # ddd.add_sub("赎回", "赎回回执")

    ddd.connect("个人保证金账户", "三方存管合同")
    ddd.connect("券商集中户", "三方存管合同")
    # ddd.connect("X行","三方存管合同")
    ddd.connect("三方存管合同", "三方存管指令")
    # ddd.connect("三方存管指令","")
    ddd.connect("投资产品", "投资交易")
    ddd.connect("交易员", "投资交易")
    ddd.connect("内部账户", "投资交易")

    return ddd


def ddd():
    ddd = DDD("tongye")

    # 客户 & 产品
    ddd.connect("客户", "客户账户")

    ddd.connect("风评", "客户")

    ddd.add_sub("客户账户", "产品户")
    ddd.add_sub("客户账户", "法人户")

    ddd.connect("客户账户", "客户份额")
    ddd.connect("交易单",  "客户份额")
    ddd.connect("产品", "客户份额")
    ddd.connect("产品", "交易单")

    # 
    ddd.add_sub("产品", "产品份额")

    ddd.add_sub("交易单", "认购订单")
    ddd.add_sub("交易单", "赎回订单")
    ddd.add_sub("交易单", "交易流水")
    ddd.add_sub("交易单", "支付流水")

    # 营销
    ddd.connect("客户群组", "客户")

    ddd.connect("行情", "产品")
    ddd.connect("工单", "任务")

    ddd.connect("产品", "工单")
    ddd.connect("客户", "工单")  
    ddd.connect("组织结构", "工单")

    # 债券
    ddd.connect("客户", "报量")
    ddd.connect("报量", "台账")
    ddd.connect("报量", "中收")

    # 基金 
      

    # 资管计划

    # 同业存放

    # 理财

    return ddd
