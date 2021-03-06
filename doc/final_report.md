# 架构治理目标
* 提升业务响应力
* 提升服务质量
* 提升研发效能

# 现状调研和问题识别
### 复杂业务缺乏设计，产品线重复建设，缺乏核心系统沉淀，学习成本高，缺乏赋能
现有业务线使用筒仓方式构建，在以客户为中心的时代需要横向打通系统之间的能力时遇到困难。
* 例1: 外汇和账户贵金属之间的保证金账户需要打通很困难
* 例2:客户经理进行自营和代销产品时需要帮助客户维护多套资料，缺乏完整的客户视图  

### 部分技术架构老旧，改造成本巨高不下，服务质量难以保证
部分技术架构还在使用陈旧的单体应用，面临用户流量的增长和高可用的挑战时，改造和部署成本很高。部分完成现代化技术框架改造的系统在系统的可维护性上已经看到了成效，需要继续推进

### 大型团队边界模糊，缺乏一致的概念和方法，协作困难，开发效能需要提升
不同团队在理解架构时，没有能统一语言，出现概念上的模糊，例如产品，交易这些在不同业务线上的二意性
不同团队的系统设计方法有差异，大多数系统使用了面向过程的方式进行，行E通部分使用了面向领域的设计

# 引入设计方法

## 企业架构模型简述
### 组织维度
从业务角度理解板块的基本划分，明确业务特征，确定业务上的边界，最终纵向划分团队
业务展开的层次:
* 业务板块:资金同业
* 业务线:同业，交易，托管  
业务线特征: 用户需求增加快，流程变化多；交易用户访问量增加，交易品种和方式增加，托管前台业务稳定，后台会计处理变更多
* 产品线:行E通，智慧同业；交易通和国债/贵金属/TIMP + MUREX；托管
* 产品小组

## 用户维度分解（价值链）
从用户角度理解系统的层次划分，明确整体系统分层，确定分层内的系统技术变化速度
### 角色和触点  
变化最快，这里出一张图，描述三个业务线的角色和触点信息
### 网关
目前出现较多诉求，应当加快建设，UM登录
### 业务逻辑
对于同业服务，变化比较多，体现在不同业务流程的差异化
对于交易服务，前端服务被客户端集成，而且要求交易速度高，不需要业务逻辑层，客户端直接对接交易引擎
### 领域服务
对于同业服务和托管业务，变化比较确定，体现在不同领域概念的稳定度
对于交易服务，交易流程为核心设计对象，其他领域气支撑作用  

## 系统设计维度
从开发角度理解系统从业务流程到应用领域的设计，明确领域和微服务划分的边界
### 业务架构
* 场景，用例
* 用户旅程
### 应用架构-组件和编排
* 领域，服务
* 编排，BFF
### 技术架构-数据和通讯
* 数据
* 通讯

# 对齐概念，落地设计产出
## 概念输出
产品，交易等名词定义对齐
## 同业团队的应用设计方法-领域设计
* 客户旅程，场景，用例
* 领域，服务，实体和接口
## 同业团队的技术设计方法-微服务
* 应用设计
* 部署监控
## 前后架构的对比
* 系统间关系简化
* 系统整体质量稳定

## 交易团队的应用设计方法-数据流
* 节点
* 数据流

## 交易团队的技术设计方法-流计算
* 总线
* 计算节点

# 后续计划
## 核心领域深化设计
### 同业
* 层次划分，有了基本框架，划分出业务逻辑和领域逻辑的团队，形成能力线，业务逻辑线关注与用户交互，任务编排，工作流
* 领域逻辑内的业务进一步以专业分工聚合，形成customer/product/settlement/accounting这样的专业能力，构建API门户
* 行E通/智慧同业/存管 
* WOW/

### 交易
* 组件划分已经完成，目前的组件分布已经完成
* 根据当前的组件设计，对现有的子系统进行模块上的识别，对于存在的问题标记出来
* 根据项目机会选择合适的组件设计细部设计，例如MarketData

## 架构守护
* 组建架构小组，管理层次和领域组件，进行架构决策
* 配合和敏捷构建DevOps能力，形成可视化的开发态和运行态系统架构关系

## 关键技术架构实现
* 确定各层次的关键技术架构原则
* 根据当前的技术要求，给出技术架构和框架选型的相关实践指导

#附录
## 词汇表
## 领域词汇表