# Lab 4: Structured Data - Restaurant Order System (Python Version)
# This lab demonstrates input/output schemas for structured data handling

from google.adk import Agent
from schemas import CustomerOrder, OrderReceipt, get_menu_as_dict, MENU_ITEMS
from datetime import datetime
import random
import json

def process_order(order_data: dict) -> dict:
    """
    Process a customer order and generate a receipt.

    Args:
        order_data: Dictionary containing order details

    Returns:
        Dictionary with receipt information
    """
    # Get menu for validation
    menu_dict = {item.name.lower(): item for item in MENU_ITEMS}

    # Process items and calculate totals
    processed_items = []
    subtotal = 0.0

    for item in order_data.get("items", []):
        item_name = item["item_name"].lower()
        if item_name in menu_dict:
            menu_item = menu_dict[item_name]
            item_total = menu_item.price * item["quantity"]
            processed_items.append({
                "name": menu_item.name,
                "quantity": item["quantity"],
                "price_each": menu_item.price,
                "total": item_total,
                "special_instructions": item.get("special_instructions")
            })
            subtotal += item_total

    # Calculate tax and total
    tax = subtotal * 0.08  # 8% tax
    total = subtotal + tax

    # Generate receipt
    receipt = {
        "order_id": f"ORD-{random.randint(1000, 9999)}",
        "customer_name": order_data["customer_name"],
        "order_type": order_data.get("order_type", "dine-in"),
        "items": processed_items,
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "tip_suggestion": {
            "15%": round(total * 0.15, 2),
            "18%": round(total * 0.18, 2),
            "20%": round(total * 0.20, 2)
        },
        "total": round(total, 2),
        "estimated_time": "20-25 minutes" if order_data.get("order_type") != "delivery" else "35-45 minutes",
        "special_notes": None,
        "timestamp": datetime.now().isoformat()
    }

    # Add dietary notes if applicable
    if order_data.get("dietary_restrictions"):
        receipt["special_notes"] = f"Dietary restrictions noted: {', '.join(order_data['dietary_restrictions'])}"

    return receipt

# Create the restaurant order agent with schemas
root_agent = Agent(
    model="gemini-2.5-flash",
    name="restaurant_order_system",
    description="Restaurant ordering system that handles structured orders and returns detailed receipts",

    instruction=f"""
    You are a friendly restaurant order system for "The Digital Diner".

    Our Menu:
    {json.dumps(get_menu_as_dict(), indent=2)}

    When taking orders:
    1. Welcome the customer warmly
    2. Confirm their order details
    3. Check for any dietary restrictions against our menu
    4. Suggest complementary items (e.g., drinks with meals, desserts)
    5. Process the order using the process_order tool
    6. Present the receipt clearly

    For dietary restrictions:
    - Vegetarian: We have several options marked
    - Vegan: Limited but delicious options available
    - Gluten-free: Various options across categories

    Always be helpful and accommodating. If an item isn't on the menu, suggest similar alternatives.
    """,

    # Input schema - what format we expect from users
    input_schema=CustomerOrder,

    # Output schema - what format we'll return
    output_schema=OrderReceipt,

    # Tool for processing orders
    tools=[process_order]
)