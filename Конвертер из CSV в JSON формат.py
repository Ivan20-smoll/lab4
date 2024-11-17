# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
  """
  Считывает содержимое CSV файла и сериализует в файл JSON с отступами.
  """
  with open(INPUT_FILENAME, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

  with open(OUTPUT_FILENAME, 'w') as outfile:
    json.dump(data, outfile, indent=4)


if __name__ == '__main__':
  # Нужно для проверки
  task()

  with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
      print(line, end="")
