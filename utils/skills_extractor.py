# pip install spacy
# python -m spacy download en_core_web_sm

from typing import List, Set
import spacy
from spacy.matcher import PhraseMatcher
from utils.llama_cpp_executor import run_llm

LLM_RESUME_CUT_OFF_CHARS_LENGTH = 400  # to limit prompt size. Can be increased if using a powerful model for better results
LLM_OUTPUT_MAX_TOKENS = 128  # to limit response size. Can be increased if using a powerful model for better results

SKILL_WORDS = [
    "java", "spring", "spring boot", "springboot", "kafka", "microservices",
    "sql", "mongo", "mongodb", "oracle", "mysql", "elasticsearch",
    "python", "machine learning", "deep learning", "tensorflow", "agent",
    "react", "node.js",
    "docker", "kubernetes", "aws", "azure", "cloud",
    "project management", "leadership"
]

NOISE_WORDS = {"experience", "responsible", "work", "company", "project", "team"}

nlp = spacy.load("en_core_web_sm")  # loads the small English language model

# PhraseMatcher is a spaCy tool for matching exact phrases (case-insensitive due to attr="LOWER").
# Converting each skill phrase into a Doc object using nlp.make_doc().
# Then telling the matcher to look for those phrases in future texts.
skill_patterns = [nlp.make_doc(skill) for skill in SKILL_WORDS]
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add("SKILL", skill_patterns)


def extract_skills_spacy(text: str) -> Set[str]:
    doc = nlp(text.lower())  # Process the input text into a Doc object.
    keywords: Set[str] = set()

    # Match known skills first
    # Use the matcher to find known skills in the text.
    matches = matcher(doc)
    for match_id, start, end in matches:
        # For each match, extract the span (start and end of the matching keyword) and add it to the result set.
        span = doc[start:end]
        keywords.add(span.text)

    # Extract nouns and proper nouns (potential skills)
    # token.pos_: checks if the word is a NOUN or PROPER NOUN (e.g., "Python", "Engineer")
    # not token.is_stop: filters out common words like “and”, “the”, etc.
    # token.lemma_: gets the base form of the word (e.g., “developing” → “develop”)
    # This is a fallback mechanism to catch new or unknown skills.
    for token in doc:
        if token.pos_ in {"NOUN", "PROPN"} and not token.is_stop and token.is_alpha:
            keywords.add(token.lemma_)

    # Remove short words or anything in the NOISE_WORDS list
    keywords = {kw for kw in keywords if len(kw) > 2 and kw not in NOISE_WORDS}

    return keywords


def refine_skills_llm(text: str, candidate_skills: Set[str]) -> List[str]:
    # Create prompt for LLM
    candidate_str = ", ".join(candidate_skills)
    prompt = f"""
        You are an expert resume analyzer.
        
        Below is a section of a resume:
        \"\"\"{text[:LLM_RESUME_CUT_OFF_CHARS_LENGTH]}\"\"\"
        
        We have already extracted these candidate skills:
        {candidate_str}
        
        Your task is to review the resume section and the candidate list, and do the following:
        - Add any relevant missing skills or qualifications that appear in the text
        - Remove any irrelevant or generic terms
        - Return a **clean, comma-separated list** of refined skills only
        - Do **not write any explanation, code, or formatting instructions** — just output the list
        
        Return format example:
        python, machine learning, aws, docker, tensorflow
        """
    response = run_llm(prompt, max_tokens=LLM_OUTPUT_MAX_TOKENS)
    refined_skills = [skill.strip() for skill in response.split(",") if skill.strip()]
    return refined_skills


def extract_skills(text: str) -> List[str]:
    candidate_skills = extract_skills_spacy(text)
    print(f"candidate_skills: {candidate_skills}")

    refined_skills = refine_skills_llm(text, candidate_skills)
    print(f"refined_skills: {refined_skills}")

    return refined_skills


# Example usage
if __name__ == "__main__":
    sample_text = """
    Experienced software engineer with 5 years in Python and Java development.
    Skilled in AWS, Docker, Kubernetes, and machine learning.
    Familiar with project management and agile methodologies.
    """
    skills = extract_skills(sample_text)
    print("Final extracted skills:", skills)
