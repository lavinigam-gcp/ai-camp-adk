# Lab 4: Schema definitions for the Restaurant Order System

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

# Menu Item Schema
class MenuItem(BaseModel):
    """Represents a single menu item"""
    name: str = Field(description="Name of the menu item")
    category: Literal["appetizer", "main", "dessert", "beverage"] = Field(description="Category of the item")
    price: float = Field(description="Price in USD")
    vegetarian: bool = Field(default=False, description="Is vegetarian")
    vegan: bool = Field(default=False, description="Is vegan")
    gluten_free: bool = Field(default=False, description="Is gluten-free")

# Order Item Schema (what customer orders)
class OrderItem(BaseModel):
    """Represents an item in a customer's order"""
    item_name: str = Field(description="Name of the menu item")
    quantity: int = Field(ge=1, description="Quantity ordered")
    special_instructions: Optional[str] = Field(default=None, description="Special preparation instructions")

# Customer Order Input Schema
class CustomerOrder(BaseModel):
    """Input schema for customer orders"""
    customer_name: str = Field(description="Customer's name")
    items: List[OrderItem] = Field(description="List of items to order")
    dietary_restrictions: Optional[List[str]] = Field(default=None, description="Any dietary restrictions")
    table_number: Optional[int] = Field(default=None, description="Table number for dine-in")
    order_type: Literal["dine-in", "takeout", "delivery"] = Field(default="dine-in", description="Type of order")

# Order Receipt Output Schema
class OrderReceipt(BaseModel):
    """Output schema for order receipts"""
    order_id: str = Field(description="Unique order identifier")
    customer_name: str = Field(description="Customer's name")
    order_type: str = Field(description="Type of order")
    items: List[dict] = Field(description="Detailed list of ordered items with prices")
    subtotal: float = Field(description="Subtotal before tax")
    tax: float = Field(description="Tax amount (8%)")
    tip_suggestion: dict = Field(description="Suggested tip amounts")
    total: float = Field(description="Total amount due")
    estimated_time: str = Field(description="Estimated preparation time")
    special_notes: Optional[str] = Field(default=None, description="Any special notes or warnings")
    timestamp: str = Field(description="Order timestamp")

# Menu Database (simulated)
MENU_ITEMS = [
    # Appetizers
    MenuItem(name="Caesar Salad", category="appetizer", price=8.99, vegetarian=True, gluten_free=True),
    MenuItem(name="Garlic Bread", category="appetizer", price=6.99, vegetarian=True),
    MenuItem(name="Chicken Wings", category="appetizer", price=10.99),
    MenuItem(name="Veggie Spring Rolls", category="appetizer", price=7.99, vegetarian=True, vegan=True),

    # Main Courses
    MenuItem(name="Grilled Salmon", category="main", price=24.99, gluten_free=True),
    MenuItem(name="Ribeye Steak", category="main", price=32.99, gluten_free=True),
    MenuItem(name="Margherita Pizza", category="main", price=16.99, vegetarian=True),
    MenuItem(name="Vegan Buddha Bowl", category="main", price=14.99, vegetarian=True, vegan=True, gluten_free=True),
    MenuItem(name="Chicken Alfredo", category="main", price=18.99),
    MenuItem(name="Mushroom Risotto", category="main", price=17.99, vegetarian=True, gluten_free=True),

    # Desserts
    MenuItem(name="Chocolate Lava Cake", category="dessert", price=7.99, vegetarian=True),
    MenuItem(name="Tiramisu", category="dessert", price=6.99, vegetarian=True),
    MenuItem(name="Fruit Sorbet", category="dessert", price=5.99, vegetarian=True, vegan=True, gluten_free=True),
    MenuItem(name="Cheesecake", category="dessert", price=7.49, vegetarian=True),

    # Beverages
    MenuItem(name="Soda", category="beverage", price=2.99, vegetarian=True, vegan=True, gluten_free=True),
    MenuItem(name="Fresh Orange Juice", category="beverage", price=4.99, vegetarian=True, vegan=True, gluten_free=True),
    MenuItem(name="Coffee", category="beverage", price=3.49, vegetarian=True, vegan=True, gluten_free=True),
    MenuItem(name="Wine (Glass)", category="beverage", price=8.99, vegetarian=True, vegan=True, gluten_free=True),
]

def get_menu_as_dict():
    """Convert menu items to dictionary format for agent use"""
    return {
        "appetizers": [item.model_dump() for item in MENU_ITEMS if item.category == "appetizer"],
        "mains": [item.model_dump() for item in MENU_ITEMS if item.category == "main"],
        "desserts": [item.model_dump() for item in MENU_ITEMS if item.category == "dessert"],
        "beverages": [item.model_dump() for item in MENU_ITEMS if item.category == "beverage"]
    }