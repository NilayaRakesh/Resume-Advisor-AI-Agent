from typing import Any, Dict

class Message:
    def __init__(self, sender: str, receiver: str, intent: str, payload: Dict[str, Any]):
        self.sender = sender
        self.receiver = receiver
        self.intent = intent
        self.payload = payload

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "intent": self.intent,
            "payload": self.payload
        }

    def __repr__(self) -> str:
        return f"<Message from {self.sender} to {self.receiver} ({self.intent})>"