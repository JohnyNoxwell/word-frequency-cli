import os
import argparse
import requests


def get_content(source):
    # Проверяем, является ли источник ссылкой
    if source.startswith(("http://", "https://")):
        print(f"--- Загрузка данных из сети: {source} ---")
        try:
            response = requests.get(source, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as http_err:
            print(f"Ошибка HTTP (например, 404): {http_err}")
        except requests.exceptions.ConnectionError:
            print("Ошибка соединения: проверьте интернет или адрес.")
        except requests.exceptions.Timeout:
            print("Превышено время ожидания ответа.")
        except requests.exceptions.RequestException as e:
            print(f"Произошла непредвиденная ошибка при запросе: {e}")
            return None

    # Иначе считаем, что это путь к файлу
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, source)
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл {file_path} не найден.")
            return None
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()


# В блоке argparse теперь можно просто принимать один аргумент 'path'
# который может быть и путем, и ссылкой.
def word_frequency(text):
    counts = {}
    words = text.split()

    for word in words:
        clean_word = word.strip(",.!?;:\"'()[]{}").lower()

        if not clean_word:
            continue

        if clean_word in counts:
            counts[clean_word] += 1
        else:
            counts[clean_word] = 1

    return counts


def main():
    parser = argparse.ArgumentParser(description="Word frequency analyzer")
    parser.add_argument("file", help="Path to text file")
    parser.add_argument("--top", type=int, default=10, help="Top N words")

    args = parser.parse_args()

    source = args.file
    top_n = args.top

    text = get_content(source)
    if text is None:
        print("Не удалось получить текст. Анализ невозможен.")
        return
    freq = word_frequency(text)

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

    for word, count in sorted_freq:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
