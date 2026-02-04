"""
Market Data Feed - Provides market data for trading
"""
import random
from .config import START_PRICE

class MarketDataFeed:
    def __init__(self):
        self.price = START_PRICE
        self.history = [START_PRICE]
    
    def update(self):
        """Update price with simulated market movement"""
        # Simulate price changes
        change = random.uniform(-0.02, 0.02)
        self.price = self.price * (1 + change)
        self.history.append(self.price)
        return self.price
    
    def get_current_price(self):
        """Get current market price"""
        return self.price
    
    def get_history(self, bars=100):
        """Get price history"""
        return self.history[-bars:]
