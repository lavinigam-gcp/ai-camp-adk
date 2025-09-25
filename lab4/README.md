# Lab 4: Structured Data - Restaurant Order System 🍽️

## Overview
This lab demonstrates how to work with structured data using Pydantic schemas. You'll build a restaurant ordering system that accepts structured orders and returns formatted receipts. This shows how ADK enforces data contracts for reliable agent interactions.

## Learning Objectives
- Define input schemas for structured requests
- Create output schemas for consistent responses
- Use Pydantic models for data validation
- Build agents that handle complex data structures
- Understand schema-driven agent design

## Features Demonstrated
- ✅ Input schema validation (CustomerOrder)
- ✅ Output schema enforcement (OrderReceipt)
- ✅ Pydantic model definitions
- ✅ Complex nested data structures
- ✅ Type hints and field validation
- ✅ Structured tool responses

## Files
- `agent.py` - Python implementation with schemas
- `root_agent.yaml` - YAML configuration
- `schemas.py` - Pydantic schema definitions
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```
Then select **lab4** from the dropdown.

## 🗣️ Try These Sample Queries

### **Simple Natural Language Orders**
```
I'd like to order a Caesar salad, grilled salmon, and a coffee for dine-in at table 7
```

```
Can I get a veggie spring roll and a chai latte for takeout?
```

```
I want to order a ribeye steak medium rare, with a side salad, and a glass of wine for table 12
```

### **Dietary Restrictions**
```
I'm vegan - what options do you have? I'd like to order something filling for delivery
```

```
I need gluten-free options. Can you recommend a meal and drink combination?
```

```
I'm vegetarian and would like something light but satisfying for dine-in
```

### **Complex Orders**
```
I'm ordering for 4 people: 2 margherita pizzas, 1 chicken alfredo, 1 vegan buddha bowl, 4 sodas, and 2 desserts for dine-in at table 15
```

```
Special instructions: Can I get the salmon with no garlic, Caesar salad with dressing on the side, and coffee decaf?
```

## 📋 Advanced: Structured JSON Orders

If you want to test the structured input format directly:
```json
{
  "customer_name": "Alice",
  "items": [
    {"item_name": "Caesar Salad", "quantity": 1},
    {"item_name": "Grilled Salmon", "quantity": 1},
    {"item_name": "Coffee", "quantity": 1}
  ],
  "order_type": "dine-in",
  "table_number": 7
}
```

### Order with Dietary Restrictions:
```json
{
  "customer_name": "Bob",
  "items": [
    {"item_name": "Vegan Buddha Bowl", "quantity": 1},
    {"item_name": "Fresh Orange Juice", "quantity": 2}
  ],
  "dietary_restrictions": ["vegan", "gluten-free"],
  "order_type": "takeout"
}
```

### Complex Order with Special Instructions:
```json
{
  "customer_name": "Carol",
  "items": [
    {"item_name": "Ribeye Steak", "quantity": 1, "special_instructions": "Medium rare, no garlic"},
    {"item_name": "Caesar Salad", "quantity": 1, "special_instructions": "Dressing on the side"},
    {"item_name": "Wine Glass", "quantity": 2},
    {"item_name": "Tiramisu", "quantity": 1}
  ],
  "order_type": "dine-in",
  "table_number": 12
}
```

## Key Concepts

### Input Schema Definition
```python
class CustomerOrder(BaseModel):
    customer_name: str = Field(description="Customer's name")
    items: List[OrderItem] = Field(description="List of items")
    dietary_restrictions: Optional[List[str]] = Field(default=None)
    order_type: Literal["dine-in", "takeout", "delivery"]
```

### Output Schema Definition
```python
class OrderReceipt(BaseModel):
    order_id: str = Field(description="Unique order ID")
    items: List[dict] = Field(description="Ordered items")
    subtotal: float = Field(description="Subtotal")
    tax: float = Field(description="Tax amount")
    total: float = Field(description="Total amount")
```

### Schema Integration
```python
root_agent = Agent(
    input_schema=CustomerOrder,   # Validates input
    output_schema=OrderReceipt,   # Enforces output format
    ...
)
```

## Schema Benefits

### 🎯 Type Safety
- Automatic validation of input data
- Guaranteed output structure
- Clear data contracts

### 📝 Documentation
- Self-documenting APIs
- Field descriptions
- Type hints for IDE support

### 🛡️ Error Handling
- Validation errors before processing
- Clear error messages
- Prevents runtime failures

## Pydantic Features Used

### Field Validation
```python
quantity: int = Field(ge=1)  # Must be >= 1
```

### Optional Fields
```python
special_instructions: Optional[str] = Field(default=None)
```

### Literal Types
```python
category: Literal["appetizer", "main", "dessert", "beverage"]
```

### Nested Models
```python
class CustomerOrder(BaseModel):
    items: List[OrderItem]  # List of another model
```

## Extending This Lab

### Add More Features:
1. **Discount System**: Apply coupons and promotions
2. **Allergen Tracking**: Track and warn about allergens
3. **Inventory Management**: Check item availability
4. **Loyalty Points**: Calculate and apply points

### More Complex Schemas:
1. **Delivery Address**: Nested address schema
2. **Payment Methods**: Multiple payment options
3. **Order Modifications**: Update existing orders
4. **Group Orders**: Multiple customers, split bills

## What's Next?

In Lab 5, you'll learn about stateful conversations and memory. You'll build a personal learning tutor that:
- Remembers previous conversations
- Tracks learning progress
- Personalizes responses based on history
- Uses memory tools for long-term retention

## Tips
- 💡 Always validate data at the boundaries
- 💡 Use descriptive field names and descriptions
- 💡 Provide sensible defaults for optional fields
- 💡 Keep schemas focused and single-purpose
- 💡 Use nested models for complex structures

## Common Issues
- Schema validation errors show which field failed
- Ensure JSON input matches schema exactly
- Field names are case-sensitive
- Lists need proper JSON array syntax `[]`
- Optional fields can be omitted entirely