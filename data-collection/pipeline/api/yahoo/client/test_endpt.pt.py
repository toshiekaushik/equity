import yfinance as yf

dat = yf.Ticker("MSFT")

# get historical market data
dat.history(period='1mo')

# options
dat.option_chain(dat.options[0]).calls

# get financials
dat.balance_sheet
dat.quarterly_income_stmt

# dates
dat.calendar

print(dat.info)
print(dat.option_chain(dat.options[0]).calls)

# # websocket
# dat.live()