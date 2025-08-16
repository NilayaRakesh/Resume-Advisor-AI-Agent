from messages.protocol import Message

def handle_message(message: Message) -> Message:
    jd_path: str = message.payload["jd_path"]
    resume_text: str = message.payload["resume_text"]

    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text: str = f.read()

    return Message(
        sender="JDExtractorAgent",
        receiver="ScoringAgent",
        intent="score_match",
        payload={
            "resume_text": resume_text,
            "jd_text": jd_text
        }
    )