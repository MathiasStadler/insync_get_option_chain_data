# FROM HERE
# https://www.youtube.com/watch?v=IITIn1tq1Pg


from ib_insync import *

ib=IB()

ib.connect(
    "127.0.0.1",
    7496,
    clientId=69
)

position_list = ib.positions()

def extract_symbols(position_list):
    symbols =[position.contract.symbol for position in position_list]
    return " and ".join(symbols)

result = extract_symbols(position_list)

print(result)

ib.disconnect()
