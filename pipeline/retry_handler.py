from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
import logging

logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(Exception),
    reraise=True
)
def retry_on_failure(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.exception("Function failed despite retries.")
        raise