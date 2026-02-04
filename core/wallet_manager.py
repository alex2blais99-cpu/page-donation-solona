"""
Wallet Manager - Manages wallets and projects configuration
"""
import json
from pathlib import Path

class WalletManager:
    def __init__(self, filepath="wallets.json"):
        self.filepath = Path(filepath)
        
    def load(self):
        """Load wallet configuration from JSON file"""
        if not self.filepath.exists():
            # Create default structure with 12 projects
            default_data = {
                "projects": [
                    {"id": i, "name": f"Projet {i}", "enabled": True, "wallet": f"wallet_{i}"}
                    for i in range(1, 13)
                ]
            }
            self.save(default_data)
            return default_data
        
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save(self, data):
        """Save wallet configuration to JSON file"""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_project(self, project_id):
        """Get a specific project by ID"""
        data = self.load()
        for project in data["projects"]:
            if project["id"] == project_id:
                return project
        return None
    
    def update_project(self, project_id, updates):
        """Update a project's properties"""
        data = self.load()
        for project in data["projects"]:
            if project["id"] == project_id:
                project.update(updates)
                break
        self.save(data)
