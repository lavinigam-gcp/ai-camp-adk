# Lab 2 Tools: Custom tools for the Multi-Tool Assistant

import random
import requests
from datetime import datetime
from typing import Dict, Any

def calculate_tip(bill_amount: float, tip_percentage: float = 15.0) -> Dict[str, Any]:
    """
    Calculate tip amount and total bill.

    Args:
        bill_amount: The original bill amount in dollars
        tip_percentage: Tip percentage (default 15%)

    Returns:
        Dictionary with tip amount and total bill
    """
    tip_amount = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip_amount

    return {
        "original_bill": f"${bill_amount:.2f}",
        "tip_percentage": f"{tip_percentage}%",
        "tip_amount": f"${tip_amount:.2f}",
        "total_amount": f"${total:.2f}",
        "per_person_2": f"${total/2:.2f}",
        "per_person_3": f"${total/3:.2f}",
        "per_person_4": f"${total/4:.2f}"
    }

def get_random_quote() -> Dict[str, Any]:
    """
    Get an inspirational quote from a free API.
    Uses the Quotable API which doesn't require an API key.

    Returns:
        Dictionary with quote information
    """
    try:
        # Free API that doesn't require authentication
        response = requests.get("https://api.quotable.io/random", timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "quote": data.get("content", ""),
                "author": data.get("author", "Unknown"),
                "length": data.get("length", 0),
                "tags": data.get("tags", []),
                "source": "Quotable API",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            return {
                "error": f"API returned status code: {response.status_code}",
                "quote": "The only way to do great work is to love what you do.",
                "author": "Steve Jobs",
                "source": "Fallback quote",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    except Exception as e:
        return {
            "error": f"Failed to fetch quote: {str(e)}",
            "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "author": "Winston Churchill",
            "source": "Fallback quote",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def convert_currency(amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
    """
    Convert currency from one type to another.
    Using simplified fixed rates for demo purposes.

    Args:
        amount: Amount to convert
        from_currency: Source currency code (USD, EUR, GBP, JPY)
        to_currency: Target currency code

    Returns:
        Dictionary with conversion details
    """
    # Simplified exchange rates (relative to USD)
    rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.73,
        "JPY": 110.0,
        "CAD": 1.25,
        "AUD": 1.35,
        "CHF": 0.91,
        "CNY": 7.2
    }

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        return {
            "error": f"Currency not supported. Supported: {', '.join(rates.keys())}"
        }

    # Convert to USD first, then to target currency
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]

    return {
        "original_amount": f"{amount:.2f} {from_currency}",
        "converted_amount": f"{converted_amount:.2f} {to_currency}",
        "exchange_rate": f"1 {from_currency} = {rates[to_currency]/rates[from_currency]:.4f} {to_currency}",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "note": "Rates are simplified for demo purposes"
    }

def generate_password(length: int = 12, include_symbols: bool = True) -> Dict[str, Any]:
    """
    Generate a secure random password.

    Args:
        length: Password length (default 12)
        include_symbols: Whether to include special characters

    Returns:
        Dictionary with password and strength information
    """
    import string

    if length < 4:
        length = 4
    elif length > 50:
        length = 50

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if include_symbols else ""

    # Ensure at least one character from each set
    password_chars = [
        random.choice(string.ascii_lowercase),  # lowercase
        random.choice(string.ascii_uppercase),  # uppercase
        random.choice(digits),                  # digit
    ]

    if include_symbols:
        password_chars.append(random.choice(symbols))

    # Fill remaining length with random characters
    all_chars = letters + digits + symbols
    for _ in range(length - len(password_chars)):
        password_chars.append(random.choice(all_chars))

    # Shuffle the password
    random.shuffle(password_chars)
    password = ''.join(password_chars)

    # Calculate strength
    strength = "Weak"
    if length >= 8 and include_symbols:
        strength = "Strong"
    elif length >= 6:
        strength = "Medium"

    return {
        "password": password,
        "length": length,
        "strength": strength,
        "includes_symbols": include_symbols,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "security_tip": "Store this password in a secure password manager"
    }