from messages.protocol import Message
from utils.skills_extractor import extract_skills

def handle_message(message: Message) -> Message:
    jd_path: str = message.payload["jd_path"]

    print("Extracting JD text from file...")
    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text: str = f.read()

    print("Extracting JD keywords...")
    jd_keywords = extract_skills(jd_text)

    return Message(
        sender="JDExtractorAgent",
        receiver="ScoringAgent",
        intent="score_match",
        payload={
            "resume_text": message.payload["resume_text"],
            "resume_keywords": message.payload["resume_keywords"],
            "jd_text": jd_text,
            "jd_keywords": jd_keywords
        }
    )