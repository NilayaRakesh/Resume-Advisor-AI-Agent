
from messages.protocol import Message

def get_inputs() -> Message:
    # Can replace this hardcoded paths with user uploaded files/text in natural language
    resume_path: str = "data/resume.pdf"
    jd_path: str = "data/job_descriptions/jd.txt"
    return Message(
        sender="UserInputAgent",
        receiver="ResumeExtractorAgent",
        intent="parse_resume",
        payload={"resume_path": resume_path, "jd_path": jd_path}
    )