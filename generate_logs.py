import logging
from pathlib import Path

log_file = Path("data/messy.log")
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)

logging.info("Application started")
logging.warning("High memory usage")
logging.error("Database connection failed")
logging.error("Database connection failed")
logging.info("User login successful")
logging.error("Authentication failed")
logging.debug("Processing request")
logging.warning("Disk space running low")

logging.shutdown()

# Add two malformed lines for testing.
with log_file.open("a", encoding="utf-8") as file:
    file.write("INVALID LOG ENTRY\n")
    file.write("Something went wrong\n")

logging.info(f"Logs generated at: {log_file}")
