from pipeline.prompt_builder import build_prompt
from pipeline.llm_runner import run_llm
from pipeline.retry_handler import retry_on_failure
from pipeline.logger import log_interaction
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    city = input("Enter your destination city: ").strip()
    duration = input("How long is your trip? (in days) ").strip()

    prompt = build_prompt(city, duration)
    print("\n🧠 Sending prompt to local LLM...\n")

    try:
        response = retry_on_failure(run_llm, prompt)
        print("\n🎒 Suggested Packing List:\n", response)
        log_interaction(city, prompt, response)
    except Exception as e:
        print("❌ LLM failed after multiple retries:", e)

if __name__ == "__main__":
    main()
