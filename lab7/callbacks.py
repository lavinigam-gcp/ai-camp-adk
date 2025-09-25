# Lab 7: Callback implementations for monitoring

import time
from datetime import datetime
from typing import Dict, Any, List

# Storage for metrics
METRICS = {
    "response_times": [],
    "tool_calls": [],
    "sentiment_scores": [],
    "token_usage": []
}

def before_model_callback(request_data: Dict[str, Any]) -> None:
    """
    Called before the model processes a request.
    Used for logging, validation, or modification.
    """
    print(f"[BEFORE MODEL] Starting request at {datetime.now().isoformat()}")
    print(f"[BEFORE MODEL] Input length: {len(str(request_data.get('content', '')))} chars")

    # Track request start time
    METRICS["request_start"] = time.time()

def after_model_callback(response_data: Dict[str, Any]) -> None:
    """
    Called after the model generates a response.
    Used for response analysis, metrics, or modification.
    """
    # Calculate response time
    if "request_start" in METRICS:
        response_time = time.time() - METRICS["request_start"]
        METRICS["response_times"].append(response_time)
        print(f"[AFTER MODEL] Response time: {response_time:.2f} seconds")

    # Analyze sentiment (simplified)
    response_text = str(response_data.get("content", ""))
    positive_words = ["great", "excellent", "happy", "wonderful", "perfect"]
    negative_words = ["sorry", "unfortunately", "problem", "issue", "cannot"]

    positive_score = sum(1 for word in positive_words if word in response_text.lower())
    negative_score = sum(1 for word in negative_words if word in response_text.lower())

    sentiment = "positive" if positive_score > negative_score else "negative" if negative_score > positive_score else "neutral"
    METRICS["sentiment_scores"].append(sentiment)

    print(f"[AFTER MODEL] Sentiment: {sentiment}")
    print(f"[AFTER MODEL] Response length: {len(response_text)} chars")

def before_tool_callback(tool_name: str, tool_args: Dict[str, Any]) -> None:
    """
    Called before a tool is executed.
    Used for tool usage tracking or parameter validation.
    """
    print(f"[BEFORE TOOL] Calling tool: {tool_name}")
    print(f"[BEFORE TOOL] Arguments: {tool_args}")

    # Track tool usage
    METRICS["tool_calls"].append({
        "tool": tool_name,
        "timestamp": datetime.now().isoformat(),
        "args": tool_args
    })

def after_tool_callback(tool_name: str, tool_result: Any) -> None:
    """
    Called after a tool completes execution.
    Used for result validation or logging.
    """
    print(f"[AFTER TOOL] Tool {tool_name} completed")
    print(f"[AFTER TOOL] Result type: {type(tool_result).__name__}")

    # Could add result validation or caching here

def get_metrics_summary() -> Dict[str, Any]:
    """
    Get a summary of collected metrics.
    """
    avg_response_time = sum(METRICS["response_times"]) / len(METRICS["response_times"]) if METRICS["response_times"] else 0

    sentiment_counts = {}
    for sentiment in METRICS["sentiment_scores"]:
        sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

    tool_usage = {}
    for call in METRICS["tool_calls"]:
        tool_name = call["tool"]
        tool_usage[tool_name] = tool_usage.get(tool_name, 0) + 1

    return {
        "total_requests": len(METRICS["response_times"]),
        "average_response_time": f"{avg_response_time:.2f} seconds",
        "sentiment_distribution": sentiment_counts,
        "tool_usage_count": tool_usage,
        "last_5_tools": METRICS["tool_calls"][-5:] if METRICS["tool_calls"] else []
    }