from messages.protocol import Message
from utils.embeddings import get_embedding, cosine_similarity

def handle_message(message: Message) -> Message:
    resume_keywords: str = message.payload["resume_keywords"]
    jd_keywords: str = message.payload["jd_keywords"]

    # converting keywords into embeddings (vectors) so that they can be semantically compared using cosine similarity
    resume_emb = get_embedding(" ".join(resume_keywords))
    jd_emb = get_embedding(" ".join(jd_keywords))

    score: float = round(cosine_similarity(resume_emb, jd_emb) * 100, 2)
    print(f"match_score: {score}")

    return Message(
        sender="ScoringAgent",
        receiver="ImprovementAgent",
        intent="suggest_improvements",
        payload={
            "match_score": score,
            "resume_text": message.payload["resume_text"],
            "resume_keywords": resume_keywords,
            "jd_text": message.payload["jd_text"],
            "jd_keywords": jd_keywords
        }
    )
