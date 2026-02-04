"""
Broker - Executes trades
"""

class Broker:
    def __init__(self, initial_balance=10000.0):
        self.balance = initial_balance
        self.positions = []
        self.trades = []
    
    def execute_trade(self, signal, price, size):
        """Execute a trade based on signal"""
        if signal == "BUY" and self.balance >= price * size:
            self.balance -= price * size
            self.positions.append({"type": "LONG", "price": price, "size": size})
            self.trades.append({"action": "BUY", "price": price, "size": size})
            return True
        elif signal == "SELL" and self.positions:
            # Close position
            position = self.positions.pop(0)
            profit = (price - position["price"]) * position["size"]
            self.balance += price * position["size"]
            self.trades.append({"action": "SELL", "price": price, "size": position["size"], "profit": profit})
            return True
        return False
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def get_positions(self):
        """Get open positions"""
        return self.positions.copy()
