from factors.momentum.Momentum_Weekly import Momentum_Weekly

tech_tickers = [
    'NVDA', 'AAPL', 'MSFT', 'AVGO', 'MU', 'AMD', 'INTC', 'ORCL',
    'CSCO', 'PLTR', 'AMAT', 'LRCX', 'PANW', 'DELL', 'KLAC', 'ANET',
    'TXN', 'CRWD', 'IBM', 'STX', 'APH', 'MRVL', 'ADI', 'QCOM',
    'WDC', 'CRM', 'GLW', 'NOW', 'FTNT', 'ACN', 'ADBE', 'INTU',
    'DDOG', 'CDNS', 'HPE', 'SNPS', 'MSI', 'LITE', 'MPWR', 'RDDT'
]

# signals = Momentum_Monthly(tickers = ["MSFT", "AMZN", "GOOG", "AAPL"])
signals = Momentum_Weekly(tickers = tech_tickers)
signals.execute()