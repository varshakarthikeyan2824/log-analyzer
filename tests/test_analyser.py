from datetime import datetime

from log_analyser.parser import parse_line


def test_parse_valid_line() -> None:
    result = parse_line("2026-10-28 16:00:00 ERROR Database connection failed")

    assert result is not None
    assert result.level == "ERROR"
    assert result.message == "Database connection failed"
    assert result.timestamp == datetime(2026, 10, 28, 16, 0, 0)


def test_parse_malformed_line() -> None:
    result = parse_line("INVALID LOG ENTRY")

    assert result is None


def test_parse_invalid_timestamp() -> None:
    result = parse_line("2026-99-99 16:00:00 ERROR Invalid date")

    assert result is None
