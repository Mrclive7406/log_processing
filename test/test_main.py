import subprocess
import sys
import tempfile
import json
import os


def test_main_script_runs():
    """Проверяем что main.py запускается и печатает отчет"""
    log_entry = {
        "@timestamp": "2025-06-22T13:57:32+00:00",
        "url": "/api/test",
        "response_time": 0.1,
    }

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(json.dumps(log_entry) + "\n")
        log_file = f.name

    result = subprocess.run(
        [sys.executable, "main.py", "--file", log_file, "--report", "average"],
        capture_output=True,
        text=True,
    )

    os.unlink(log_file)  # удаляем временный файл

    assert result.returncode == 0
    assert "/api/test" in result.stdout
