from data.collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

tech_tickers = [
    'NVDA', 'AAPL', 'MSFT', 'AVGO', 'MU', 'AMD', 'INTC', 'ORCL',
    'CSCO', 'PLTR', 'AMAT', 'LRCX', 'PANW', 'DELL', 'KLAC', 'ANET',
    'TXN', 'CRWD', 'IBM', 'STX', 'APH', 'MRVL', 'ADI', 'QCOM',
    'WDC', 'CRM', 'GLW', 'NOW', 'FTNT', 'ACN', 'ADBE', 'INTU',
    'DDOG', 'CDNS', 'HPE', 'SNPS', 'MSI', 'LITE', 'MPWR', 'RDDT'
]

# acc = MonthlyReturnsAcc(tickers = ["MSFT", "AMZN", "GOOG", "AAPL", "NFLX"])
acc = WeeklyReturnsAcc(tickers = tech_tickers)
acc.execute()