from typing import List
from messages.protocol import Message

def handle_message(message: Message) -> Message:
    score: float = message.payload["match_score"]
    suggestions: List[str] = []

    if score < 70:
        suggestions.append("Add specific tools and technologies mentioned in the job description.")
    elif score < 85:
        suggestions.append("Good match! You may still want to align some keywords.")
    else:
        suggestions.append("Strong match. Resume looks well tailored!")

    return Message(
        sender="ImprovementAgent",
        receiver="User",
        intent="final_output",
        payload={
            "score": score,
            "suggestions": suggestions
        }
    )
