import logging
import re
from datetime import datetime

from log_analyser.models import LogEntry

logger = logging.getLogger(__name__)

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2}) "
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) "
    r"(?P<message>.+)$"
)


def parse_line(line: str) -> LogEntry | None:
    match = LOG_PATTERN.match(line.strip())

    if not match:
        logger.warning("Malformed log line: %s", line.strip())
        return None

    try:
        timestamp = datetime.strptime(
            match.group("timestamp"),
            "%Y-%m-%d %H:%M:%S",
        )
    except ValueError:
        logger.warning("Invalid timestamp: %s", line.strip())
        return None

    return LogEntry(
        timestamp=timestamp,
        level=match.group("level"),
        message=match.group("message"),
    )
