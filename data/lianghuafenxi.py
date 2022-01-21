from app.dfd import DFD

def biz():
    dfd = DFD("量化分析")
    dfd.create_request("分析师", "量化分析").span("量化策略平台子系统")
    return dfd
