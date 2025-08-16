from typing import List
from messages.protocol import Message
from utils.embeddings import get_embedding, cosine_similarity

def extract_keywords(text: str) -> List[str]:
    words = text.lower().split()
    return list(set(words))

def handle_message(message: Message) -> Message:
    resume_text: str = message.payload["resume_text"]
    jd_text: str = message.payload["jd_text"]

    resume_keywords: List[str] = extract_keywords(resume_text)
    jd_keywords: List[str] = extract_keywords(jd_text)

    resume_emb = get_embedding(" ".join(resume_keywords))
    jd_emb = get_embedding(" ".join(jd_keywords))

    score: float = round(cosine_similarity(resume_emb, jd_emb) * 100, 2)

    return Message(
        sender="ScoringAgent",
        receiver="ImprovementAgent",
        intent="suggest_improvements",
        payload={
            "match_score": score,
            "resume_text": resume_text,
            "jd_text": jd_text
        }
    )
