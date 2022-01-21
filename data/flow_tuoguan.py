from app.dataflow import Flow,Node

def flow():
    flow = Flow.find_or_create("f1")
    flow.start("SOURCE1").next("PROCESS1").next("PROCESS2")
    flow.start("SOURCE2").next("PROCESS1")