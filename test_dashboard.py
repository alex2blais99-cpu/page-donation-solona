"""
Test Dashboard Functionality - Without GUI
Demonstrates dashboard functionality in headless mode
"""
from core.wallet_manager import WalletManager
from core.liquidity_tracker import LiquidityTracker
from core.price_feed import PriceFeed

def test_dashboard():
    """Test dashboard components"""
    print("=" * 60)
    print("🧪 Test Dashboard Functionality")
    print("=" * 60)
    
    # Initialize components
    print("\n1️⃣ Initializing components...")
    manager = WalletManager()
    data = manager.load()
    price_feed = PriceFeed()
    tracker = LiquidityTracker(data["projects"])
    
    print(f"   ✅ Loaded {len(data['projects'])} projects")
    print(f"   ✅ Initialized liquidity tracker")
    print(f"   ✅ Initialized price feed")
    
    # Display dashboard data
    print("\n2️⃣ Dashboard Display (as it would appear in UI):")
    print("-" * 60)
    print(f"{'ID':<5} {'Projet':<15} {'Actif':<8} {'SOL':<12} {'CAD':<10}")
    print("-" * 60)
    
    price = price_feed.get_price()
    
    for project in data["projects"]:
        project_id = project["id"]
        name = project["name"]
        enabled = "✅" if project["enabled"] else "❌"
        sol = tracker.get_liquidity(project_id)
        cad = round(sol * price, 2)
        
        print(f"{project_id:<5} {name:<15} {enabled:<8} {sol:<12.4f} {cad:<10.2f} $")
    
    print("-" * 60)
    
    # Test adding liquidity
    print("\n3️⃣ Testing liquidity injection:")
    print("   Adding 10.5 SOL to Projet 1...")
    tracker.add_liquidity(1, 10.5)
    
    print("   Adding 5.25 SOL to Projet 3...")
    tracker.add_liquidity(3, 5.25)
    
    print("   Adding 20.0 SOL to Projet 5...")
    tracker.add_liquidity(5, 20.0)
    
    # Display updated data
    print("\n4️⃣ Updated Dashboard Display:")
    print("-" * 60)
    print(f"{'ID':<5} {'Projet':<15} {'Actif':<8} {'SOL':<12} {'CAD':<10}")
    print("-" * 60)
    
    for project in data["projects"]:
        project_id = project["id"]
        name = project["name"]
        enabled = "✅" if project["enabled"] else "❌"
        sol = tracker.get_liquidity(project_id)
        cad = round(sol * price, 2)
        
        print(f"{project_id:<5} {name:<15} {enabled:<8} {sol:<12.4f} {cad:<10.2f} $")
    
    print("-" * 60)
    
    # Calculate totals
    total_sol = sum(tracker.get_all_liquidity().values())
    total_cad = round(total_sol * price, 2)
    
    print(f"\n{'TOTAL':<29} {total_sol:<12.4f} {total_cad:<10.2f} $")
    print("-" * 60)
    
    print("\n✅ Dashboard test completed successfully!")
    print("\n📊 Summary:")
    print(f"   • Total projects: {len(data['projects'])}")
    print(f"   • Active projects: {sum(1 for p in data['projects'] if p['enabled'])}")
    print(f"   • Total liquidity: {total_sol:.4f} SOL (${total_cad} CAD)")
    print(f"   • SOL/CAD price: ${price}")
    print(f"   • Projects with liquidity: {sum(1 for v in tracker.get_all_liquidity().values() if v > 0)}")

if __name__ == "__main__":
    test_dashboard()
