from app.injector import Injector
from app.biz import BizBlueprint, Group


class BizAll:
    def __init__(self,injector):
        super().__init__()
        self.injector = injector
        self.data = [
            self.ZCFZ(),
            self.JRTY(),
            self.JRJY(),
            self.ZJYYZX(),
            self.ZCTGSYB(),
            self.HK(),
            self.ZCGLSYB(),
            self.CWQHB(),
            self.FXGLB(),
            self.JZYYZX(),
            self.PZCPSYB(),
            self.GJSJRSYB(),
            self.LAJRZX(),
            self.SHZMSYQ(),
            self.XDFXSP(),
            self.PAYHYYGLB(),
            self.LINGSHOU(),
            self.DUIGONG(),
        ]
        self.bind_biz()

    def generate_graph(self):
        self.injector.clear()
        for i in self.data:
            i.generate_business(self.injector)
            i.generate_groups(self.injector)

    def ZCFZ(self):
        biz = BizBlueprint("资产负债管理部")
        group = biz.root
        [group.child(x) for x in [
            "存款保险管理室",
            "资本管理室",
            "统计信息管理室",
            "资金管理室",
            "定价管理室",
            "规划管理室"
        ]]

        Group.find_or_create("存款保险管理室")  # .bind_biz("存款保险管理")
        Group.find_or_create("资本管理室")  # .bind_biz("资本管理")
        Group.find_or_create("统计信息管理室")  # .bind_biz("统计信息管理")
        # Group.find_or_create("资金管理室").bind_biz("资金预报")
        Group.find_or_create("定价管理室")  # .bind_biz("定价管理")
        Group.find_or_create("规划管理室")  # .bind_biz("规划管理")
        return biz

    def JRTY(self):
        biz = BizBlueprint("金融同业事业部")
        group = biz.root
        [group.child(x) for x in [
            "投后及销后管理部",
            "业务支持部",
            "产品管理部",
            "平台开发及运营管理部",
            "组合管理部",
            "渠道管理部",
            "网络金融部",
            "客户管理部",
            "另类投资部",
            "各地方分行金融同业事业部"
        ]]
        Group.find_or_create("网络金融部")
        Group.find_or_create("平台开发及运营管理部")

        # Group.find_or_create("投后及销后管理部").bind_bizs(["同业项目合规"])  # TIMP
        # Group.find_or_create("业务支持部").bind_bizs(["同业业务考核"])  # 企划 PMS
        # Group.find_or_create("客户管理部").bind_bizs(["同业客户引入"])  # 智慧同业CRM
        # Group.find_or_create("产品管理部").bind_bizs(["同业产品引入", "同业产品行E通管理"])  # "撮合"？，TIMP

        # Group.find_or_create("组合管理部").bind_bizs(["同业产品投资", "同业存放", "同业存款"])
        # Group.find_or_create("另类投资部").bind_bizs(["同业产品投资"])  # , "资产证券化", "资管计划", "票据业务"

        # Group.find_or_create("渠道管理部").bind_bizs(["同业产品销售", "行E通代销", "同业销售线索"])  # 存管 #"业绩考核方法", "中小非银机构"？ PMS？
        # Group.find_or_create("各地方分行金融同业事业部").bind_bizs(["同业产品销售", "行E通代销", "同业销售线索"])  # 同E家/行E通。MUREX，TIMP/三方存管
        # Group.find_or_create("客户管理部").bind_bizs(["行E通账户"])
        
        return biz

    def JRJY(self):
        biz = BizBlueprint("金融交易部")
        group = biz.root
        [group.child(x) for x in [
            "债券做市团队",
            "资金交易团队",
            "策略交易团队",
            "衍生品做市团队",
            "交易中台团队",
            "量化分析团队",
            "智能算法团队",
            "FICCIT团队",
            "产品经理团队"
        ]]
        Group.find_or_create("智能算法团队")
        Group.find_or_create("FICCIT团队")
        Group.find_or_create("策略交易团队")

        # Group.find_or_create("债券做市团队").bind_bizs(["固收做市"])
        # Group.find_or_create("资金交易团队").bind_bizs(["流动性"])
        # Group.find_or_create("衍生品做市团队").bind_bizs(["衍生品做市"])
        # Group.find_or_create("交易中台团队").bind_bizs(["风险管控"])
        # Group.find_or_create("量化分析团队").bind_biz("量化分析")
        # Group.find_or_create("产品经理团队").bind_bizs(["结构化产品", "利率交易", "账户贵金属", "柜台债券","金交所代理","黄金账户"])
        return biz

    def ZJYYZX(self):
        biz = BizBlueprint("资金运营中心")
        group = biz.root
        [group.child(x) for x in [
            "财务企划室",
            "内控合规室",
            "固定收益团队",
            "外汇交易团队",
            "衍生品团队",
            "企业销售室",
            "产品管理室",
            "结构融资室",
            "司库交易室",
            "策略交易团队",
            "综合管理中心",
            "贵金属自营交易团队"
        ]]

        Group.find_or_create("财务企划室")
        Group.find_or_create("内控合规室")
        Group.find_or_create("产品管理室")
        Group.find_or_create("结构融资室")
        Group.find_or_create("司库交易室")
        Group.find_or_create("策略交易团队")
        Group.find_or_create("综合管理中心")

        # Group.find_or_create("固定收益团队").bind_biz("固收自营")
        # Group.find_or_create("外汇交易团队").bind_bizs(["外汇代客交易", "报价平盘", "外汇自营"])
        # Group.find_or_create("企业销售室").bind_biz("外汇代客交易")  

        return biz

    def ZCTGSYB(self):
        biz = BizBlueprint("资产托管事业部")
        group = biz.root
        [group.child(x) for x in [
            "基金服务中心",
            "规划管理室",
            "督察合规室",
            "IT系统支持室",
            "市场拓展室",
            "估值核算室",
            "资金清算室"
            # "创新发展室"
        ]]

        Group.find_or_create("基金服务中心").bind_biz("基金服务")
        Group.find_or_create("规划管理室")
        Group.find_or_create("督察合规室").bind_biz("交易监督")
        Group.find_or_create("IT系统支持室").bind_bizs(["托管服务", "基金服务"])
        Group.find_or_create("市场拓展室").bind_bizs(
            ["托管服务", "托管账户"]) 
        Group.find_or_create("估值核算室").bind_bizs(
            ["估值核算"])
        Group.find_or_create("资金清算室").bind_bizs(
            ["资金清算"])
        # Group.find_or_create("创新发展室")
        return biz

    def HK(self):
        biz = BizBlueprint("平安银行香港分行")
        group = biz.root
        [group.child(x) for x in [
            "金融市场部",
            "企业银行部",
            "企划财务部",
            "人事行政部（行政）",
            "科技运营部",
            "人事行政部（人力）",
            "稽核监察部",
            "法律合规部",
            "风险管理部",
            "大零售板块"
        ]]

        Group.find_or_create("金融市场部").bind_bizs(["结构化产品", "利率交易", "港行-外汇交易"])
        Group.find_or_create("企业银行部")
        Group.find_or_create("企划财务部")
        Group.find_or_create("人事行政部（行政）")
        Group.find_or_create("科技运营部")
        Group.find_or_create("大零售板块")
        Group.find_or_create("人事行政部（人力）")
        Group.find_or_create("稽核监察部")
        Group.find_or_create("法律合规部")
        Group.find_or_create("风险管理部").bind_biz("风险管控")
        return biz

    def ZCGLSYB(self):
        biz = BizBlueprint("平安银行资产管理事业部")
        group = biz.root
        [group.child(x) for x in [
            "营销与综合室",
            "综拓发展室",
            "项目投资室",
            "商品衍生品与另类投资室",
            "组合管理室",
            "产品研发与政策研究室",
            "系统与运营支持室",
            "财务企划团队",
            "综合行政团队",
            "集中交易团队",
            "老产品投资团队",
            "科技运营团队",
            "非标投资团队",
            "事业部风险合规团队",
            "固定收益投资团队",
            "创新投资团队",
            "渠道产品团队",
            "资本市场投资室",
            "固定收益投资室",
            "综合规划发展室"
        ]]

        Group.find_or_create("营销与综合室")
        Group.find_or_create("综拓发展室")
        Group.find_or_create("项目投资室")
        Group.find_or_create("商品衍生品与另类投资室")
        Group.find_or_create("组合管理室")
        Group.find_or_create("产品研发与政策研究室")
        Group.find_or_create("系统与运营支持室")
        Group.find_or_create("财务企划团队")
        Group.find_or_create("综合行政团队")
        Group.find_or_create("集中交易团队")
        Group.find_or_create("老产品投资团队")
        Group.find_or_create("科技运营团队").bind_biz(
            "结构化产品")  # todo: TBC 结构化产品是否是同一个
        Group.find_or_create("非标投资团队")
        Group.find_or_create("事业部风险合规团队")
        Group.find_or_create("固定收益投资团队")
        Group.find_or_create("创新投资团队")
        Group.find_or_create("渠道产品团队")
        Group.find_or_create("资本市场投资室")
        Group.find_or_create("固定收益投资室")
        Group.find_or_create("综合规划发展室")

        return biz

    def CWQHB(self):
        biz = BizBlueprint("平安银行财务企划部")
        group = biz.root
        [group.child(x) for x in [
            "税务管理室",
            "财务报告室",
            "管理会计室",
            "数字化经营PMO团队",
            "预算考核室",
            "费用管理室",
            "采购管理室",
            "经营分析室"
        ]]

        Group.find_or_create("税务管理室")
        Group.find_or_create("财务报告室").bind_biz("资金清算核算")
        Group.find_or_create("管理会计室")
        Group.find_or_create("数字化经营PMO团队")
        Group.find_or_create("预算考核室")
        Group.find_or_create("费用管理室")
        Group.find_or_create("采购管理室")
        Group.find_or_create("经营分析室")

        return biz

    def FXGLB(self):
        biz = BizBlueprint("平安银行风险管理部")
        group = biz.root
        [group.child(x) for x in [
            "授信后督中心",
            "信用评级室",
            "新资本协议室",
            "行业研究室",
            "信用风险管理室",
            "市场风险管理室",
            "资产监控部",
            "产品风险管理室",
            "系统管理室",
            "风险预算室",
            "放款中心"
        ]]

        Group.find_or_create("授信后督中心")
        Group.find_or_create("信用评级室")
        Group.find_or_create("新资本协议室")
        Group.find_or_create("行业研究室")
        Group.find_or_create("信用风险管理室")
        Group.find_or_create("市场风险管理室").bind_bizs(["市场风险监督"])
        Group.find_or_create("资产监控部")
        Group.find_or_create("产品风险管理室")
        Group.find_or_create("系统管理室")
        Group.find_or_create("风险预算室")
        Group.find_or_create("放款中心")

        return biz

    def JZYYZX(self):
        biz = BizBlueprint("集中运营中心资金业务运营中心")
        group = biz.root
        [group.child(x) for x in [
            "外币资金业务组",
            "本币资金业务组",
            "交易核实系统支持组",
            "理财及贵金属业务组"
        ]]

        Group.find_or_create("外币资金业务组").bind_biz("资金清算核算")
        Group.find_or_create("本币资金业务组").bind_biz("资金清算核算")
        Group.find_or_create("交易核实系统支持组")  # todo: TBC
        Group.find_or_create("理财及贵金属业务组").bind_biz(
            "理财及贵金属清算&核算")  # todo: TBC, 缺系统

        return biz

    def PZCPSYB(self):
        biz = BizBlueprint("平安银行派驻产品事业部风险团队")
        group = biz.root
        [group.child(x) for x in [
            "派驻扶贫金融办公室风险团队",
            "派驻普惠金融事业部风险团队",
            "派驻资产管理事业部风险合规团队",
            "派驻资金同业风险团队",
            "派驻投资银行事业部风险团队",
            "总行派驻金融交易部暨资金运营中心风险团队",
            "总行派驻金融同业事业部风险团队",
            "派驻IT风险团队",
            "交易银行事业部派驻风险团队",
            "交易银行事业部派驻科技团队",
            "派驻公司网络金融事业部风险团队",
            "派驻交易银行事业部风险团队",
            "派驻离岸金融事业部风险团队"
        ]]

        Group.find_or_create("派驻扶贫金融办公室风险团队")
        Group.find_or_create("派驻普惠金融事业部风险团队")
        Group.find_or_create("派驻资产管理事业部风险合规团队")
        Group.find_or_create("派驻资金同业风险团队")
        Group.find_or_create("派驻投资银行事业部风险团队")
        Group.find_or_create(
            "总行派驻金融交易部暨资金运营中心风险团队").bind_bizs(["风险管控", "敞口监控"])
        Group.find_or_create("总行派驻金融同业事业部风险团队")
        Group.find_or_create("派驻IT风险团队")
        Group.find_or_create("交易银行事业部派驻风险团队")
        Group.find_or_create("交易银行事业部派驻科技团队")
        Group.find_or_create("派驻公司网络金融事业部风险团队")
        Group.find_or_create("派驻交易银行事业部风险团队")
        Group.find_or_create("派驻离岸金融事业部风险团队")

        return biz

    def GJSJRSYB(self):
        biz = BizBlueprint("贵金属金融事业部筹备组")
        group = biz.root
        [group.child(x) for x in [
            "筹备组规划发展部",
            "筹备组司库内控部",
            "筹备组营销管理部",
            "筹备组自营交易团队",
            "筹备组结构融资团队",
            "筹备组代理交易团队",
            "筹备组渠道营销团队",
            "筹备组资产配置团队",
            "筹备组策略交易团队"
        ]]
        Group.find_or_create("筹备组渠道营销团队")
        Group.find_or_create("筹备组规划发展部")
        Group.find_or_create("筹备组司库内控部")
        Group.find_or_create("筹备组营销管理部")

        # Group.find_or_create("筹备组自营交易团队").bind_bizs(["黄金自营"])  # 系统：黄金自营
        # Group.find_or_create("筹备组结构融资团队").bind_bizs(["黄金租赁"])  # 系统：黄金租赁
        # Group.find_or_create("筹备组代理交易团队").bind_bizs(["实物金",  "套期保值"])  # 系统：实物金，黄金二级，清算行        
        # Group.find_or_create("筹备组资产配置团队").bind_bizs(["黄金份额"])  # 系统：黄金账户，线上交易
        # Group.find_or_create("筹备组策略交易团队").bind_bizs(["量化交易"])  # 系统： 代客贵金属
        return biz

    # Remark:
    # 1、黄金自营：黄金期权、做市交易、询价
    # 2、量化交易：做市交易
    # 3、贵金属账户：即存金


    # 做市交易
    # "结构融资"
    #贵金属交易业务

    def LAJRZX(self):
        biz = BizBlueprint("离岸金融中心")
        group = biz.root
        [group.child(x) for x in [
            "创新研发团队",
            "资金管理团队",
            "业务管理室",
            "外汇政策团队",
            "运营管理团队",
            "国际结算及贸融团队",
            "风险管理团队"
        ]]

        Group.find_or_create("创新研发团队")
        Group.find_or_create("资金管理团队")
        Group.find_or_create("业务管理室")
        Group.find_or_create("外汇政策团队")
        Group.find_or_create("运营管理团队").bind_biz("外汇交易")
        Group.find_or_create("国际结算及贸融团队")
        Group.find_or_create("风险管理团队")

        return biz

    def SHZMSYQ(self):
        biz = BizBlueprint("上海自贸试验区分行")
        group = biz.root
        [group.child(x) for x in [
            "自贸金融部"
        ]]

        Group.find_or_create("自贸金融部").bind_bizs(
            ["外汇交易"])
        return biz

    def PAYHYYGLB(self):
        biz = BizBlueprint("平安银行运营管理部")
        group = biz.root
        [group.child(x) for x in [
            "信中运营中心",
            "零售运营管理室",
            "公司运营管理室",
            "综合管理室",
            "运营风险管理室",
            "网点管理中心",
            "账户尽调中心",
            "结算与系统管理室",
            "安全保卫中心",
            "消费者权益保护中心",
            "派驻交易银行事业部产品运营管理团队"
        ]]

        Group.find_or_create("信中运营中心")
        Group.find_or_create("零售运营管理室")
        Group.find_or_create("公司运营管理室")
        Group.find_or_create("综合管理室")
        Group.find_or_create("运营风险管理室")
        Group.find_or_create("网点管理中心")
        Group.find_or_create("账户尽调中心")
        Group.find_or_create("结算与系统管理室").bind_bizs(["证券资金清算代理"])
        Group.find_or_create("安全保卫中心")
        Group.find_or_create("消费者权益保护中心")
        Group.find_or_create("派驻交易银行事业部产品运营管理团队")
        return biz

    def XDFXSP(self):
        biz = BizBlueprint("平安银行公司授信审批部")
        group = biz.root
        [group.child(x) for x in [
            "信贷风险管理"
        ]]

        Group.find_or_create("信贷风险管理").bind_bizs(["额度调整"])
        return biz

    def LINGSHOU(self):
        biz = BizBlueprint("零售网金")
        group = biz.root
        [group.child(x) for x in [
            "财富管理"
        ]]
        return biz
    
    def DUIGONG(self):
        biz = BizBlueprint("对公网金")
        group = biz.root
        [group.child(x) for x in [
            "对公网金贵金属"
        ]]
        return biz

    def bind_biz(self):
        # 平安银行公司授信审批部
        Group.find_or_create("信贷风险管理").bind_bizs(["额度调整"])
        Group.find_or_create("自贸金融部").bind_bizs(
            ["外汇交易"])
        Group.find_or_create("资金管理室").bind_biz("资金预报")
        # 同业金融
        Group.find_or_create("投后及销后管理部").bind_bizs(["同业项目合规"])  # TIMP
        Group.find_or_create("业务支持部").bind_bizs(["同业业务考核"])  # 企划 PMS
        Group.find_or_create("客户管理部").bind_bizs(["同业客户引入"])  # 智慧同业CRM
        Group.find_or_create("产品管理部").bind_bizs(["同业产品引入", "同业产品行E通管理"])  # "撮合"？，TIMP
        Group.find_or_create("组合管理部").bind_bizs(["同业产品投资", "同业存放", "同业存款"])
        Group.find_or_create("另类投资部").bind_bizs(["同业产品投资"])  # , "资产证券化", "资管计划", "票据业务"
        Group.find_or_create("渠道管理部").bind_bizs(["同业产品销售", "行E通代销", "同业销售线索"])  # 存管 #"业绩考核方法", "中小非银机构"？ PMS？
        Group.find_or_create("各地方分行金融同业事业部").bind_bizs(["同业产品销售", "行E通代销", "同业销售线索"])  # 同E家/行E通。MUREX，TIMP/三方存管
        Group.find_or_create("客户管理部").bind_bizs(["行E通账户"])
        # 金融交易
        Group.find_or_create("债券做市团队").bind_bizs(["固收做市"])
        Group.find_or_create("资金交易团队").bind_bizs(["流动性"])
        Group.find_or_create("衍生品做市团队").bind_bizs(["衍生品做市"])
        Group.find_or_create("交易中台团队").bind_bizs(["风险管控"])
        Group.find_or_create("量化分析团队").bind_biz("量化分析","量化交易")
        Group.find_or_create("产品经理团队").bind_bizs(["结构化产品", "利率交易", "账户贵金属", "柜台债券","金交所代理","黄金账户"])
        # 资金运营中心
        Group.find_or_create("固定收益团队").bind_biz("固收自营")
        Group.find_or_create("外汇交易团队").bind_bizs(["外汇代客交易", "报价平盘", "外汇自营"])
        Group.find_or_create("企业销售室").bind_biz("外汇代客交易")
        Group.find_or_create("贵金属自营交易团队").bind_bizs(["黄金自营","保价金条","黄金回购"])  # 系统：黄金自营
        
        # 零售网金
        Group.find_or_create("财富管理").bind_biz("实物金")
        # 对公网金贵金属
        Group.find_or_create("对公网金贵金属").bind_bizs(["黄金租赁"])  # 系统：黄金租赁
        Group.find_or_create("对公网金贵金属").bind_bizs(["贵金属套期保值"])  # 系统：实物金，黄金二级，清算行
        # 贵金属筹备
        
        
