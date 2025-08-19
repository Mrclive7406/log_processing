from reports import generate_report


def test_generate_report_average():
    logs = [
        {"url": "/api/test", "response_time": 0.1},
        {"url": "/api/test", "response_time": 0.3},
        {"url": "/api/other", "response_time": 0.2},
    ]

    report = generate_report(logs)

    # Проверим что два эндпоинта
    urls = [row[0] for row in report]
    assert "/api/test" in urls
    assert "/api/other" in urls

    # Проверим среднее для /api/test
    for url, count, avg in report:
        if url == "/api/test":
            assert count == 2
            assert avg == 0.2  # (0.1 + 0.3) / 2
