import json
import logging

# настроим базовое логирование (можно заменить на конфигурацию из main.py)
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def parse_logs(file_path, date_filter=None):
    """
    Читает лог-файл построчно и возвращает список словарей.
    Если указана date_filter (YYYY-MM-DD), то фильтруем по дате.
    """
    logs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            try:
                log = json.loads(line)
                if date_filter:
                    if not log.get("@timestamp", "").startswith(date_filter):
                        continue
                logs.append(log)
            except json.JSONDecodeError:
                logging.warning(f"Файл {file_path}, строка {line_no}: \
                                не удалось распарсить JSON -> {line.strip()}")
                continue
    return logs
