import logging
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from log_analyser.exceptions import LogFileError
from log_analyser.parser import parse_line

logger = logging.getLogger(__name__)


def analyse_log(file_path: Path) -> dict[str, Any]:
    counts: Counter[str] = Counter()
    errors: Counter[str] = Counter()
    timestamps: list[datetime] = []
    bad_lines = 0

    try:
        with file_path.open("r", encoding="utf-8") as file:
            for line in file:
                entry = parse_line(line)

                if entry is None:
                    bad_lines += 1
                    continue

                level = entry.level
                message = entry.message

                counts[level] += 1
                timestamps.append(entry.timestamp)

                if level == "ERROR":
                    errors[message] += 1

    except OSError as error:
        logger.error("Unable to read log file %s: %s", file_path, error)
        raise LogFileError(f"Unable to read log file: {file_path}") from error

    logger.info(
        "Analysed %s; found %d malformed lines",
        file_path,
        bad_lines,
    )

    return {
        "counts_by_level": dict(counts),
        "top_errors": [
            {"message": message, "count": count}
            for message, count in errors.most_common(5)
        ],
        "time_range": {
            "start": min(timestamps).isoformat() if timestamps else None,
            "end": max(timestamps).isoformat() if timestamps else None,
        },
        "bad_lines": bad_lines,
    }
