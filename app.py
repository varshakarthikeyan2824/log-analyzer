import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Log analyser application started")
    logger.debug("Loading application configuration")
    logger.warning("This is a sample warning")
    logger.error("This is a sample error")
    logger.info("Log analyser application finished")


if __name__ == "__main__":
    main()
