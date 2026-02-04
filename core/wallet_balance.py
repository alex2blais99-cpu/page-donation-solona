"""
Wallet Balance - Tracks and manages wallet balances
"""

class WalletBalance:
    def __init__(self):
        self.balances = {}
    
    def get_balance(self, wallet_id):
        """Get balance for a specific wallet"""
        return self.balances.get(wallet_id, 0.0)
    
    def set_balance(self, wallet_id, amount):
        """Set balance for a specific wallet"""
        self.balances[wallet_id] = round(amount, 4)
    
    def add_balance(self, wallet_id, amount):
        """Add to wallet balance"""
        current = self.get_balance(wallet_id)
        self.set_balance(wallet_id, current + amount)
    
    def subtract_balance(self, wallet_id, amount):
        """Subtract from wallet balance"""
        current = self.get_balance(wallet_id)
        self.set_balance(wallet_id, current - amount)
