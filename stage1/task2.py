import logging


def plants_vs_zombies(plant: list[int], zombie: list[int]) -> bool:
    try:
        logging.info(f"Вхідні дані: рослини={plant}, зомбі={zombie}")
        plant_result = 0 + len(plant)
        zombie_result = 0 + len(zombie)
        item = len(plant) if len(plant) == len(zombie) else max(len(plant), len(zombie)) - min(len(plant), len(zombie))
        for i in range(item):
            if plant[i] > zombie[i]:
                plant_result += 1
            if plant[i] < zombie[i]:
                zombie_result += 1

        logging.info(f"Проміжні результати: plant_result={plant_result}, zombie_result={zombie_result}")

        if plant_result == zombie_result:
            if sum(plant) == sum(zombie):
                logging.info("Сили рівні, рослини виграли")
                return True
            result = sum(plant) > sum(zombie)
            logging.info(f"Перевірка суми: {sum(plant)} vs {sum(zombie)}, результат: {result}")
            return result
        result = plant_result > zombie_result
        logging.info(f"Фінальний результат: {result}")
        return result
    except Exception as e:
        logging.error(f"Помилка: {e}")


print(plants_vs_zombies([2, 4, 6, 8], [1, 3, 5, 7]))  # True
print(plants_vs_zombies([2, 4], [1, 3, 5, 7]))  # False
print(plants_vs_zombies([2, 4, 0, 8], [1, 3, 5, 7]))  # True
print(plants_vs_zombies([1, 2, 1, 1], [2, 1, 1, 1]))  # True