import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.product import Product
from Agents.comparison_agent import comparison_agent
from Agents.recommendation_agent import recommendation_agent


# -----------------------------
# Mock Products (Pydantic Model)
# -----------------------------
MOCK_PRODUCTS = [
    Product(
        name="iPhone 15 128GB Blue",
        price=65999,
        rating=4.6,
        reviews=12500,
        seller="Appario Retail",
        url="https://amazon.in/x1",
        image_url="",
        source="Amazon",
        delivery_info="Free delivery tomorrow",
        specifications="128GB",
        brand="Apple",
    ),
    Product(
        name="Apple iPhone 15 (128 GB)",
        price=64999,
        rating=4.5,
        reviews=8300,
        seller="RetailNet",
        url="https://flipkart.com/x2",
        image_url="",
        source="Flipkart",
        delivery_info="2 Days",
        specifications="128GB",
        brand="Apple",
    ),
    Product(
        name="Samsung Galaxy S24",
        price=59999,
        rating=4.4,
        reviews=6100,
        seller="Samsung",
        url="https://amazon.in/x3",
        image_url="",
        source="Amazon",
        delivery_info="Tomorrow",
        specifications="128GB",
        brand="Samsung",
    ),
    Product(
        name="Samsung Galaxy S24 5G",
        price=57499,
        rating=4.3,
        reviews=4200,
        seller="SuperComNet",
        url="https://flipkart.com/x4",
        image_url="",
        source="Flipkart",
        delivery_info="3 Days",
        specifications="128GB",
        brand="Samsung",
    ),
    Product(
        name="OnePlus 12",
        price=64999,
        rating=4.5,
        reviews=3100,
        seller="OnePlus",
        url="https://amazon.in/x5",
        image_url="",
        source="Amazon",
        delivery_info="Tomorrow",
        specifications="256GB",
        brand="OnePlus",
    ),
]


def run_case(title, state):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    comparison = comparison_agent(state)
    state.update(comparison)

    recommendation = recommendation_agent(state)
    state.update(recommendation)

    comparison_data = state["comparison_data"]

    print("\nComparison Summary")
    print("-" * 30)

    if comparison_data:

        cheapest = comparison_data.get("cheapest")
        highest = comparison_data.get("highest_rated")
        best = comparison_data.get("best_value")

        if cheapest:
            print(f"Cheapest      : {cheapest['name']}  ₹{cheapest['price']}")

        if highest:
            print(f"Highest Rated : {highest['name']} ({highest['rating']}⭐)")

        if best:
            print(f"Best Value    : {best['name']} ({best['value_score']})")

        print("\nProducts by Source")

        for source, products in comparison_data.get("by_source", {}).items():
            print(f"{source} : {len(products)} products")

    print("\nRecommendations")
    print("-" * 30)

    for product in state["recommendations"]:

        print(
            f"{product['name']} | "
            f"₹{product['price']} | "
            f"{product['rating']}⭐ | "
            f"{product['source']} | "
            f"Score = {product['recommendation_score']}"
        )

    print("\nAgent Status")
    print(state["agent_status"])

    if state["errors"]:
        print("\nErrors")
        for error in state["errors"]:
            print(error)


if __name__ == "__main__":

    base_state = {
        "query": "iPhone 15",
        "budget": 60000,
        "brand_filter": "",
        "products": [p.model_dump() for p in MOCK_PRODUCTS],
        "comparison_data": {},
        "recommendations": [],
        "agent_status": {
            "search": "completed",
            "comparison": "pending",
            "recommendation": "pending",
            "response": "pending",
        },
        "errors": [],
    }

    run_case(
        "CASE 1 : Budget ₹60,000",
        base_state,
    )

    brand_state = {
        "query": "iPhone 15",
        "budget": 70000,
        "brand_filter": "Apple",
        "products": [p.model_dump() for p in MOCK_PRODUCTS],
        "comparison_data": {},
        "recommendations": [],
        "agent_status": {
            "search": "completed",
            "comparison": "pending",
            "recommendation": "pending",
            "response": "pending",
        },
        "errors": [],
    }

    run_case(
        "CASE 2 : Apple Only",
        brand_state,
    )

    print("\nAll tests completed successfully.")