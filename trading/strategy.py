"""
Trading Strategy - Implements trading logic
"""

class Strategy:
    def __init__(self, name="default"):
        self.name = name
        self.signals = []
    
    def analyze(self, market_data):
        """Analyze market data and generate signals"""
        price = market_data.get_current_price()
        history = market_data.get_history()
        
        if len(history) < 20:
            return None
        
        # Simple moving average strategy
        sma_20 = sum(history[-20:]) / 20
        
        if price > sma_20 * 1.01:
            return "BUY"
        elif price < sma_20 * 0.99:
            return "SELL"
        
        return None
    
    def get_signal(self):
        """Get latest trading signal"""
        return self.signals[-1] if self.signals else None
