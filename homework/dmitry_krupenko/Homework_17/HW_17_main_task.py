import argparse
import os
import sys
from pathlib import Path
import re


def search_in_file(file_path, search_text, context_words=5):
    """
    Ищет текст (regex) в файле и возвращает результаты с контекстом.
    """
    results = []

    try:
        pattern = re.compile(search_text, re.IGNORECASE)

        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                words = line.split()

                for i, word in enumerate(words):
                    if pattern.search(word):
                        start = max(0, i - context_words)
                        end = min(len(words), i + context_words + 1)

                        context_words_list = words[start:end]
                        context = ' '.join(context_words_list)

                        results.append((line_num, context))

    except UnicodeDecodeError:
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}", file=sys.stderr)
        return []

    return results


def main():
    parser = argparse.ArgumentParser(description="Поиск текста (regex) в лог-файлах")

    parser.add_argument("directory", help="Путь к папке с логами")
    parser.add_argument("--text", required=True, help="Regex для поиска")
    parser.add_argument("-d", "--date", help="Фильтр по дате в имени файла")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Ошибка: Директория '{args.directory}' не существует", file=sys.stderr)
        sys.exit(1)

    directory_path = Path(args.directory)
    search_text = args.text
    found_any = False

    for file_path in directory_path.iterdir():
        if file_path.is_file():

            if args.date and args.date not in file_path.name:
                continue

            results = search_in_file(file_path, search_text)

            if results:
                found_any = True

                print(f"Файл: {file_path.name}")
                print(f"Найдено совпадений: {len(results)}")

                for line_num, context in results:
                    print(f"  Строка {line_num}: ...{context}...")

                print()

    if not found_any:
        print(f"Ничего не найдено по заданным параметрам: {search_text}")


main()
