import logging
import os
from datetime import datetime

log_path = "logs/interactions.log"
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logging.basicConfig(filename=log_path, level=logging.INFO)

def log_interaction(city, prompt, response):
    timestamp = datetime.utcnow().isoformat()
    logging.info(f"[{timestamp}] CITY: {city}")
    logging.info(f"PROMPT: {prompt}")
    logging.info(f"RESPONSE: {response}")
    logging.info("-" * 40)