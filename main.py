import argparse
from tabulate import tabulate
from parser import parse_logs
from reports import generate_report


def main():
    parser = argparse.ArgumentParser(description="Log file analyzer. "
                                                 "Анализатор лог файлов")
    parser.add_argument("--file",
                        nargs="+",
                        required=True,
                        help="Path to log file. Путь к лог файлам")
    parser.add_argument("--report",
                        required=True,
                        choices=["average"],
                        help="Report type")
    parser.add_argument("--date",
                        help="Filter logs by date (YYYY-MM-DD)")

    args = parser.parse_args()

    logs = []
    for file_path in args.file:
        logs.extend(parse_logs(file_path,
                               date_filter=args.date))

    if not logs:
        print("No logs found for the given filters."
              "Логи для данных фильтров не найдены")
        return

    if args.report == "average":
        table = generate_report(logs)
        print(tabulate(table, headers=["Endpoint",
                                       "Requests",
                                       "Avg Response Time"], tablefmt="grid"))


if __name__ == "__main__":
    main()
