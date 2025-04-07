# FROM HERE
# https://www.youtube.com/watch?v=IITIn1tq1Pg


from ib_insync import *
from ibapi.common import TickerId, SetOfFloat, SetOfString, MarketDataTypeEnum

ib=IB()

ib.connect(
    "127.0.0.1",
    7496,
    clientId=69
)

ib.reqMarketDataType(MarketDataTypeEnum.DELAYED)

# position_list = ib.positions()

positions = ib.positions()

for position in positions:
        contract = position.contract
        market_data = ib.reqMktData(contract)
        print("Market Data {}".format(market_data))
        ib.sleep(1)  # Allow time for market data to be received
        # print(contract.localSymbol)



# result = extract_symbols(position_list)

# print(result)

ib.disconnect()
