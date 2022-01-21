# Market Trading

## Quote Management
## Dealer Workbench
## Market Order Execution
The Market Order Execution Service Domain is responsible for the booking of securities transactions (e.g. resulting from market orders or some types of corporate actions) on investment accounts, so in terms of security name plus quantity. Market Order Execution knows the different transaction types and the related booking sets. It will call Securities Position Keeping to create the debit and the credit bookings of a transaction. It will ensure that the bookings of a securities transaction are executed completely or not at all (the latter in the case of an exception). 
The execution of a market order may be in parts (trades) or it may be combined with other market orders for a block trade. The Service Connection "Execute Market Order" on this Service Domain handles the execution of (an undivided part of) one Market Order. 

A securities transaction will have a related money transaction. This will be handled by Payment Order - Payment Execution. 


市场订单执行服务域负责创建投资帐户上的证券交易订单，包含证券名称和数量，它包括不同的交易类型和相关的交易组合。它将根据头寸来确定交易的借贷方想。它将确保证券交易的成功和失败回滚。市场订单的执行可以是部分交易（交易），也可以与其他市场订单组合进行大宗交易。该服务域上的服务连接“执行市场订单”处理一个市场订单（一个未分割部分）的执行。

证券交易将有相关的货币交易。这将由“付款单-付款执行”处理。


## Program Trading
## Suitability Checking
Role Definition:Confirm that all involved counterparties are suitable for a proposed market trade. The checks address regulatory requirements to ensure involved parties are suitably qualified/knowledgeable to participate in the type of trading activity (e.g. in the US suitability is defined by FINRA Rule 2111)
Key Features:
* Determine suitability requirements 
* Match these to the prospective investor 
* Perform confirmation checks with the customer 
* Report and document the results of the suitability checks as appropriate
## Market Making
Role Definition:Orchestrate the market making of a security (matching buy to sell orders typically through coordination with a stock exchange)  
Example of Use:A financial institution acts as the market maker for a number of market assets/securities. Buy and sell trades are automatically captured and the pricing adjusted to maintain a limited net position by influencing buy/sell decisions  

## Stock Lending/Repos
## Market Order
## Traded Position Management