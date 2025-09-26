# Lab 4a: Input Schema for Order Processing

from pydantic import BaseModel, Field
from typing import Optional

class CustomerOrder(BaseModel):
    """Input schema for customer orders"""
    customer_name: str = Field(description="Customer's name")
    items: str = Field(description="Items to order as text")
    order_type: str = Field(description="Order type: dine-in, takeout, or delivery")
    dietary_restrictions: Optional[str] = Field(default=None, description="Any dietary restrictions")