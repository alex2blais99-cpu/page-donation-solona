"""
Solana Validator - Validates Solana addresses
"""
import re

def is_valid_solana_address(address):
    """
    Validate if a string is a valid Solana address
    Solana addresses are base58 encoded and typically 32-44 characters
    """
    if not address or not isinstance(address, str):
        return False
    
    # Basic validation: check length and allowed characters
    if len(address) < 32 or len(address) > 44:
        return False
    
    # Solana addresses use base58 encoding (no 0, O, I, l)
    base58_pattern = r'^[1-9A-HJ-NP-Za-km-z]+$'
    if not re.match(base58_pattern, address):
        return False
    
    return True
