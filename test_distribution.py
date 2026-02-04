"""
Test Distribution Calculator - Test distribution logic
"""
from core.distribution_calculator import DistributionCalculator

def test_equal_distribution():
    """Test equal distribution"""
    print("=" * 60)
    print("🧪 Test Equal Distribution")
    print("=" * 60)
    
    calc = DistributionCalculator()
    
    # Test 1: Distribute 100 SOL among 3 wallets
    print("\n1️⃣ Test: 100 SOL among 3 wallets")
    result = calc.equal_distribution(100.0, 3)
    print(f"   Per wallet: {result['per_wallet']} SOL")
    print(f"   Remainder: {result['remainder']} SOL")
    print(f"   Total: {result['total']} SOL")
    
    # Test 2: Distribute 10 SOL among 12 wallets
    print("\n2️⃣ Test: 10 SOL among 12 wallets")
    result = calc.equal_distribution(10.0, 12)
    print(f"   Per wallet: {result['per_wallet']} SOL")
    print(f"   Remainder: {result['remainder']} SOL")
    print(f"   Total: {result['total']} SOL")
    
    # Test 3: Zero wallets
    print("\n3️⃣ Test: 100 SOL among 0 wallets")
    result = calc.equal_distribution(100.0, 0)
    print(f"   Per wallet: {result['per_wallet']} SOL")
    print(f"   Remainder: {result['remainder']} SOL")

def test_percentage_distribution():
    """Test percentage distribution"""
    print("\n" + "=" * 60)
    print("🧪 Test Percentage Distribution")
    print("=" * 60)
    
    calc = DistributionCalculator()
    
    # Test 1: Valid percentages
    print("\n1️⃣ Test: 100 SOL with valid percentages")
    percentages = {
        1: 50.0,   # 50%
        2: 30.0,   # 30%
        3: 20.0    # 20%
    }
    result = calc.percentage_distribution(100.0, percentages)
    for wallet_id, amount in result.items():
        print(f"   Wallet {wallet_id}: {amount} SOL ({percentages[wallet_id]}%)")
    
    # Test 2: Invalid percentages (don't sum to 100%)
    print("\n2️⃣ Test: Invalid percentages (sum != 100%)")
    percentages = {
        1: 50.0,
        2: 30.0,
        3: 15.0   # Total = 95%
    }
    try:
        result = calc.percentage_distribution(100.0, percentages)
    except ValueError as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Complex percentages
    print("\n3️⃣ Test: 1000 SOL with complex percentages")
    percentages = {
        1: 25.5,
        2: 18.3,
        3: 32.1,
        4: 24.1
    }
    result = calc.percentage_distribution(1000.0, percentages)
    total = 0
    for wallet_id, amount in result.items():
        print(f"   Wallet {wallet_id}: {amount} SOL ({percentages[wallet_id]}%)")
        total += amount
    print(f"   Total distributed: {total} SOL")

def test_validate_percentages():
    """Test percentage validation"""
    print("\n" + "=" * 60)
    print("🧪 Test Percentage Validation")
    print("=" * 60)
    
    calc = DistributionCalculator()
    
    # Test 1: Valid
    print("\n1️⃣ Test: Valid percentages")
    percentages = {1: 60.0, 2: 40.0}
    valid, msg = calc.validate_percentages(percentages)
    print(f"   Valid: {valid}, Message: {msg}")
    
    # Test 2: Sum > 100%
    print("\n2️⃣ Test: Sum > 100%")
    percentages = {1: 60.0, 2: 50.0}
    valid, msg = calc.validate_percentages(percentages)
    print(f"   Valid: {valid}, Message: {msg}")
    
    # Test 3: Negative percentage
    print("\n3️⃣ Test: Negative percentage")
    percentages = {1: 120.0, 2: -20.0}
    valid, msg = calc.validate_percentages(percentages)
    print(f"   Valid: {valid}, Message: {msg}")
    
    # Test 4: Empty
    print("\n4️⃣ Test: Empty percentages")
    percentages = {}
    valid, msg = calc.validate_percentages(percentages)
    print(f"   Valid: {valid}, Message: {msg}")

def main():
    """Run all tests"""
    test_equal_distribution()
    test_percentage_distribution()
    test_validate_percentages()
    
    print("\n" + "=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
