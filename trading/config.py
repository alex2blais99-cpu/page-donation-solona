"""
Trading Configuration
"""

# Initial prices and balances
START_PRICE = 200.0
INITIAL_BALANCE = 10000.0

# Risk management
RISK_PER_TRADE = 0.02  # 2% risk per trade
STOP_LOSS_PCT = 0.05   # 5% stop loss
TAKE_PROFIT_PCT = 0.10 # 10% take profit

# Bot configurations
BOTS = [
    {"id": 1, "name": "Bot Scalper", "strategy": "scalping", "enabled": True},
    {"id": 2, "name": "Bot Trend", "strategy": "trend_following", "enabled": True},
    {"id": 3, "name": "Bot Mean Reversion", "strategy": "mean_reversion", "enabled": False},
]
