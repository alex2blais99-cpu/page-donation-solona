"""
Installation Script - Install dependencies
"""
import subprocess
import sys

def install_dependencies():
    """Install required packages"""
    print("📦 Installation des dépendances...")
    
    try:
        # Upgrade pip
        print("⬆️  Mise à jour de pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Install requirements
        print("📥 Installation des packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("✅ Installation terminée avec succès!")
        print("🚀 Vous pouvez maintenant lancer l'application avec: python launcher.py")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
