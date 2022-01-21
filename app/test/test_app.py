from app.biz import BizBlueprint,Group

class TestServiceBlueprint:
    def test_group(self):
        biz = BizBlueprint("")
        group = biz.root
        [group.child(x) for x in ["资产托管事业部","投资管理事业部","投资银行事业部"]]
        for x in ["资产托管","基金服务"]:
            Group.find_or_create("资产托管事业部").bind_biz(x)
        for x in ["结算业务"]:
            Group.find_or_create("投资管理事业部").bind_biz(x)
        for x in ["投行业务"]:
            Group.find_or_create("投资银行事业部").bind_biz(x)
        biz.generate_business()
        biz.generate_groups()

    def xx_group2(self):
        biz = BizBlueprint("交易银行事业部")
        group = biz.root
        [group.child(x) for x in ["资金运营中心","离岸金融中心","自贸试验区分行","香港分行金融市场部","金融交易部","资金托管事业部"]]
        for x in ["个人外汇","对公外汇","报价平盘"]:
            Group.find_or_create("资金运营中心").bind_biz(x)
        for x in ["对公外汇"]:
            Group.find_or_create("离岸金融中心").bind_biz(x)
        for x in ["对公外汇","对公利率"]:
            Group.find_or_create("自贸试验区分行").bind_biz(x)
        for x in ["港行外汇利率"]:
            Group.find_or_create("香港分行金融市场部").bind_biz(x)
        for x in ["报价平盘","对公利率","账户贵金属","柜台债券","债券回购"]:
            Group.find_or_create("金融交易部").bind_biz(x)
        for x in ["基金资金托管"]:
            Group.find_or_create("资金托管事业部").bind_biz(x)

        assert len(group.children) == 6
        biz.generate_business()
        biz.generate_groups()

    def xxx_group(self):
        biz = BizBlueprint("贵金属事业部")
        group = biz.root
        node = group.child("交易团队")
        [node.child(x) for x in ["做市交易组","实物金及代理组","策略交易组","同业交易组"]]
        node = group.child("投融资团队")
        [node.child(x) for x in ["黄金租赁组"]]
        node = group.child("零售团队")
        [node.child(x) for x in ["产品开发组"]]

        for x in ["做市交易","现货交易","即远掉"]:
            Group.find_or_create("做市交易组").bind_biz(x)
        for x in ["实物金","金交所代理"]:
            Group.find_or_create("实物金及代理组").bind_biz(x)
        for x in ["程序化交易","期权交易"]:
            Group.find_or_create("策略交易组").bind_biz(x)
        for x in ["同业拆借"]:
            Group.find_or_create("同业交易组").bind_biz(x)
        for x in ["换金租赁"]:
            Group.find_or_create("黄金租赁组").bind_biz(x)
        for x in ["黄金份额","金生金","互联网黄金"]:
            Group.find_or_create("产品开发组").bind_biz(x)

        assert len(group.children) == 3
        assert len(biz.businesses) == 12
        biz.generate_business()
        biz.generate_groups()
