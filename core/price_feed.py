"""
Price Feed - Provides price data for SOL/CAD
"""
import random

class PriceFeed:
    def __init__(self, initial_price=200.0):
        """Initialize price feed with starting price"""
        self.price = initial_price
    
    def update(self):
        """Update and return current price (simulated)"""
        # Simulate price changes (±1% variation)
        variation = random.uniform(-0.01, 0.01)
        self.price = self.price * (1 + variation)
        return round(self.price, 2)
    
    def get_price(self):
        """Get current price without updating"""
        return round(self.price, 2)
