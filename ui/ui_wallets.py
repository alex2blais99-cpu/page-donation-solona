"""
Wallets Tab - Manage wallets and projects
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QLineEdit, QCheckBox, QMessageBox
)
from PySide6.QtCore import Qt, QTimer
from core.wallet_manager import WalletManager
from core.wallet_balance import WalletBalance
from core.price_feed import PriceFeed
from core.injection_engine import InjectionEngine
from core.risk_controller import RiskController
from core.solana_validator import is_valid_solana_address
from core.liquidity_tracker import LiquidityTracker

class WalletTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.manager = WalletManager()
        self.balance = WalletBalance()
        self.price_feed = PriceFeed()
        self.injection = InjectionEngine()
        self.risk = RiskController()
        
        data = self.manager.load()
        self.tracker = LiquidityTracker(data["projects"])
        
        layout = QVBoxLayout(self)
        
        # Title
        layout.addWidget(QLabel("💼 Gestion des Wallets"))
        
        # Table for projects
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "ID", "Projet", "Wallet", "Actif"
        ])
        
        layout.addWidget(self.table)
        
        # Controls
        controls = QHBoxLayout()
        
        self.project_input = QLineEdit()
        self.project_input.setPlaceholderText("Nom du projet")
        controls.addWidget(self.project_input)
        
        add_btn = QPushButton("Ajouter Projet")
        add_btn.clicked.connect(self.add_project)
        controls.addWidget(add_btn)
        
        layout.addLayout(controls)
        
        # Refresh
        self.refresh_table()
        
        # Auto-refresh timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_table)
        self.timer.start(2000)
    
    def refresh_table(self):
        """Refresh the projects table"""
        data = self.manager.load()
        projects = data.get("projects", [])
        
        self.table.setRowCount(len(projects))
        
        for row, project in enumerate(projects):
            # ID
            self.table.setItem(row, 0, QTableWidgetItem(str(project["id"])))
            
            # Name
            self.table.setItem(row, 1, QTableWidgetItem(project["name"]))
            
            # Wallet
            wallet = project.get("wallet", "N/A")
            self.table.setItem(row, 2, QTableWidgetItem(wallet))
            
            # Active checkbox
            checkbox = QCheckBox()
            checkbox.setChecked(project.get("enabled", False))
            checkbox.stateChanged.connect(
                lambda state, pid=project["id"]: self.toggle_project(pid, state)
            )
            self.table.setCellWidget(row, 3, checkbox)
        
        self.table.resizeColumnsToContents()
    
    def toggle_project(self, project_id, state):
        """Toggle project enabled/disabled"""
        enabled = state == Qt.CheckState.Checked.value
        self.manager.update_project(project_id, {"enabled": enabled})
    
    def add_project(self):
        """Add a new project"""
        name = self.project_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Erreur", "Entrez un nom de projet")
            return
        
        data = self.manager.load()
        new_id = max([p["id"] for p in data["projects"]]) + 1 if data["projects"] else 1
        
        new_project = {
            "id": new_id,
            "name": name,
            "wallet": f"wallet_{new_id}",
            "enabled": True
        }
        
        data["projects"].append(new_project)
        self.manager.save(data)
        
        self.project_input.clear()
        self.refresh_table()
        
        QMessageBox.information(self, "Succès", f"Projet '{name}' ajouté!")
