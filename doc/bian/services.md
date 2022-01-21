Business Management
    Business Direction
    Corporate Relations
    Corporate Services

Resource Management
    Unit Management
    Human Resources
    Platform Operations
    Buildings & Equipment

Business Development
    Intelectual Property & Knowledge
    Models & Analytics
    Solution Development
    Product Management
    Marketing & Development
    Channel Management

Operations
    Clearing & Settlement
        Settlement Obligation Management
            Orchestrate the clearing and settlement of market transactions    
        Payment Order
            Payment Order handles the internal bank and compliance checks and processing of funds transfers prior to initiating the actual mechanics of transfer which is handled by the service domain Payment Execution. This includes watch-list and other regulatory checks and applying any counterparty specific limits and payment preferences. It may also oversee payment netting arrangements between the bank and other counterparties 
            付款指令，还没发生支付活动，在启动由服务域“付款执行”处理的实际转账机制之前，“付款单”将处理内部银行和合规性检查以及资金转账的处理。这包括监视列表和其他监管检查，并应用交易对手特定的限额和付款首选项。它还可能会监督银行与其他交易对手之间的支付净额安排
            Perform bank and regulatory checks on the payee and payer
            Retrieve counterparty payment preferences 
            Structure payment execution requests to match preferences 
            Oversee counterparty netting arrangements
        Payment Execution
            Payment Execution handles the back-end processing of a movement funds from a debtor account to a creditor account. Payments need to have been authorized and validated against customer/bank agreements before being instructed to Payment Execution. Payment Execution then determines whether debtor and creditor accounts are held within the bank and if not selects the appropriate payment mechanism/channel to use to complete the transfer. It is responsible for ensuring that both (or neither) sides of the exchange are completed successfully 
            执行付款的地方
        Counterparty Administration
            Maintain and provide access to the counterparty reference details to support trading/payment activity. This includes SWIFT addresses, standard settlement instructions that are published. The data is typically acquired using a market feed for the default values, but the facility can support the maintenance of specific details and instructions that apply to the counterparty relationship overriding the public default
            看不懂
        Correspondent Bank Data Management
            This service domain maintains reference details specific to a correspondent banking partner covering payment terms and preferences and security keys. It also consolidates transactional activity as might be needed to track reciprocity with the correspondent bank. Any specific arrangements and terms (e.g. SSIs) that might override market directory details are maintained here as part of the data record. 
            对账时要用的对手行信息
            Maintain correspondent bank reference data 
            Maintain specific correspondent settlement instructions 
            Track correspondent bank's service reciprocity
        Correspondent Bank
            This Service Domain handles incoming and outgoing payment clearing and settlement messages to the bank's correspondent banking partners. The actual message transmission is delegated to the Financial Message Gateway service domain. Correspondent Bank administers the mirror accounting for interbank payments undertaking the underlying account reconciliation tasks.
            执行对手交易信息处理，网关？
        Transaction Engine
            The Service Domain provides a utility/background operational support service to orchestrate a schedule of payment transaction and reporting activities for the fulfillment of certain long term instruments or structured facilities. The Service Domain maintains a link to the associated fulfillment Service Domain and the applicable product instance for reporting and processing issues that may arise.
            对于长生命周期的交易，对任务分解，并确定执行任务的时间，管理整个交易的状态
            Establish the processing schedule for a product instance 
            Process transaction and reporting tasks as necessary 
            Escalate issues to the product fulfillment Service Domain as necessary 
            Report on transaction fulfillment activity
        ACH Fulfillment
            This service domain handles the operational interface with an external automated clearing house (ACH) service. It handles the sending and receipt of batched transactions, servicing reporting and executes the schedule of service operations
            对接清算所
        Order Allocation
            Apply appropriate rules to allocated a completed order across counterparties
            A large market order is partly fulfilled and the pricing and allocation of the constituent transactions is allocated across the counterparties 
            拆单/合并
        Cheque Processing
            This service domains handles the processing of paper checks, performing the necessary checks and extracting the transaction details required to create a payment transaction record stream. This includes MICR number processing and character recognition facilities
            支票业务，要不要管？            
        Card Clearing
            The behavior varies depending on the role of the participant bank/network. A card acquiring Bank consolidates all incoming transactions from Merchants, determining their routing, and transmitting to the respective Card Networks. For the Card Networks it receives and consolidates the transactions from all Acquiring Banks and to distribute and route them to the respective Card Issuing Banks. For the Card Issuing Banks it receives their cardholder transactions from the Card Networks and routes them to the instance of the Credit/Charge Card service domain which is responsible for the card used in the transaction. The transactions may include charges, refunds, and chargebacks. 
        Card Financial Settlement
            This service domain is used by the Card Network to initiate either gross or net settlement for the charges cleared during a specified period and to issue settlement instructions to the Issuing and Acquiring Banks. This requires the Card Network to issue settlement instructions to each Issuing Bank directing them to remit the total amounts corresponding to the cleared charges to designated bank accounts that are managed by the Card Network, which in turn makes the corresponding remittances to the designated bank accounts for the Card Issuers. The service domain is also used by the Issuing and Acquiring banks to perform reconciliation of the settlement instructions against the cleared charges and to initiate remittances through the Payment Order service domain. 
            信用卡业务，先不管
        Card eCommerce Gateway
            This service domain is used by the Card Acquiring bank to handle the authentication, authorization and submission of a Card payment from an e-commerce merchant. It supports the "3-D" Secure method of authentication which routes the authentication request to the Card Issuing Bank, which may use multi-factor authentication for the authentication of the Card and the Cardholder. It also handles the routing of the authorization request through the Card Transaction Switch service domain and the routing of the submitted charges to the Card Clearing service domain. 
            当使用卡在商户的电子商务网站上进行付款时，商户将启动三个步骤来处理付款：1）请求对卡进行身份验证和持卡人； 2）请求对费用金额进行授权； 3）将费用明细提交给收卡人以进行处理和付款。

    Accounting Services
        Commissions
            Capture and structure commissionable transactions that are subsequently processed against an existing commission agreement
            佣金计算
        Accounts Receivable
            Manage the tracking, chasing and receipt of scheduled payments against issued invoices. For the significant majority accounts are likely to be settled in compliance with established arrangements. For late payment the Service Domain includes actions to negotiate with the customer and handle defaulted payments
            管理对应收付款，已开具发票的预定付款的跟踪，追踪和接收。对于绝大多数，帐户很可能会按照既定安排进行结算。对于延迟付款，服务域包括与客户协商并处理拖欠付款的操作
        Customer Tax Handling
        Securities Position Keeping
        Financial Accounting
            财务会计服务域接受财务事实，并根据这些事实创建会计说明。它位于银行的会计界，并且只能用于取款操作才能访问银行，卡和证券界。它知道并维护会计科目表，并且可以创建会计指令以更新总分类帐和子分类帐。
            财务事实的例子包括开设贷款帐户，抵押品重估和定期（例如每天）：付款交易导致的头寸变化。
            Maintain the chart of accounts 
            Provide information about the chart of accounts 
            Reflect the opening of accounts in the GL 
            Create summary interval bookings in the GL for all entries in Position Keeping and (if applicable) Credit Card Position Keeping
        Position Keeping
            交易流水和持仓，维护财务交易日志以用于管理信息，跟踪和对帐目的。它可以提供实用程序，使其能够维持余额/头寸，计算利息并支持交易对账活动。财务交易随后被记入会计系统
            任何产品履行域，活期帐户，储蓄帐户，信用卡等都将交易过帐/跟踪委托给头寸保持服务域。
            Configure the transaction log for recording services 
            Post transactions 
            Repair/update transactions 
            Maintain positions as configured (includes limits and blocks) 
            Provide simple accounting services (e.g. interest accruals) 
            Provide transaction reporting and alert services   
        Customer Position
            Individual products will maintain different financial views for the customer. This service domain consolidates financial details from all in-force products and services in order to derive a consolidated financial view which can include current (real-time) positions and projected/estimated values. The consolidated customer position can cover aspects such as cash flows/balances, credit and collateral positions and may derive actual and estimated/projected values
            客户分户帐
        Account Reconciliation
            Match, reconcile and resolve identified discrepancies between accounts. Includes nostro/vostro arrangements
            对账                          
        Fraud Diagnosis
        Reward Points Account
        Fraud Evaluation
            Analyze suspect transaction with Customer behavior information across product portfolio, using Expert Systems /Artificial Intelligence and/or manual review, including customer contact to determine if transaction is fraudulent.  Further apply Economic Model to determine transaction disposition and notify applicable Product Fulfillment SDs.
            欺诈评估，使用专家系统/人工智能和/或人工审核（包括与客户联系以确定交易是否为欺诈行为），使用整个产品组合中的客户行为信息分析可疑交易。进一步应用经济模型来确定交易处置并通知适用的产品实现
    Custody, Collateral & Documents            
    Operational Services
    External Agency

Products
    Market Operations
        Trade Confirmation Matching
        Financial Instrument Valuation
        Trade/Price Reporting
        Corporate Events
        Trading Book Oversight
        Securities Fails Processing
        Securities Delivery & Receipt Management
        Credit Risk Operations    
    Market Trading
        Quote Management
        Dealer Workbench
        Market Order Execution
        Program Trading
        Suitability Checking
        Market Making
        Stock Lending/Repos
        Market Order
        Traded Position Management
    Trade Banking    
    Corporate Banking    
    Consumer Banking        
    Corporate Finance
        Private Placement
        Hedge Fund Administration
        ECM/DCM
        Mutual Fund Administration
        Unit Trust Administration
        Public Offering    
    Advisory Services
    Loans & Deposits
    Cards


Customers
    Party Reference
        Party Reference Data Directory
            The party reference data directory service domain maintains a potentially wide range of party reference data that might be used in any interaction between the bank and the party including relationship development, sales/marketing, servicing and product delivery. This can include general reference and contact details, party associations, demographic details and some servicing preferences. Different information may be maintained for different party types such as individuals, corporates, partners
            参与方参考数据目录服务域维护着广泛的参与方参考数据，可在银行与参与方之间的任何交互中使用，包括关系开发，销售/营销，服务和产品交付。这可以包括一般参考和联系方式，政党协会，人口统计详细信息和某些服务偏好。可以为不同类型的当事人（例如个人，公司，合伙人）维护不同的信息
            Maintain party reference information 
            Maintain party demographic indicators 
            人口统计指标
            Maintain party roles, associations and relationships 
            角色，协会和关系
            Maintain customer bank contacts 
            联系人
        Legal Entity Directory
            Maintain the legal entity structure including ownership, subsidiaries and partnership details
            Maintain legal entity reference details for bank customers
            维护银行客户的法人参考详细信息
            Track/update legal entity details based on market research and reports 
            根据市场研究和报告跟踪/更新法人实体的详细信息
            Process legal entity detail updates from customers/bank sources 
            处理客户/银行来源的法人实体详细信息更新
            Confirm/provide legal entity details for transaction processing tasks
            确认/提供交易处理任务的法人实体详细信息
        Location Data Management
            The maintenance of location details is used to check the validity, allowed use and occupancy of locations - both physical and virtual. This information can be augmented using external directory services when appropriate. The information is used for authentication and security purposes, and can also be used for interactive location based sales and marketing when combined with location tracking services/capabilities
            Maintain/confirm location address/details 
            维护/确认位置地址/细节
            Track allowed and actual location usage
            跟踪允许的位置和实际位置使用情况
            Track location ownership/occupancy details
            跟踪位置所有权/占用率详细信息
    Investment Services
        Consumer Investments
            This supports consumer initiated securities investment and trading activity for their self-managed securities investments. Trades will typically be blocked/netted against the bank's own securities position for subsequent market execution. Quotes/prices are based on the prevailing price at the time of the customer instruction to trade
            这支持了消费者发起的证券投资以及其自我管理的证券投资的交易活动。通常，将针对银行自身的证券头寸对交易进行冻结/净销，以用于随后的市场执行。报价/价格基于客户指示进行交易时的现行价格
            Provide price quotes
            Initiate market order for consumer customer
            Update banks security position
        eTrading Workbench
            Operate the distributed consumer e-trading facility (local application and network connectivity to the bank). This environment hosts/supports a financial facility type product (service domain Consumer Investments) that customer use to trade securities on their own account through the bank. From the workbench environment using consumer investments a customer can initiate the execution of securities trades against their facility as well as applying service/facility fees and charges. The consumer investments capability accessed through the workbench integrates with the supporting customer accounting facilities which can include more complex margin accounts (and margin call initiation) as necessary
            操作分布式消费者电子交易工具（本地应用程序和银行的网络连接）。此环境托管/支持客户用来通过银行在其自己的帐户上交易证券的金融工具类型产品（服务域“消费者投资”）。在使用客户投资的工作台环境中，客户可以启动针对其设施的证券交易，以及应用服务/设施费用。通过工作台访问的消费者投资功能与支持的客户核算工具集成在一起，该工具可以根据需要包括更复杂的保证金帐户（和发起追加保证金通知）
        Investment Portfolio Planning
            Agree the customer investment portfolio governing principles, risk appetite, management/trading guidelines and target portfolio profile. Identify any desired/target and 'out of bounds' securities/sectors. Ensure disclosures and related eligibility, suitability and other regulatory obligations are addressed and reflected in the agreement
            * Identify and agree investment portfolio properties and make-up (includes risk appetite) Handle regulatory and bank requirements (e.g. disclosures, suitability, eligibility) Identify any target and securities to avoid 
            Agree key roles and schedules for the investment portfolio handling
        Investment Portfolio Management
            Orchestrate the investment/ rebalancing of an investment portfolio to optimize gains remaining within the terms of the portfolio 'charter' or agreement
            Monitor market for opportunities/threats 
            Match identified trading opportunity to investment portfolio policies 
            Initiate market trades to rebalance/improve portfolio make-up
        Investment Portfolio Analysis
            Perform scheduled and ad-hoc performance analysis on a customer's investment portfolio. This can include different types of analysis and performance comparisons
            Consolidate investment portfolio transaction details and comparative market activity reports 
            Select types of performance analysis and apply analyses to the period of transaction data 
            Develop portfolio performance comparisons and evaluations/justifications
    Relationship Management
        Customer Relationship Management
            此功能处理客户关系。通常会有针对高价值客户的客户发展计划和预算/目标。该功能可以利用外部市场洞察力以及内部产品和服务的实现来跟踪绩效并在适当时触发联系。该功能是提供产品/服务匹配和认知度的业务发展的重要来源。作为联系的主要联系人，客户关系经理可以帮助解决问题和解决问题。关系管理适用于公司和高净值客户。自动化的基于知识的设施可能在消费者银行业务级别上提供某些关系管理功能，尤其是用于销售和营销
            Develop a customer relationship plan/targets 
            Liaise/advise customer, develop relationship 
            Match products and services to customer needs 
            Troubleshoot issues with customer
        Customer Behavioral Insights
            This service domain references the range of customer historical data maintained by the Customer Event History service domain to develop behavioral insights into customers. This analysis can support sales and marketing activity (e.g. by determining the likely response to sales efforts based on passed performance) as well as identifying changes in status and behavior that might influence the desired product mix for a customer. The actual analysis routines are developed/maintained by the Customer Behavior Models service domain
            Consolidate customer activity data from internal and external sources 
            Select and apply analyses to the historical customer data 
            Maintain/derive insights into behavior and preferences
        Customer Credit Rating
            This service domain handles the derivation and maintenance of each customer's credit rating for both consumer and corporate customers. The internal rating can integrate externally provided credit details from credit scoring agencies with internal transactional data and relationship assessments. The credit rating will be maintained based on internal rules, but it is possible that a service will be offered to support an unscheduled recalculation of the credit score 
            该服务域为消费者和公司客户处理和维护每个客户的信用等级。内部评级可以将信用评分机构从外部提供的信用详细信息与内部交易数据和关系评估进行集成。信用评级将根据内部规则进行维护，但有可能会提供服务以支持计划外的信用评分重新计算
            Access external rating agencies for customer credit reports 
            Consolidate bank product use that impacts the rating 
            Derive and maintain the bank's customer credit assessment
        Customer Agreement
            The Customer Agreement service domain captures and maintains the master legal terms of conditions in force for a customer (which as noted can be a complex multinational with many underlying product and service specific agreements). 
            Set-up and maintain the customer master agreement 
            Ensure legal, regulatory and corporate considerations are covered in agreement 
            Determine if proposed actions are covered by the agreement
        Sales Product Agreement
            The Sales Product Agreement service domain captures and maintains the legal terms and conditions in force for a sold product. The product specific terms and conditions are subordinate to the terms of the customer master agreement that is maintained by the Customer Agreement service domain. The product contractual terms and conditions influence product and service fulfillment for example by defining applicable fees/rates/penalties and selected features/options. Note that there can be other product configuration features that are not contractually binding - these features are maintained in the associated product/service fulfillment service domain directly 
            销售产品协议服务域捕获并维护对已售出产品有效的法律条款和条件。产品特定的条款和条件从属于客户协议服务域维护的客户主协议的条款。产品合同条款和条件会影响产品和服务的实现，例如通过定义适用的费用/费率/罚款和选定的功能/选项。请注意，可能存在其他未按合同方式绑定的产品配置功能-这些功能直接在关联的产品/服务实现服务域中维护     
            Set-up and maintain the customer sales product agreement 
            Ensure legal, regulatory and corporate considerations are covered 
            Determine if proposed actions are covered by the agreement
        Customer Product and Service Eligibility
            This Service Domain maintains a list of products and services for which a customer is eligible. This could include products and services that the customer has had in the past. In order to update the list, periodically or at certain events, the Service Domain calls Product Matching to find additional products for which the customer is eligible. Once a customer acquires a product or a service, this is removed from the current list and added to the customer's recording in Customer Products and Services.
            该服务域维护客户有资格获得的产品和服务的列表。这可能包括客户过去拥有的产品和服务。为了定期或在某些特定事件中更新列表，服务域调用“产品匹配”以查找客户有资格使用的其他产品。客户获得产品或服务后，将从当前列表中将其删除，并添加到客户产品和服务中的客户记录中。
            Provide a list of products and services for which a customer is eligible 
            Update the list of products and services for which a customer is eligible, based on a request from customer relationship management and with the help of Product Matching) 
        Customer Proposition
            Support customer feature specific product fulfillment
            example:银行对客户实施适用于所有产品的服务费减免。
        Customer Event History
            The service domain captures a wide range of customer events to build a comprehensive history of customer activity that can support subsequent behavioral analysis. This includes key sales/proposal events, relationship management events, product delivery events, detected customer triggers (typically gleaned during servicing dialogues) and possibly externally sourced customer activity. The assembled data is made available for behavioral analysis and for more general reference (as might be used for relationship management for example)
            服务域捕获广泛的客户事件，以建立全面的客户活动历史记录，以支持后续的行为分析。这包括关键的销售/投标事件，关系管理事件，产品交付事件，检测到的客户触发条件（通常在服务对话期间收集）以及可能来自外部的客户活动。组合后的数据可用于行为分析和更一般的参考（例如，可能用于关系管理）
            Log customer sales/marketing and relationship development events 
            Log customer servicing events 
            Log detected life events (from interactions or external research) 
            Log product fulfillment events and alerts
        Customer Products and Services
            This Service Domain maintains the most important data of all products and services that a customer has acquired from the bank. As such it maintains data of current and past products and services. It is the only domain in the model that can provide information on a customer's current products and services.
            该服务域维护客户从银行购买的所有产品和服务中最重要的数据。因此，它维护当前和过去的产品和服务的数据。它是模型中唯一可以提供有关客户当前产品和服务的信息的域。
            Provide a list of products and services that the cuatomer currently takes from the bank 
            Add a product or service to the list when a customer acquires and new product or service
    Sales
        Customer Campaign Execution
            处理客户活动的部署，执行和持续优化。这包括许多类型的主动客户活动，例如追加销售，交叉销售和客户保留。活动执行过程对候选客户进行初步选择和确认，包括向设计部门提供有关活动影响的重要反馈，以根据实际经验支持规范的重新校准和完善
            Candidate customer selection/identification 
            Customer interaction and response capture 
            Campaign performance analysis and feedback
        Prospect Campaign Execution
            处理潜在客户活动的部署，执行和持续改进。这包括许多类型的积极的潜在客户获取活动。活动执行过程执行候选列表的初始选择和确认/确认，并包括将对活动影响的关键反馈提供给设计单位，以支持根据实际经验对规格进行重新校准和完善
            Candidate prospect selection/identification (list development) 
            Prospect interaction and response capture 
            Campaign performance analysis and feedback  
        Party Lifecycle Management   
            Perform party qualification/confirmation checks 
            Maintain a schedule and perform periodic re-assessments 
            Provide status reports and process status update notifications          
        Lead/Opportunity Management
            该服务域捕获，评估和推进在客户关系开发，销售，服务和实现交互过程中可能出现的潜在顾客/机会。在开始正式报价过程之前，它将澄清并确认客户的兴趣，并检查产品是否合适以及客户是否合格
            Lead/opportunity classification and capture 
            Lead/opportunity evaluation and confirmation 
            Verify opportunity, initiate/schedule customer offer processing
        Product Expert Sales Support
            Provide specialist support advice to customers for products and services on offer
            example:An established corporate customer arranges a meeting with a specialist to discuss short term funding options 
        Product Matching
            The service domain implements a decision service (that might be interactive) to isolate the preferred product(s) for which a customer is eligible in a specific servicing situation. The product selection logic will balance factors including customer indicated desired product type/features, customer type/profile, solicitation/retention/enquiry servicing situation, prevailing campaigns/bank preferred products. The decision logic improves product selection to optimize the customer interaction and support business development
            Determine customer product interest 
            Isolate eligible products 
            Consider context to filter/prioritize products 
            Apply broader campaign/bank preferences
        Customer Offer
            报价管理服务域可以为所有类型的客户以及任何允许的产品或服务组合处理报价。它参考产品目录以获取必须遵循的特定于产品的报价说明。要约过程可以结合对产品/服务特定细节的选择（例如，定价和谈判范围，文档/授权/监管要求，资格和声明，信用和其他客户详细信息），客户特定的细节（例如信用状况，其他分类，例如运营费用/保留目标/活动历史记录，人口统计和细分）。服务域编排了潜在的复杂/多线程/多阶段工作流，以使报价到达可以启动产品/服务的地步。
            Obtain offer processing requirements for selected product 
            Confirm customer suitability/eligibility for product 
            Agree product features, fees and pricing with customer 
            Obtain documents/signatures and required disclosures 
            Arrange collateral and obtain underwriting authorizations 
            Perform any audit and compliance checks                  
        Special Pricing Conditions
            This service domain allows the bank to apply special pricing terms and conditions that override standard price calculations. These override facilities are to be used in specific situations where a bank level decision is taken to amend prices or pricing terms in response to some major event or business development action
            Capture authorized override bank pricing terms 
            Broadcast special terms to interested parties 
            Confirm terms applied as required in production
        <!-- Initiate product set-up         -->
    Customer Care
        Servicing Mandate
            服务授权服务域维护银行与外部方之间的协议，该协议管理/约束对银行产品和服务的允许访问。可以在两个级别上定义此访问权限-总体上定义服务提供商，并在更详细的级别上定义特定的客户。
            Set-up mandate covering 3rd party access to services 
            Set-up provider's customer specific servicing permissions 
            Check proposed activity is covered by the mandate 
            Maintain/report on 3rd party activity
        Servicing Order
            服务订单服务域处理可能影响多个产品和服务的请求的处理，并且可能涉及处理周期/步骤，并可能具有相关的费用/收费。可以根据需要定义几种类型的标准“服务订单”以供选择。维修订单可以由客户直接启动，也可以由授权的第三方服务提供商代表他们提出请求。如果请求是由第三方服务提供商代表客户提出的，则过程可以包括检查相关权限/授权是否到位
        Customer Case Management
            管理客户案例处理，跟踪案例解决的有效性和影响。评估并确认决策规则和阈值在公平确定的过程中与过程的一般客户和商人接受程度之间取得了良好的平衡。确保并且有足够的和经过适当培训的资源
            Define and refine the guiding principles and rules for case resolution 
            Assess effectiveness of the case processing function 
            Determine and monitor staffing levels and utilization
        Customer Case
            Case resolution tasks follow specific procedures for the type of case involved. Case resolution can be quick by applying resolution rules and obtaining additional authorization as necessary, or they can be long living activities, for example where documentation is requested and has to be retrieved from merchants or other interested parties before the disputed issue can finally be ruled upon. A wide range of case types can be expected
            Customer case capture and classification 
            Case related information consolidation 
            Customer case diagnosis and decisioning 
            Customer case resolution implementation
        Card Case
            Capture, track, resolve and report on card related transactional disputes, handling all the dispute resolution messages between the Issuer, the Card Network and the Acquirer.
            Consolidation of transaction details 
            Chargeback processing 
            Case decisioning and arbitration 
            Case resolution
Channels
    Information Providers
        Financial Instrument Reference Data Management
        Financial Market Analysis
        Public Reference Data Management
            Consolidate market information from multiple sources and in any suitable media/format in order to build a bank financial market knowledge-base. The service domain activities include maintaining, refining, qualifying/verifying and presenting information in order to improve the quality of the available market intelligence within the bank
        Market Data Switch Operation
        Market Information Management
        Information Provider Operation
        Financial Market Research
    Cross Channel
        Contact Handler
        Session Dialogue
        Party Authentication
        Contact Routing
        Transaction Authorization
        Customer Access Entitlement
        Customer Profile
        Channel Activity History
        Customer Workbench    
    Channel Specific
    Servicing
    Distribution
















Market Risk
Compliance
Financial Control
Credit Risk
Operational Risk
Group Treasury


Service Domain Overview Diagrams





