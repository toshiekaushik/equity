from CoreConsts import TECH_TICKERS
from data.collector.dal.db.postgress.FactorPG import FactorPG
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG

time_returns = TimeReturnsPG()
factor_db = FactorPG()
# returns = time_returns.get_returns("2026-08-10", "2026-08-15", TECH_TICKERS)
momentum = factor_db.get_momentum_weekly("2026-08-10", "2026-08-15", TECH_TICKERS)
reversal = factor_db.get_reversal_weekly("2026-08-10", "2026-08-15", TECH_TICKERS)
volatility = factor_db.get_volatility_20_days("2026-08-10", "2026-08-15", TECH_TICKERS)
alpha_model = time_returns.execute_query(
    """
    select * from first_alpha_model where version = 'v2';
    """
)

# 1. Merge momentum and reversal on ticker and date
filtered_df = momentum.merge(reversal[["ticker", "date", "reversal_chg"]], on=["ticker", "date"], how="inner")
filtered_df = filtered_df.merge(volatility[["ticker", "date", "volatility"]], on=["ticker", "date"], how="inner")

# 3. Extract scalar coefficients from alpha_model safely
a_rev = alpha_model["reversal"].iloc[0]
a_mom4 = alpha_model["momentum4"].iloc[0]
a_mom12 = alpha_model["momentum12"].iloc[0]
a_vol = alpha_model["volatility"].iloc[0]
intercept = alpha_model["intercept"].iloc[0]
# print(filtered_df)
# 4. Calculate expected returns across the whole table instantly
filtered_df["predicted_return"] = (
    (a_rev * filtered_df["reversal_chg"]) +
    (a_mom4 * filtered_df["mom_4_1"]) +
    (a_mom12 * filtered_df["mom_12_1"]) +
    (a_vol * filtered_df["volatility"]) +
    intercept
)

print("Expected Return: ", (1/len(TECH_TICKERS)) * filtered_df["predicted_return"].sum())