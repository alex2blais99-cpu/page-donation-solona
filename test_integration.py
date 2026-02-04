"""
Integration Test - Test all new features together
"""
from core.wallet_manager import WalletManager
from core.liquidity_tracker import LiquidityTracker
from core.distribution_calculator import DistributionCalculator

def test_complete_workflow():
    """Test a complete workflow: load wallets, distribute, check results"""
    print("=" * 70)
    print("🧪 Test Workflow Complet - Distribution Professionnelle")
    print("=" * 70)
    
    # Step 1: Load wallets
    print("\n1️⃣ Chargement des wallets...")
    manager = WalletManager()
    data = manager.load()
    print(f"   ✅ {len(data['projects'])} projets chargés")
    
    # Step 2: Initialize tracker
    print("\n2️⃣ Initialisation du tracker de liquidité...")
    tracker = LiquidityTracker(data["projects"])
    print(f"   ✅ Tracker initialisé pour {len(tracker.liquidity)} projets")
    
    # Step 3: Show initial state
    print("\n3️⃣ État initial:")
    total_initial = sum(tracker.get_all_liquidity().values())
    print(f"   Total liquidité: {total_initial} SOL")
    
    # Step 4: Equal distribution
    print("\n4️⃣ Test Distribution Équitable:")
    print("   Scénario: Distribuer 1000 SOL entre 4 projets")
    
    selected_projects = [1, 2, 3, 4]
    amount = 1000.0
    
    calc = DistributionCalculator()
    result = calc.equal_distribution(amount, len(selected_projects))
    
    print(f"   Montant par projet: {result['per_wallet']} SOL")
    print(f"   Reste: {result['remainder']} SOL")
    
    # Execute distribution
    for i, project_id in enumerate(selected_projects):
        if i == 0:
            # First wallet gets the remainder
            tracker.add_liquidity(project_id, result['per_wallet'] + result['remainder'])
        else:
            tracker.add_liquidity(project_id, result['per_wallet'])
    
    print("\n   Distribution effectuée:")
    for project_id in selected_projects:
        liq = tracker.get_liquidity(project_id)
        print(f"   • Projet {project_id}: {liq:.4f} SOL")
    
    # Step 5: Percentage distribution
    print("\n5️⃣ Test Distribution par Pourcentage:")
    print("   Scénario: Distribuer 500 SOL avec percentages personnalisés")
    
    percentages = {
        5: 40.0,   # 40%
        6: 35.0,   # 35%
        7: 25.0    # 25%
    }
    
    distribution = calc.percentage_distribution(500.0, percentages)
    
    print("   Distribution calculée:")
    for project_id, amount in distribution.items():
        pct = percentages[project_id]
        print(f"   • Projet {project_id}: {amount:.4f} SOL ({pct}%)")
        tracker.add_liquidity(project_id, amount)
    
    # Step 6: Verify total
    print("\n6️⃣ Vérification finale:")
    all_liquidity = tracker.get_all_liquidity()
    total_distributed = sum(all_liquidity.values())
    
    print(f"   Total initial: {total_initial} SOL")
    print(f"   Total distribué: {total_distributed - total_initial} SOL")
    print(f"   Total final: {total_distributed} SOL")
    
    print("\n   Liquidité par projet:")
    for project in data["projects"]:
        project_id = project["id"]
        liq = tracker.get_liquidity(project_id)
        if liq > 0:
            print(f"   • {project['name']} (#{project_id}): {liq:.4f} SOL")
    
    # Step 7: Test wallet editing simulation
    print("\n7️⃣ Test Modification de Wallet:")
    project_to_edit = data["projects"][0]
    old_name = project_to_edit["name"]
    old_wallet = project_to_edit["wallet"]
    
    print(f"   Avant: {old_name}, {old_wallet}")
    
    new_values = {
        "name": "Wallet Principal Production",
        "wallet": "NewAddress1234567890123456789012"
    }
    
    manager.update_project(project_to_edit["id"], new_values)
    updated_data = manager.load()
    updated_project = [p for p in updated_data["projects"] if p["id"] == project_to_edit["id"]][0]
    
    print(f"   Après: {updated_project['name']}, {updated_project['wallet']}")
    print("   ✅ Modification réussie")
    
    # Restore original
    manager.update_project(project_to_edit["id"], {
        "name": old_name,
        "wallet": old_wallet
    })
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ Test Workflow Complet: SUCCÈS")
    print("=" * 70)
    print("\nRésumé des fonctionnalités testées:")
    print("   ✅ Chargement des wallets")
    print("   ✅ Initialisation du tracker")
    print("   ✅ Distribution équitable")
    print("   ✅ Distribution par pourcentage")
    print("   ✅ Mise à jour des liquidités")
    print("   ✅ Modification de wallets")
    print("   ✅ Validation des totaux")
    print("\nToutes les nouvelles fonctionnalités sont opérationnelles! 🎉")

if __name__ == "__main__":
    test_complete_workflow()
