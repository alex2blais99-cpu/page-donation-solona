"""
Settings Tab - Manage application settings and wallet parameters
⚙️ Paramètres
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox, QDialog,
    QDialogButtonBox, QFormLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from core.wallet_manager import WalletManager
from core.solana_validator import is_valid_solana_address

class EditProjectDialog(QDialog):
    """Dialog for editing project details"""
    
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.project = project
        self.setWindowTitle(f"Modifier Projet #{project['id']}")
        self.setMinimumWidth(500)
        
        layout = QFormLayout(self)
        
        # Project name
        self.name_input = QLineEdit(project['name'])
        layout.addRow("Nom du projet:", self.name_input)
        
        # Wallet address
        self.wallet_input = QLineEdit(project.get('wallet', ''))
        layout.addRow("Adresse Wallet:", self.wallet_input)
        
        # Buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.validate_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)
    
    def validate_and_accept(self):
        """Validate inputs before accepting"""
        name = self.name_input.text().strip()
        wallet = self.wallet_input.text().strip()
        
        if not name:
            QMessageBox.warning(self, "Erreur", "Le nom du projet ne peut pas être vide")
            return
        
        if wallet and not is_valid_solana_address(wallet):
            reply = QMessageBox.question(
                self,
                "Adresse invalide",
                "L'adresse Solana semble invalide. Continuer quand même?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
        
        self.accept()
    
    def get_values(self):
        """Get the edited values"""
        return {
            'name': self.name_input.text().strip(),
            'wallet': self.wallet_input.text().strip()
        }


class SettingsTab(QWidget):
    """Settings tab for managing wallet parameters"""
    
    def __init__(self):
        super().__init__()
        
        self.manager = WalletManager()
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("⚙️ Paramètres de l'Application")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Modifier les adresses des wallets, renommer les projets, etc.")
        layout.addWidget(subtitle)
        
        # Table for projects
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "ID", "Projet", "Adresse Wallet", "Actions", "Supprimer"
        ])
        
        layout.addWidget(self.table)
        
        # Refresh button
        refresh_layout = QHBoxLayout()
        refresh_btn = QPushButton("🔄 Actualiser")
        refresh_btn.clicked.connect(self.refresh_table)
        refresh_layout.addWidget(refresh_btn)
        refresh_layout.addStretch()
        layout.addLayout(refresh_layout)
        
        # Initial refresh
        self.refresh_table()
    
    def refresh_table(self):
        """Refresh the projects table"""
        data = self.manager.load()
        projects = data.get("projects", [])
        
        self.table.setRowCount(len(projects))
        
        for row, project in enumerate(projects):
            # ID
            id_item = QTableWidgetItem(str(project["id"]))
            id_item.setFlags(id_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 0, id_item)
            
            # Name
            name_item = QTableWidgetItem(project["name"])
            name_item.setFlags(name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 1, name_item)
            
            # Wallet address
            wallet = project.get("wallet", "N/A")
            wallet_item = QTableWidgetItem(wallet)
            wallet_item.setFlags(wallet_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 2, wallet_item)
            
            # Edit button
            edit_btn = QPushButton("✏️ Modifier")
            edit_btn.clicked.connect(
                lambda checked, p=project: self.edit_project(p)
            )
            self.table.setCellWidget(row, 3, edit_btn)
            
            # Delete button
            delete_btn = QPushButton("🗑️ Supprimer")
            delete_btn.clicked.connect(
                lambda checked, pid=project["id"]: self.delete_project(pid)
            )
            self.table.setCellWidget(row, 4, delete_btn)
        
        self.table.resizeColumnsToContents()
    
    def edit_project(self, project):
        """Open dialog to edit project"""
        dialog = EditProjectDialog(project, self)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            values = dialog.get_values()
            self.manager.update_project(project['id'], values)
            self.refresh_table()
            QMessageBox.information(
                self,
                "Succès",
                f"Projet '{values['name']}' mis à jour!"
            )
    
    def delete_project(self, project_id):
        """Delete a project"""
        reply = QMessageBox.question(
            self,
            "Confirmer la suppression",
            f"Êtes-vous sûr de vouloir supprimer le projet #{project_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            data = self.manager.load()
            data["projects"] = [p for p in data["projects"] if p["id"] != project_id]
            self.manager.save(data)
            self.refresh_table()
            QMessageBox.information(
                self,
                "Succès",
                f"Projet #{project_id} supprimé!"
            )
