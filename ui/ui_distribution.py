"""
Distribution Tab - Professional distribution options
💰 Distribution
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox, QGroupBox,
    QRadioButton, QSpinBox, QDoubleSpinBox, QCheckBox, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from core.wallet_manager import WalletManager
from core.liquidity_tracker import LiquidityTracker
from core.distribution_calculator import DistributionCalculator

class DistributionTab(QWidget):
    """Distribution tab with professional options"""
    
    def __init__(self, tracker=None):
        super().__init__()
        
        self.manager = WalletManager()
        self.tracker = tracker
        self.calculator = DistributionCalculator()
        
        # Store percentage inputs for each project
        self.percentage_inputs = {}
        self.selection_checkboxes = {}
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("💰 Distribution Professionnelle")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Amount input section
        amount_group = QGroupBox("Montant à Distribuer")
        amount_layout = QHBoxLayout(amount_group)
        
        amount_layout.addWidget(QLabel("Montant total (SOL):"))
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0.0, 1000000.0)
        self.amount_input.setDecimals(4)
        self.amount_input.setValue(100.0)
        self.amount_input.setSuffix(" SOL")
        self.amount_input.valueChanged.connect(self.calculate_preview)
        amount_layout.addWidget(self.amount_input)
        amount_layout.addStretch()
        
        layout.addWidget(amount_group)
        
        # Distribution mode selection
        mode_group = QGroupBox("Mode de Distribution")
        mode_layout = QVBoxLayout(mode_group)
        
        self.equal_radio = QRadioButton("Distribution Équitable (égale entre tous)")
        self.equal_radio.setChecked(True)
        self.equal_radio.toggled.connect(self.on_mode_changed)
        mode_layout.addWidget(self.equal_radio)
        
        self.percentage_radio = QRadioButton("Distribution par Pourcentage (%)")
        self.percentage_radio.toggled.connect(self.on_mode_changed)
        mode_layout.addWidget(self.percentage_radio)
        
        layout.addWidget(mode_group)
        
        # Wallet selection section
        selection_group = QGroupBox("Sélection des Wallets")
        selection_layout = QVBoxLayout(selection_group)
        
        # Select all / deselect all buttons
        select_buttons = QHBoxLayout()
        select_all_btn = QPushButton("✓ Tout Sélectionner")
        select_all_btn.clicked.connect(self.select_all_wallets)
        select_buttons.addWidget(select_all_btn)
        
        deselect_all_btn = QPushButton("✗ Tout Désélectionner")
        deselect_all_btn.clicked.connect(self.deselect_all_wallets)
        select_buttons.addWidget(deselect_all_btn)
        select_buttons.addStretch()
        
        selection_layout.addLayout(select_buttons)
        
        # Scrollable wallet list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        self.wallets_layout = QVBoxLayout(scroll_widget)
        scroll.setWidget(scroll_widget)
        
        selection_layout.addWidget(scroll)
        layout.addWidget(selection_group)
        
        # Preview section
        preview_group = QGroupBox("Aperçu de la Distribution")
        preview_layout = QVBoxLayout(preview_group)
        
        self.preview_table = QTableWidget()
        self.preview_table.setColumnCount(4)
        self.preview_table.setHorizontalHeaderLabels([
            "Projet", "Adresse Wallet", "Montant (SOL)", "Pourcentage (%)"
        ])
        preview_layout.addWidget(self.preview_table)
        
        # Total row
        total_layout = QHBoxLayout()
        total_layout.addWidget(QLabel("Total:"))
        self.total_label = QLabel("0.0000 SOL")
        total_label_font = QFont()
        total_label_font.setBold(True)
        self.total_label.setFont(total_label_font)
        total_layout.addWidget(self.total_label)
        total_layout.addStretch()
        preview_layout.addLayout(total_layout)
        
        layout.addWidget(preview_group)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        calc_btn = QPushButton("📊 Calculer Distribution")
        calc_btn.clicked.connect(self.calculate_preview)
        button_layout.addWidget(calc_btn)
        
        execute_btn = QPushButton("✅ Exécuter Distribution")
        execute_btn.clicked.connect(self.execute_distribution)
        button_layout.addWidget(execute_btn)
        
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        # Initialize wallet list
        self.refresh_wallet_list()
    
    def refresh_wallet_list(self):
        """Refresh the list of wallets"""
        # Clear existing widgets
        while self.wallets_layout.count():
            item = self.wallets_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        self.selection_checkboxes.clear()
        self.percentage_inputs.clear()
        
        data = self.manager.load()
        
        for project in data.get("projects", []):
            if not project.get("enabled", False):
                continue
            
            wallet_widget = QWidget()
            wallet_layout = QHBoxLayout(wallet_widget)
            wallet_layout.setContentsMargins(0, 0, 0, 0)
            
            # Checkbox for selection
            checkbox = QCheckBox(f"{project['name']} (#{project['id']})")
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(self.calculate_preview)
            self.selection_checkboxes[project['id']] = checkbox
            wallet_layout.addWidget(checkbox, stretch=2)
            
            # Percentage input (only visible in percentage mode)
            pct_label = QLabel("%:")
            pct_input = QDoubleSpinBox()
            pct_input.setRange(0.0, 100.0)
            pct_input.setDecimals(2)
            pct_input.setValue(0.0)
            pct_input.setSuffix(" %")
            pct_input.valueChanged.connect(self.calculate_preview)
            pct_input.setVisible(False)
            pct_label.setVisible(False)
            
            self.percentage_inputs[project['id']] = (pct_label, pct_input)
            
            wallet_layout.addWidget(pct_label)
            wallet_layout.addWidget(pct_input, stretch=1)
            
            self.wallets_layout.addWidget(wallet_widget)
        
        self.wallets_layout.addStretch()
        self.calculate_preview()
    
    def on_mode_changed(self):
        """Handle mode change between equal and percentage"""
        is_percentage = self.percentage_radio.isChecked()
        
        # Show/hide percentage inputs
        for pct_label, pct_input in self.percentage_inputs.values():
            pct_label.setVisible(is_percentage)
            pct_input.setVisible(is_percentage)
        
        # Auto-distribute percentages equally if switching to percentage mode
        if is_percentage:
            selected = self.get_selected_projects()
            if selected:
                equal_pct = round(100.0 / len(selected), 2)
                for i, project_id in enumerate(selected):
                    pct_label, pct_input = self.percentage_inputs[project_id]
                    # Give remainder to first wallet
                    if i == 0:
                        pct_input.setValue(100.0 - (equal_pct * (len(selected) - 1)))
                    else:
                        pct_input.setValue(equal_pct)
        
        self.calculate_preview()
    
    def get_selected_projects(self):
        """Get list of selected project IDs"""
        selected = []
        for project_id, checkbox in self.selection_checkboxes.items():
            if checkbox.isChecked():
                selected.append(project_id)
        return selected
    
    def select_all_wallets(self):
        """Select all wallets"""
        for checkbox in self.selection_checkboxes.values():
            checkbox.setChecked(True)
    
    def deselect_all_wallets(self):
        """Deselect all wallets"""
        for checkbox in self.selection_checkboxes.values():
            checkbox.setChecked(False)
    
    def calculate_preview(self):
        """Calculate and display distribution preview"""
        total_amount = self.amount_input.value()
        selected = self.get_selected_projects()
        
        if not selected:
            self.preview_table.setRowCount(0)
            self.total_label.setText("0.0000 SOL")
            return
        
        data = self.manager.load()
        projects_dict = {p['id']: p for p in data.get("projects", [])}
        
        # Calculate distribution
        if self.equal_radio.isChecked():
            # Equal distribution
            result = self.calculator.equal_distribution(total_amount, len(selected))
            per_wallet = result['per_wallet']
            
            distribution = {pid: per_wallet for pid in selected}
            
            # Add remainder to first wallet
            if result['remainder'] != 0 and selected:
                distribution[selected[0]] += result['remainder']
        else:
            # Percentage distribution
            percentages = {}
            for project_id in selected:
                pct_label, pct_input = self.percentage_inputs[project_id]
                percentages[project_id] = pct_input.value()
            
            try:
                distribution = self.calculator.percentage_distribution(total_amount, percentages)
            except ValueError as e:
                QMessageBox.warning(self, "Erreur", str(e))
                return
        
        # Display in preview table
        self.preview_table.setRowCount(len(distribution))
        
        total_distributed = 0.0
        for row, (project_id, amount) in enumerate(distribution.items()):
            project = projects_dict.get(project_id, {})
            
            # Project name
            name_item = QTableWidgetItem(project.get('name', f'Project {project_id}'))
            self.preview_table.setItem(row, 0, name_item)
            
            # Wallet address
            wallet_item = QTableWidgetItem(project.get('wallet', 'N/A'))
            self.preview_table.setItem(row, 1, wallet_item)
            
            # Amount
            amount_item = QTableWidgetItem(f"{amount:.4f}")
            self.preview_table.setItem(row, 2, amount_item)
            
            # Percentage
            pct = (amount / total_amount * 100.0) if total_amount > 0 else 0.0
            pct_item = QTableWidgetItem(f"{pct:.2f}")
            self.preview_table.setItem(row, 3, pct_item)
            
            total_distributed += amount
        
        self.preview_table.resizeColumnsToContents()
        self.total_label.setText(f"{total_distributed:.4f} SOL")
    
    def execute_distribution(self):
        """Execute the distribution"""
        total_amount = self.amount_input.value()
        selected = self.get_selected_projects()
        
        if not selected:
            QMessageBox.warning(
                self,
                "Erreur",
                "Veuillez sélectionner au moins un wallet"
            )
            return
        
        if total_amount <= 0:
            QMessageBox.warning(
                self,
                "Erreur",
                "Le montant doit être supérieur à 0"
            )
            return
        
        # Confirm execution
        reply = QMessageBox.question(
            self,
            "Confirmer Distribution",
            f"Distribuer {total_amount:.4f} SOL entre {len(selected)} wallet(s)?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply != QMessageBox.StandardButton.Yes:
            return
        
        # Calculate distribution
        if self.equal_radio.isChecked():
            result = self.calculator.equal_distribution(total_amount, len(selected))
            per_wallet = result['per_wallet']
            distribution = {pid: per_wallet for pid in selected}
            if result['remainder'] != 0 and selected:
                distribution[selected[0]] += result['remainder']
        else:
            percentages = {}
            for project_id in selected:
                pct_label, pct_input = self.percentage_inputs[project_id]
                percentages[project_id] = pct_input.value()
            
            try:
                distribution = self.calculator.percentage_distribution(total_amount, percentages)
            except ValueError as e:
                QMessageBox.warning(self, "Erreur", str(e))
                return
        
        # Execute distribution (add to liquidity tracker)
        if self.tracker:
            for project_id, amount in distribution.items():
                self.tracker.add_liquidity(project_id, amount)
        
        QMessageBox.information(
            self,
            "Succès",
            f"Distribution de {total_amount:.4f} SOL exécutée avec succès!"
        )
        
        # Reset form
        self.amount_input.setValue(100.0)
        self.calculate_preview()
