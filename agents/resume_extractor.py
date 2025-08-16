from messages.protocol import Message
from utils.parser import extract_text_from_pdf

def handle_message(message: Message) -> Message:
    resume_path: str = message.payload["resume_path"]
    jd_path: str = message.payload["jd_path"]
    resume_text: str = extract_text_from_pdf(resume_path)

    return Message(
        sender="ResumeExtractorAgent",
        receiver="JDExtractorAgent",
        intent="parse_jd",
        payload={
            "resume_text": resume_text,
            "jd_path": jd_path
        }
    )