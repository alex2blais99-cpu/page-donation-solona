"""
Debug Checks - Verify all modules and configurations
"""
import sys

print("🔍 Vérification des modules...")

try:
    from core.wallet_manager import WalletManager
    from core.injection_engine import InjectionEngine
    from core.liquidity_tracker import LiquidityTracker
    from core.wallet_balance import WalletBalance
    from core.price_feed import PriceFeed
    from core.risk_controller import RiskController
    from core.solana_validator import is_valid_solana_address
    
    print("✅ Modules core importés avec succès")
    
    from trading.main import TradingBot
    from trading.config import BOTS
    from trading.data_feed import MarketDataFeed
    from trading.strategy import Strategy
    from trading.broker import Broker
    from trading.risk import calculate_position_size
    
    print("✅ Modules trading importés avec succès")
    
    # UI imports (may fail in headless environment)
    try:
        from ui.ui_dashboard import DashboardTab
        from ui.ui_wallets import WalletTab
        from ui.ui_qt import MainWindow
        print("✅ Modules UI importés avec succès")
    except ImportError as e:
        print(f"⚠️  Modules UI: {e}")
        print("   (Normal dans un environnement sans affichage)")
    
    # Test wallet manager
    print("\n📝 Test Wallet Manager...")
    manager = WalletManager()
    data = manager.load()
    print(f"   Projets chargés: {len(data['projects'])}")
    
    # Test liquidity tracker
    print("\n💧 Test Liquidity Tracker...")
    tracker = LiquidityTracker(data["projects"])
    print(f"   Liquidités initialisées pour {len(tracker.liquidity)} projets")
    for pid, liq in tracker.liquidity.items():
        print(f"   Projet {pid}: {liq} SOL")
    
    # Test price feed
    print("\n💰 Test Price Feed...")
    price_feed = PriceFeed()
    price = price_feed.get_price()
    print(f"   Prix SOL/CAD: {price} $")
    
    # Test solana validator
    print("\n🔐 Test Solana Validator...")
    valid_addr = "11111111111111111111111111111111"
    invalid_addr = "invalid"
    print(f"   '{valid_addr}' valide: {is_valid_solana_address(valid_addr)}")
    print(f"   '{invalid_addr}' valide: {is_valid_solana_address(invalid_addr)}")
    
    # Test trading config
    print("\n📈 Test Trading Config...")
    print(f"   Bots configurés: {len(BOTS)}")
    for bot in BOTS:
        print(f"   - {bot['name']} ({bot['strategy']}): {'Activé' if bot['enabled'] else 'Désactivé'}")
    
    print("\n✅ Tous les tests sont passés avec succès!")
    print("🚀 Vous pouvez lancer l'application avec: python launcher.py")
    
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
except Exception as e:
    print(f"❌ Erreur lors des tests: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
