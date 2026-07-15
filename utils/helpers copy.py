# import re
# import difflib

import re

def normalize_price(price):
    if price:
        price = re.sub(r"[^\d.]", "", str(price))
        return float(price)
    return 0.0


def format_currency(amount):
    return f"₹{amount:,.2f}"

# def normalize_price(price_str: str) -> float:
#     """Strip currency symbols, commas, spaces and return float."""
#     if not price_str or price_str == 'None':
#         return 0.0
#     try:
#         # Remove currency symbols and commas
#         cleaned = re.sub(r'[₹$€£,\s]', '', str(price_str))
#         return float(cleaned)
#     except (ValueError, TypeError):
#         return 0.0

# def normalize_rating(rating_str: str) -> float:
#     """Parse rating to float, clamp 0-5."""
#     if not rating_str or rating_str == 'None':
#         return 0.0
#     try:
#         # Extract the first float-like pattern if there is extra text
#         match = re.search(r'\d+(\.\d+)?', str(rating_str))
#         if match:
#             val = float(match.group())
#             return max(0.0, min(5.0, val))
#         return 0.0
#     except (ValueError, TypeError):
#         return 0.0

# def deduplicate_products(products: list) -> list:
#     """Remove duplicate products based on normalized name fuzzy match.
    
#     If two products match closely and have the same source, keep the one with the lower price.
#     """
#     unique_products = []
    
#     for prod in products:
#         prod_name = prod.get('name', '').lower().strip()
#         prod_source = prod.get('source', '')
#         prod_price = prod.get('price', 0.0)
        
#         is_duplicate = False
#         for i, existing in enumerate(unique_products):
#             existing_name = existing.get('name', '').lower().strip()
#             existing_source = existing.get('source', '')
            
#             # Check source match and fuzzy name match
#             if prod_source == existing_source:
#                 similarity = difflib.SequenceMatcher(None, prod_name, existing_name).ratio()
#                 if similarity > 0.85:
#                     is_duplicate = True
#                     # Keep the cheaper one
#                     if prod_price > 0 and (existing.get('price', 0) == 0 or prod_price < existing.get('price', 0)):
#                         unique_products[i] = prod
#                     break
                    
#         if not is_duplicate:
#             unique_products.append(prod)
            
#     return unique_products

# def calculate_value_score(price: float, rating: float, max_price: float) -> float:
#     """Score 0-100 based on price (lower is better) and rating (higher is better)."""
#     if price <= 0 or rating <= 0:
#         return 0.0
        
#     rating_score = (rating / 5.0) * 50
    
#     price_score = 0
#     if max_price > 0:
#         price_score = ((1 - price / max_price) * 50)
        
#     return max(0.0, min(100.0, rating_score + price_score))

# def format_currency(amount: float, symbol: str = '₹') -> str:
#     """Format amount with commas and 2 decimal places."""
#     return f"{symbol}{amount:,.2f}"

# def truncate_text(text: str, max_length: int = 100) -> str:
#     """Truncate text with ellipsis if it exceeds max_length."""
#     if not text:
#         return ""
#     if len(text) <= max_length:
#         return text
#     return text[:max_length-3] + "..."
