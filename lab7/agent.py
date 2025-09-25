# Lab 7: Callbacks & Events - Customer Service Monitor (Python Version)
# This lab demonstrates callback usage for monitoring and analytics

from google.adk import Agent
from lab7.callbacks import (
    before_model_callback,
    after_model_callback,
    before_tool_callback,
    after_tool_callback,
    get_metrics_summary
)

def handle_complaint(issue: str, severity: str = "medium") -> dict:
    """
    Handle customer complaints with tracking.

    Args:
        issue: Description of the complaint
        severity: low, medium, or high

    Returns:
        Resolution details
    """
    return {
        "status": "resolved",
        "issue": issue,
        "severity": severity,
        "resolution": "We've addressed your concern and applied a 10% discount to your next order.",
        "ticket_id": f"TKT-{hash(issue) % 10000:04d}"
    }

def check_order_status(order_id: str) -> dict:
    """
    Check the status of an order.

    Args:
        order_id: The order identifier

    Returns:
        Order status information
    """
    # Simulated order statuses
    statuses = ["processing", "shipped", "out for delivery", "delivered"]
    import random
    status = random.choice(statuses)

    return {
        "order_id": order_id,
        "status": status,
        "estimated_delivery": "2-3 business days",
        "tracking_number": f"TRK{order_id}"
    }

# Create customer service agent with callbacks
root_agent = Agent(
    model="gemini-2.5-flash",
    name="customer_service_monitor",
    description="Customer service agent with performance monitoring and sentiment tracking",

    instruction="""
    You are Sarah, a professional customer service representative.

    Your responsibilities:
    1. Handle customer inquiries professionally
    2. Resolve complaints efficiently
    3. Check order statuses
    4. Maintain positive sentiment
    5. Track performance metrics

    Your approach:
    - Always greet customers warmly
    - Empathize with their concerns
    - Provide clear solutions
    - Follow up on resolution
    - Thank them for their patience

    Available tools:
    - handle_complaint: For resolving issues
    - check_order_status: For order inquiries
    - get_metrics_summary: For performance review

    Remember:
    - Every interaction is monitored for quality
    - Response time matters
    - Sentiment is tracked
    - Tool usage is logged
    """,

    # Tools for customer service
    tools=[
        handle_complaint,
        check_order_status,
        get_metrics_summary
    ],

    # Callbacks for monitoring
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,
    before_tool_callback=before_tool_callback,
    after_tool_callback=after_tool_callback
)