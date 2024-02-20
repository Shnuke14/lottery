## импорт рандома
import random

## Задание функции "лотерея"
def lottery():
  ## Количество чисел +1
  for i in range(4):
    ## Промежуток в котором будут генерироваться числа
    yield random.randint(1, 40)

  ## Возвращает последнее число от 1 до 15
  yield random.randint(1, 15)


for random_number in lottery():
  print("And the next number is... %d" %(random_number))