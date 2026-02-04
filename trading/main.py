"""
Trading Bot Main - Main trading bot logic
"""
from .data_feed import MarketDataFeed
from .strategy import Strategy
from .broker import Broker
from .risk import calculate_position_size, calculate_stops
from .config import RISK_PER_TRADE, STOP_LOSS_PCT, INITIAL_BALANCE

class TradingBot:
    def __init__(self, bot_id, name, strategy_type="default"):
        self.bot_id = bot_id
        self.name = name
        self.market_data = MarketDataFeed()
        self.strategy = Strategy(strategy_type)
        self.broker = Broker(INITIAL_BALANCE)
        self.is_running = False
    
    def start(self):
        """Start the trading bot"""
        self.is_running = True
        print(f"Bot {self.name} started")
    
    def stop(self):
        """Stop the trading bot"""
        self.is_running = False
        print(f"Bot {self.name} stopped")
    
    def run_cycle(self):
        """Run one trading cycle"""
        if not self.is_running:
            return
        
        # Update market data
        price = self.market_data.update()
        
        # Get signal from strategy
        signal = self.strategy.analyze(self.market_data)
        
        if signal:
            # Calculate position size
            balance = self.broker.get_balance()
            position_size = calculate_position_size(balance, RISK_PER_TRADE)
            
            # Calculate stops
            stop_loss, take_profit = calculate_stops(price, STOP_LOSS_PCT)
            
            # Execute trade
            self.broker.execute_trade(signal, price, position_size / price)
    
    def get_status(self):
        """Get bot status"""
        return {
            "bot_id": self.bot_id,
            "name": self.name,
            "running": self.is_running,
            "balance": self.broker.get_balance(),
            "positions": len(self.broker.get_positions())
        }
