"""
Main UI Application - Qt Interface
"""
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget,
    QVBoxLayout, QLabel, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont
import sys
from trading.main import TradingBot
from trading.config import BOTS
from ui.ui_wallets import WalletTab
from ui.ui_dashboard import DashboardTab
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("AutoTrading Bot - Solana Donation Tracker")
        self.setMinimumSize(1000, 700)
        
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        
        layout = QVBoxLayout(central)
        
        # Title
        title = QLabel("🚀 AutoTrading Bot - Solana")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Tab widget
        self.tabs = QTabWidget()
        
        # Add Dashboard tab (first)
        self.tabs.addTab(DashboardTab(), "📊 Dashboard")
        
        # Add Wallets tab
        self.tabs.addTab(WalletTab(), "💼 Wallets")
        
        # Add Trading tab
        self.tabs.addTab(self.create_trading_tab(), "📈 Trading")
        
        layout.addWidget(self.tabs)
        
        # Load stylesheet if exists
        self.load_stylesheet()
    
    def create_trading_tab(self):
        """Create trading tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        layout.addWidget(QLabel("📈 Trading Bots"))
        
        # Bot controls
        for bot_config in BOTS:
            bot_label = QLabel(f"Bot: {bot_config['name']} ({bot_config['strategy']})")
            layout.addWidget(bot_label)
            
            btn = QPushButton("Start Bot" if bot_config["enabled"] else "Bot Disabled")
            btn.setEnabled(bot_config["enabled"])
            layout.addWidget(btn)
        
        layout.addStretch()
        
        return widget
    
    def load_stylesheet(self):
        """Load CSS stylesheet if exists"""
        css_path = Path("ui/styles.css")
        if css_path.exists():
            with open(css_path, 'r', encoding='utf-8') as f:
                self.setStyleSheet(f.read())

def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
