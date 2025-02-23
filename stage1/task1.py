import logging


# Pythagorean triangle check
def pythagorean_pants(arr: list[int]) -> bool:
    try:
        if len(arr) != 3:
            raise ValueError("Масив повинен містити рівно 3 числа")
        arr.sort()
        result = arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2
        logging.info(f"Перевірка трикутника для {arr}: {result}")
        return result
    except Exception as e:
        logging.error(f"Помилка: {e}")


print(pythagorean_pants([3, 4, 5, 7]))  # ValueError
print(pythagorean_pants([5, 12, 13]))  # True
print(pythagorean_pants([5, 3, 4]))  # True
print(pythagorean_pants([6, 8, 10]))  # True
print(pythagorean_pants([100, 3, 65]))  # False
