"""
Liquidity Tracker - Tracks liquidity for all projects
Source unique de vérité pour les liquidités
"""

class LiquidityTracker:
    def __init__(self, projects):
        """Initialize liquidity tracker with projects list"""
        self.liquidity = {
            p["id"]: 0.0 for p in projects
        }

    def get_liquidity(self, project_id):
        """Get current liquidity for a project"""
        return self.liquidity.get(project_id, 0.0)

    def set_liquidity(self, project_id, amount):
        """Set liquidity for a project"""
        self.liquidity[project_id] = round(amount, 4)

    def add_liquidity(self, project_id, amount):
        """Add liquidity to a project"""
        current = self.get_liquidity(project_id)
        self.set_liquidity(project_id, current + amount)
    
    def get_all_liquidity(self):
        """Get all liquidity data"""
        return self.liquidity.copy()
