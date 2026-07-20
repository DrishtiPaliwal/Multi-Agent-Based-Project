from models.product import Product


def calculate_value_score(price: float, rating: float, max_price: float) -> float:
    """Calculate value score based on price and rating."""

    if max_price == 0:
        return 0.0

    price_score = (1 - (price / max_price)) * 50
    rating_score = (rating / 5) * 50

    return round(price_score + rating_score, 2)


def comparison_agent(state):

    products: list[Product] = state.get("products", [])

    if not products:
        return {
            "comparison_data": {}
        }

    # Cheapest product
    cheapest = min(products, key=lambda product: product.price)

    # Highest rated product
    highest_rated = max(products, key=lambda product: product.rating)

    # Maximum price
    max_price = max(product.price for product in products)

    # Calculate value score
    for product in products:
        product.value_score = calculate_value_score(
            product.price,
            product.rating,
            max_price
        )

    # Best value product
    best_value = max(products, key=lambda product: product.value_score)

    # Group products by source
    by_source = {}

    for product in products:
        source = product.source

        if source not in by_source:
            by_source[source] = []

        by_source[source].append(product)

    comparison_data = {
        "products": products,
        "cheapest": cheapest,
        "highest_rated": highest_rated,
        "best_value": best_value,
        "by_source": by_source
    }

    return {
        "comparison_data": comparison_data
    }