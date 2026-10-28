import json
import logging
from pathlib import Path

from log_analyser.analyser import analyse_log

logging.basicConfig(level=logging.INFO)


def main() -> None:
    result = analyse_log(Path("data/messy.log"))

    output_file = Path("output/summary.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)

    logging.info("Summary saved to %s", output_file)


if __name__ == "__main__":
    main()
