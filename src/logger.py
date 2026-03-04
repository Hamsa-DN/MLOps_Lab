import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Pipeline started")
    logger.warning("This is a warning")
    logger.error("An error occurred")