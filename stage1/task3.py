from datetime import datetime, timedelta
from typing import List
import logging

logging.basicConfig(level=logging.INFO)


def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> List[datetime]:
    schedule = []
    current_date = start_date

    try:
        while len(schedule) < days:
            for _ in range(work_days):
                if len(schedule) < days:
                    schedule.append(current_date)
                    logging.info(f"Додано робочий день: {current_date}")
                    current_date += timedelta(days=1)

            current_date += timedelta(days=rest_days)
            logging.info(f"Пропущено дні відпочинку, наступний робочий день: {current_date}")
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")

    return schedule


# Перевірка
print(generate_schedule(5, 2, 1, datetime(2024, 1, 30)))

