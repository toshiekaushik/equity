from CoreConsts import TECH_TICKERS
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG

time_returns = TimeReturnsPG()

# alpha_tester_data = WeeklyReturnsAcc(tickers = TECH_TICKERS)
# alpha_tester_data.execute()

returns = time_returns.get_returns_v2("2026-08-14", "2026-08-26", TECH_TICKERS, "alpha_tester_v1")
returns.sort_values(['ticker', 'date'])
returns["pct_change"] = (
    returns.groupby("ticker")["close"].pct_change()
)

returns.dropna()
print("Expected Return: ", (1/len(TECH_TICKERS)) * returns["pct_change"].sum())