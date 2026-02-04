"""
Risk Controller - Manages risk parameters and limits
"""

class RiskController:
    def __init__(self, max_risk_per_project=100.0):
        self.max_risk_per_project = max_risk_per_project
        self.risk_levels = {}
    
    def check_risk(self, project_id, amount):
        """Check if injection amount exceeds risk limits"""
        current_risk = self.risk_levels.get(project_id, 0.0)
        if current_risk + amount > self.max_risk_per_project:
            return False
        return True
    
    def update_risk(self, project_id, amount):
        """Update risk level for a project"""
        current = self.risk_levels.get(project_id, 0.0)
        self.risk_levels[project_id] = current + amount
    
    def get_risk_level(self, project_id):
        """Get current risk level for a project"""
        return self.risk_levels.get(project_id, 0.0)
