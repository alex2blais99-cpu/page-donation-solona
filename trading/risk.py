"""
Risk Management - Calculate position sizes and stops
"""
from .config import RISK_PER_TRADE, STOP_LOSS_PCT, TAKE_PROFIT_PCT

def calculate_position_size(balance, risk_per_trade=RISK_PER_TRADE):
    """Calculate position size based on account balance and risk"""
    return balance * risk_per_trade

def calculate_stops(entry_price, stop_loss_pct=STOP_LOSS_PCT, take_profit_pct=TAKE_PROFIT_PCT):
    """Calculate stop loss and take profit levels"""
    stop_loss = entry_price * (1 - stop_loss_pct)
    take_profit = entry_price * (1 + take_profit_pct)
    return stop_loss, take_profit

def check_risk_limits(position_size, max_position_size):
    """Check if position size exceeds limits"""
    return position_size <= max_position_size
