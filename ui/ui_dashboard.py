"""
Dashboard Tab - Shows project status and liquidity
📊 Dashboard — Projets & Liquidité
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont, QColor
from core.wallet_manager import WalletManager
from core.liquidity_tracker import LiquidityTracker
from core.price_feed import PriceFeed

class DashboardTab(QWidget):
    def __init__(self, tracker=None):
        super().__init__()

        self.manager = WalletManager()
        self.data = self.manager.load()

        self.price_feed = PriceFeed()
        
        # Use provided tracker or create new one
        if tracker:
            self.tracker = tracker
        else:
            self.tracker = LiquidityTracker(self.data["projects"])

        layout = QVBoxLayout(self)

        # Title
        title = QLabel("📊 Dashboard — Projets & Liquidité")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "ID", "Projet", "Actif", "Liquidité (SOL)", "Valeur (CAD)"
        ])

        layout.addWidget(self.table)

        # Initial refresh
        self.refresh()
        
        # Auto-refresh timer (every 1 second)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def refresh(self):
        """Refresh dashboard data"""
        data = self.manager.load()
        price = self.price_feed.update()

        self.table.setRowCount(len(data["projects"]))

        for row, project in enumerate(data["projects"]):
            sol = self.tracker.get_liquidity(project["id"])
            cad = round(sol * price, 2)

            # ID
            id_item = QTableWidgetItem(str(project["id"]))
            self.table.setItem(row, 0, id_item)
            
            # Project name
            name_item = QTableWidgetItem(project["name"])
            self.table.setItem(row, 1, name_item)
            
            # Active status
            status_item = QTableWidgetItem("✅" if project["enabled"] else "❌")
            self.table.setItem(row, 2, status_item)
            
            # SOL liquidity
            sol_item = QTableWidgetItem(f"{sol:.4f}")
            self.table.setItem(row, 3, sol_item)
            
            # CAD value
            cad_item = QTableWidgetItem(f"{cad:.2f} $")
            self.table.setItem(row, 4, cad_item)

        self.table.resizeColumnsToContents()
