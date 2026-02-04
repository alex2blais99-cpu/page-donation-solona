"""
Launcher - Main entry point for the application
"""
import sys
from ui.ui_qt import main

if __name__ == "__main__":
    print("🚀 Démarrage de l'application AutoTrading Bot...")
    print("📊 Chargement de l'interface...")
    
    try:
        main()
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
