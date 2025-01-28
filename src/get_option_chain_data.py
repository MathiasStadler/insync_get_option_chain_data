from ib_insync import *
from ibapi.common import TickerId, SetOfFloat, SetOfString, MarketDataTypeEnum

# Connect to the Interactive Brokers paper trading account
# Make sure TWS or IB Gateway is running and API is enabled
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=15)  # Default paper trading port is 7496
ib.reqMarketDataType(MarketDataTypeEnum.DELAYED)

# Define the stock symbol and expiration date
symbol = 'META'
exchange = "SMART"
expiration_date = '20250207'  # Format: YYYYMMDD

# Create a stock contract for TREX
stock = Stock(symbol, 'SMART', 'USD')

# https://medium.com/@kchanchal78/connecting-to-interactive-brokers-to-get-option-chain-data-using-python-5640196057ad

underlying = Index(symbol, exchange)
print("********  OPTION CHAIN *********")
print(f"Requesting option chain for symbol => {underlying.symbol} exchange =>  {underlying.exchange}")


contract = Stock('META', 'SMART', 'USD')
contract_details = ib.reqContractDetails(contract)
print(contract_details)

# contract_details = ib.reqContractDetails(underlying)



if contract_details:
    conId = contract_details[0].contract.conId
    print(f" Line35 : ConId for {symbol}: {conId}")

    option_chain = ib.reqSecDefOptParams(underlying.symbol, '', underlying.secType, conId)
    for chain in option_chain:
        print(f"Exchange: {chain.exchange}")
        print(f"Underlying ConId: {chain.underlyingConId}")
        print(f"Trading Class: {chain.tradingClass}")
        print(f"Multiplier: {chain.multiplier}")
        print(f"Expirations: {chain.expirations}")
        print(f"Strikes: {chain.strikes}")
        print('-' * 50)
        print("********  END Here (Requesting option Chain) *********")

# Disconnect from IB
ib.disconnect()