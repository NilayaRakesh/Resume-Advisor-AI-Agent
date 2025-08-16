from typing import List
from messages.protocol import Message
from utils.llama_cpp_executor import run_llm

TEXT_CUT_OFF_CHARS_LENGTH = 400  # to limit prompt size. Can be increased if using a powerful model for better results
SCORE_THRESHOLD = 85


def handle_message(message: Message) -> Message:
    resume_text = message.payload["resume_keywords"]
    jd_text = message.payload["jd_text"]
    resume_keywords = set(message.payload["resume_keywords"])
    jd_keywords = set(message.payload["jd_keywords"])

    missing_keywords = list(jd_keywords - resume_keywords)
    print(f"missing_keywords: {missing_keywords}")

    score = message.payload["match_score"]
    suggestions: List[str] = []

    if score < SCORE_THRESHOLD:
        suggestions.append("Your resume could be improved to better align with this job description.")
        if missing_keywords:
            suggestions.append(f"Consider adding or emphasizing the following concepts: {', '.join(missing_keywords[:5])}.")

            # Build a prompt for llama.cpp
            prompt = f"""
                You are a career coach assistant.
                
                Resume snippet:
                {resume_text[:TEXT_CUT_OFF_CHARS_LENGTH]}
                
                Job description snippet:
                {jd_text[:TEXT_CUT_OFF_CHARS_LENGTH]}
                
                Resume match score: {score}%
                
                Missing important concepts or skills: {', '.join(missing_keywords[:10])}
                
                Please provide 2-3 concise suggestions on how to improve the resume to better match the job description.
                """
            try:
                print("generating LLM suggestions...")
                llm_suggestions = run_llm(prompt)
                print(f"llm_suggestions: {llm_suggestions}")
                suggestions.append(f"LLM suggestions: {llm_suggestions}")
            except Exception as e:
                suggestions.append(f"LLM generation failed: {e}")
    else:
        suggestions.append("Great match! Your resume aligns well with the job description.")

    return Message(
        sender="ImprovementAgent",
        receiver="User",
        intent="final_output",
        payload={
            "score": score,
            "suggestions": suggestions
        }
    )
