from app.dfd import DFD

def biz():
    # sys = ["同业CRM应用","同业CRM营销销售管理服务","同业CRM客户管理服务","同业CRM数据协议交换服务","智慧同业统一门户批量服务","智慧同业统一门户适配器服务","同业销售产品工厂管理台","智慧同业统一门户后台服务","一账通前置","行E通互联网平台管理台","行E通互联网平台","行E通一账通前置服务","行E通理财能力服务","行E通账户中心","行E通用户服务","行E通客户服务","行E通适配服务","行E通查询分析服务","行E通批量调度任务","行E通数据交换中心（协议转换）","行E通清算中心","行E通支付中心","行E通业务规则服务","行E通资产服务","行E通流程服务","行E通公共服务","行E通债券产品能力服务","行E通数据交换中心（文件处理）","行E通基金产品能力服务","行E通产品子系统"]
    # sys = ["同业CRM应用","同业CRM营销销售管理服务","同业CRM客户管理服务","同业CRM数据协议交换服务","智慧同业统一门户批量服务","智慧同业统一门户适配器服务","同业销售产品工厂管理台","智慧同业统一门户后台服务","一账通前置","行E通互联网平台管理台","行E通互联网平台","行E通一账通前置服务","行E通理财能力服务","行E通账户中心","行E通用户服务","行E通客户服务","行E通适配服务","行E通查询分析服务","行E通批量调度任务","行E通数据交换中心（协议转换）","行E通清算中心","行E通支付中心","行E通业务规则服务","行E通资产服务","行E通流程服务","行E通公共服务","行E通债券产品能力服务","行E通数据交换中心（文件处理）","行E通基金产品能力服务","行E通产品子系统"]
    dfd = DFD("hyt")
    dfd.create_request("客户","注册").span("行E通门户").span("CRM子系统")
    span = dfd.create_request("客户经理","用户审批").span("同E家").span("CRM子系统")
    span.span("BECIF","客户创建")
    span.span("ODS","客户信息同步")
    dfd.create_request("客户","风险评估").span("行E通门户").span("CRM子系统").span("风评系统")

    span = dfd.create_request("产品经理","产品发布").span("智慧同业门户").span("同业产品工厂")
    dfd.create_request("产品经理","产品上下架").span("智慧同业门户").span("同业产品工厂")

    dfd.create_request("客户经理","查看产品").span("同E家").span("同业产品工厂")

    dfd.create_request("客户","查看产品").span("行E通门户").span("同业产品工厂")
    dfd.create_request("客户","产品资讯").span("行E通门户").span("同业资讯")
    dfd.create_request("客户经理","债券报量").span("智慧同业门户").span("CRM子系统")
    
    dfd.create_request("客户","基金签约").span("行E通门户").span("行E通产品子系统").span("基金公司",external=True)
    dfd.create_request("客户","基金开平仓").span("行E通门户").span("行E通产品子系统").span("行E通代销子系统").span("基金公司",external=True)
    dfd.create_system_request("统一TA","基金交易清算").span("行E通产品子系统").span("D+")

    dfd.create_request("客户经理","同存报价").span("智慧同业门户").span("同业产品工厂")
    dfd.create_request("客户","同存存款").span("行E通门户").span("行E通产品子系统").span("TIMP")
    dfd.create_request("客户","同存支取").span("行E通门户").span("行E通产品子系统").span("TIMP")
    
    return dfd

def hyt_old():
    dfd = DFD("hyt")
    dfd.create_request("客户","注册").span("行E通门户").span("行E通产品子系统").span("CRM子系统")
    dfd.create_request("客户经理","用户审批").span("同E家").span("CRM子系统").span("BECIF","客户创建").span("ODS","客户信息同步")
    dfd.create_request("客户","风险评估").span("行E通门户").span("行E通产品子系统").span("风评系统")

    span = dfd.create_request("产品经理","产品发布").span("智慧同业门户").span("同业产品工厂")
    span.span("行E通产品子系统")
    span.span("同E家")
    dfd.create_request("产品经理","产品上下架").span("智慧同业门户").span("同业产品工厂")

    dfd.create_request("客户","查看产品").span("行E通门户").span("行E通产品子系统")
    dfd.create_request("客户","产品资讯").span("行E通门户").span("行E通产品子系统").span("同业资讯")
    dfd.create_request("客户经理","债券报量").span("智慧同业门户").span("CRM子系统")
    
    dfd.create_request("客户","基金签约").span("行E通门户").span("行E通产品子系统").span("基金公司",external=True)
    dfd.create_request("客户","基金开平仓").span("行E通门户").span("行E通产品子系统").span("行E通代销子系统").span("基金公司",external=True)
    dfd.create_system_request("统一TA","基金交易清算").span("行E通产品子系统").span("D+")

    dfd.create_request("客户经理","同存报价").span("智慧同业门户").span("同业产品工厂")
    dfd.create_request("客户","同存存款").span("行E通门户").span("行E通产品子系统").span("TIMP")
    dfd.create_request("客户","同存支取").span("行E通门户").span("行E通产品子系统").span("TIMP")

    return dfd
