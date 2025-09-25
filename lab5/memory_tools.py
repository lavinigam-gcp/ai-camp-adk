# Lab 5: Memory tools for the Personal Learning Tutor

from typing import Dict, Any, List
from datetime import datetime

# Simulated memory storage (in production, use a database)
LEARNING_MEMORY = {
    "topics_covered": [],
    "quiz_scores": {},
    "learning_preferences": {},
    "study_sessions": []
}

def remember_topic(topic: str, details: str) -> Dict[str, Any]:
    """
    Remember a topic that was discussed.

    Args:
        topic: The topic name
        details: Key points or details about the topic

    Returns:
        Confirmation of memory storage
    """
    LEARNING_MEMORY["topics_covered"].append({
        "topic": topic,
        "details": details,
        "timestamp": datetime.now().isoformat(),
        "review_count": 0
    })

    return {
        "status": "remembered",
        "topic": topic,
        "total_topics": len(LEARNING_MEMORY["topics_covered"])
    }

def recall_topics() -> Dict[str, Any]:
    """
    Recall all topics that have been covered.

    Returns:
        List of topics with details
    """
    if not LEARNING_MEMORY["topics_covered"]:
        return {"status": "no_topics", "message": "No topics covered yet"}

    return {
        "status": "success",
        "topics": LEARNING_MEMORY["topics_covered"],
        "total": len(LEARNING_MEMORY["topics_covered"])
    }

def record_quiz_score(topic: str, score: int, total: int) -> Dict[str, Any]:
    """
    Record a quiz score for a topic.

    Args:
        topic: The topic tested
        score: Points earned
        total: Total possible points

    Returns:
        Score summary
    """
    if topic not in LEARNING_MEMORY["quiz_scores"]:
        LEARNING_MEMORY["quiz_scores"][topic] = []

    percentage = (score / total) * 100
    LEARNING_MEMORY["quiz_scores"][topic].append({
        "score": score,
        "total": total,
        "percentage": percentage,
        "timestamp": datetime.now().isoformat()
    })

    # Update review count for this topic
    for t in LEARNING_MEMORY["topics_covered"]:
        if t["topic"] == topic:
            t["review_count"] += 1

    return {
        "status": "recorded",
        "topic": topic,
        "score": f"{score}/{total}",
        "percentage": f"{percentage:.1f}%",
        "improvement_tip": "Great job!" if percentage >= 80 else "Keep practicing!"
    }

def get_learning_progress() -> Dict[str, Any]:
    """
    Get overall learning progress summary.

    Returns:
        Progress summary with statistics
    """
    total_topics = len(LEARNING_MEMORY["topics_covered"])
    total_quizzes = sum(len(scores) for scores in LEARNING_MEMORY["quiz_scores"].values())

    avg_score = 0
    if total_quizzes > 0:
        all_percentages = []
        for topic_scores in LEARNING_MEMORY["quiz_scores"].values():
            all_percentages.extend([s["percentage"] for s in topic_scores])
        avg_score = sum(all_percentages) / len(all_percentages)

    # Find topics that need review (not reviewed recently or low scores)
    topics_to_review = []
    for topic in LEARNING_MEMORY["topics_covered"]:
        topic_name = topic["topic"]
        if topic_name in LEARNING_MEMORY["quiz_scores"]:
            recent_scores = LEARNING_MEMORY["quiz_scores"][topic_name]
            if recent_scores and recent_scores[-1]["percentage"] < 70:
                topics_to_review.append(topic_name)
        elif topic["review_count"] == 0:
            topics_to_review.append(topic_name)

    return {
        "total_topics_learned": total_topics,
        "total_quizzes_taken": total_quizzes,
        "average_score": f"{avg_score:.1f}%",
        "topics_needing_review": topics_to_review[:3],  # Top 3 topics to review
        "study_streak": len(LEARNING_MEMORY["study_sessions"])
    }

def set_learning_preference(preference_type: str, value: str) -> Dict[str, Any]:
    """
    Set a learning preference for personalization.

    Args:
        preference_type: Type of preference (e.g., "style", "pace", "focus_area")
        value: The preference value

    Returns:
        Confirmation of preference saved
    """
    LEARNING_MEMORY["learning_preferences"][preference_type] = value

    return {
        "status": "preference_saved",
        "type": preference_type,
        "value": value,
        "message": f"I'll remember that you prefer {value} for {preference_type}"
    }