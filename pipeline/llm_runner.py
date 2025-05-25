import ollama

def run_llm(prompt, model):
    response = ollama.chat(model='llama2', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']