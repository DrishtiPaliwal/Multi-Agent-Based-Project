import re

def normalize_price(price):
    if price:
        price = re.sub(r"[^\d.]", "", str(price))
        return float(price)
    return 0.0


def format_currency(amount, symbol="₹"):
    """Format price with currency symbol."""
    return f"{symbol}{amount:,.2f}"
