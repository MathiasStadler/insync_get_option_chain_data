from ib_insync import *
from ibapi.common import TickerId, SetOfFloat, SetOfString, MarketDataTypeEnum

# Connect to the IB paper trading account
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=33)
ib.reqMarketDataType(MarketDataTypeEnum.DELAYED)

# Function to get open positions
def get_open_positions():
    positions = ib.positions()
    open_positions_data = []

    for position in positions:
        contract = position.contract
        market_data = ib.reqMktData(contract)
        ib.sleep(1)  # Allow time for market data to be received

        # Collecting required data
        data = {
            'WKN': contract.conId,  # WKN is not directly available, using conId as a placeholder
            'Stock Market Initial Price': market_data.last,
            'Fees': position.avgCost * position.position,  # Example calculation for fees
            'Open': position.position,
            'Profit/Loss': position.position * (market_data.last - position.avgCost),
            'Exchange':"SMART",
            'Expiration Date': contract.lastTradeDateOrContractMonth if hasattr(contract, 'lastTradeDateOrContractMonth') else None
        }
        open_positions_data.append(data)

    return open_positions_data

# Retrieve and print open positions
open_positions = get_open_positions()
for pos in open_positions:
    print(pos)

# Disconnect from IB
ib.disconnect()