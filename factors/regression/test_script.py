from factors.regression.Momentum_Weekly_Regression import Momentum_Weekly_Regression

tech_tickers = [
    'NVDA', 'AAPL', 'MSFT', 'AVGO', 'MU', 'AMD', 'INTC', 'ORCL',
    'CSCO', 'PLTR', 'AMAT', 'LRCX', 'PANW', 'DELL', 'KLAC', 'ANET',
    'TXN', 'CRWD', 'IBM', 'STX', 'APH', 'MRVL', 'ADI', 'QCOM',
    'WDC', 'CRM', 'GLW', 'NOW', 'FTNT', 'ACN', 'ADBE', 'INTU',
    'DDOG', 'CDNS', 'HPE', 'SNPS', 'MSI', 'LITE', 'MPWR', 'RDDT'
]

regression = Momentum_Weekly_Regression(tickers = tech_tickers)
regression.execute()