from typing import Optional
from messages.protocol import Message
from agents.user_input_agent import get_inputs
from agents.resume_extractor import handle_message as resume_handler
from agents.jd_extractor import handle_message as jd_handler
from agents.scoring_agent import handle_message as scoring_handler
from agents.improvement_agent import handle_message as improvement_handler

def route(message: Message) -> Optional[Message]:
    if message.receiver == "ResumeExtractorAgent":
        return resume_handler(message)
    elif message.receiver == "JDExtractorAgent":
        return jd_handler(message)
    elif message.receiver == "ScoringAgent":
        return scoring_handler(message)
    elif message.receiver == "ImprovementAgent":
        return improvement_handler(message)
    elif message.receiver == "User":
        print("\nFinal Match Score:", message.payload["score"])
        print("Suggestions:")
        for suggestion in message.payload["suggestions"]:
            print(" -", suggestion)
        return None
    return None

def main():
    msg: Optional[Message] = get_inputs()
    while msg:
        print("Routing:", msg)
        msg = route(msg)

if __name__ == "__main__":
    main()
