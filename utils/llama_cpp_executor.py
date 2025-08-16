from llama_cpp import Llama

# Load your local phi-2.Q4_K_M.gguf model once
llm = Llama(model_path="models/phi-2.Q4_K_M.gguf")

def run_llm(prompt: str, max_tokens: int = 256) -> str:
    output = llm(prompt, max_tokens=max_tokens, stop=["\n\n"])
    return output['choices'][0]['text'].strip()
