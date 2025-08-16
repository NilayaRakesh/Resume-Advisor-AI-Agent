
from messages.protocol import Message

def get_inputs() -> Message:
    resume_path: str = "data/resume.pdf"
    jd_path: str = "data/job_descriptions/jd_google.txt"
    return Message(
        sender="UserInputAgent",
        receiver="ResumeExtractorAgent",
        intent="parse_resume",
        payload={"resume_path": resume_path, "jd_path": jd_path}
    )