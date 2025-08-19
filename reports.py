from collections import defaultdict


def generate_report(logs):
    """
    Формирует отчет по эндпоинтам:
    - количество запросов
    - среднее время ответа
    Возвращает список для tabulate
    """
    stats = defaultdict(lambda: {"count": 0, "sum_time": 0.0})

    for log in logs:
        url = log.get("url")
        response_time = log.get("response_time", 0.0)

        stats[url]["count"] += 1
        stats[url]["sum_time"] += response_time

    report = []
    for url, data in stats.items():
        avg_time = data["sum_time"] / data["count"] if data["count"] > 0 else 0
        report.append([url, data["count"], round(avg_time, 3)])

    return sorted(report, key=lambda x: x[0])
