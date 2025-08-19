import tempfile
import json
from parser import parse_logs


def test_parse_logs_no_filter():
    data = [
        {"@timestamp": "2025-06-22T13:57:32+00:00",
         "url": "/api/test",
         "response_time": 0.1},
        {"@timestamp": "2025-06-22T13:57:33+00:00",
         "url": "/api/test",
         "response_time": 0.2},
    ]

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        for d in data:
            f.write(json.dumps(d) + "\n")
        f.flush()
        logs = parse_logs(f.name)

    assert len(logs) == 2
    assert logs[0]["url"] == "/api/test"


def test_parse_logs_with_date_filter():
    data = [
        {"@timestamp": "2025-06-22T13:57:32+00:00",
         "url": "/api/a",
         "response_time": 0.1},
        {"@timestamp": "2025-06-23T13:57:33+00:00",
         "url": "/api/b",
         "response_time": 0.2},
    ]

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        for d in data:
            f.write(json.dumps(d) + "\n")
        f.flush()
        logs = parse_logs(f.name, date_filter="2025-06-22")

    assert len(logs) == 1
    assert logs[0]["url"] == "/api/a"
