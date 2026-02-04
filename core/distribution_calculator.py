"""
Distribution Calculator - Calculate distribution of amounts across wallets
"""

class DistributionCalculator:
    """Calculate how to distribute amounts across multiple wallets"""
    
    @staticmethod
    def equal_distribution(total_amount, wallet_count):
        """
        Distribute amount equally across wallets
        
        Args:
            total_amount: Total amount to distribute
            wallet_count: Number of wallets to distribute to
            
        Returns:
            dict: Amount per wallet and any remainder
        """
        if wallet_count == 0:
            return {"per_wallet": 0.0, "remainder": total_amount}
        
        per_wallet = round(total_amount / wallet_count, 4)
        remainder = round(total_amount - (per_wallet * wallet_count), 4)
        
        return {
            "per_wallet": per_wallet,
            "remainder": remainder,
            "total": total_amount
        }
    
    @staticmethod
    def percentage_distribution(total_amount, percentages):
        """
        Distribute amount based on percentages
        
        Args:
            total_amount: Total amount to distribute
            percentages: dict of {wallet_id: percentage}
            
        Returns:
            dict: Amount per wallet
        """
        total_pct = sum(percentages.values())
        
        if abs(total_pct - 100.0) > 0.01:
            raise ValueError(f"Percentages must sum to 100%, got {total_pct}%")
        
        distribution = {}
        remaining = total_amount
        
        # Calculate amounts
        for wallet_id, pct in percentages.items():
            amount = round(total_amount * (pct / 100.0), 4)
            distribution[wallet_id] = amount
            remaining -= amount
        
        # Add any rounding remainder to first wallet
        if remaining != 0 and distribution:
            first_wallet = list(distribution.keys())[0]
            distribution[first_wallet] = round(distribution[first_wallet] + remaining, 4)
        
        return distribution
    
    @staticmethod
    def validate_percentages(percentages):
        """
        Validate that percentages are valid
        
        Args:
            percentages: dict of {wallet_id: percentage}
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not percentages:
            return False, "No percentages provided"
        
        total = sum(percentages.values())
        
        if abs(total - 100.0) > 0.01:
            return False, f"Percentages must sum to 100% (currently {total:.2f}%)"
        
        for wallet_id, pct in percentages.items():
            if pct < 0:
                return False, f"Percentage for wallet {wallet_id} cannot be negative"
            if pct > 100:
                return False, f"Percentage for wallet {wallet_id} cannot exceed 100%"
        
        return True, "Valid"
