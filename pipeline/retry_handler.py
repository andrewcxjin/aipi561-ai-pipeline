from tenacity import retry, stop_after_attempt, wait_fixed
from pipeline.llm_runner import run_llm

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def retry_llm_call(prompt):
    return run_llm(prompt)