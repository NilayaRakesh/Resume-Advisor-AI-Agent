from messages.protocol import Message
from utils.parser import extract_text_from_pdf
from utils.skills_extractor import extract_skills

def handle_message(message: Message) -> Message:
    resume_path = message.payload["resume_path"]

    print("Extracting resume text from file...")
    resume_text = extract_text_from_pdf(resume_path)

    print("Extracting resume keywords...")
    resume_keywords = extract_skills(resume_text)

    return Message(
        sender="ResumeExtractorAgent",
        receiver="JDExtractorAgent",
        intent="parse_jd",
        payload={
            "jd_path": message.payload["jd_path"],
            "resume_text": resume_text,
            "resume_keywords": resume_keywords
        }
    )