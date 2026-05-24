import base64
import random


class Track:

    def __init__(self, title, duration, genre, rating):
        if not title:
            title = "Без названия"
        if duration <= 0:
            duration = 180
        if rating < 0.0 or rating > 5.0:
            rating = 5.0

        self.title = title
        self.duration = duration
        self.genre = genre
        self.rating = rating

    # перевод секунд в нормальное время мм:сс
    def get_formatted_time(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"


class Playlist:

    def __init__(self):
        self.tracks = []  # тут храним треки (динамический массив)
        self.repeat_mode = "none"

    def add_track(self, title, duration, genre, rating):
        new_track = Track(title, duration, genre, rating)
        self.tracks.append(new_track)
        print(f"Добавлен трек: {title}")

    def remove_track(self, index):
        # проверки на пустой список и выход за границы
        if len(self.tracks) == 0:
            print("Ошибка: Плейлист пуст.")
            return
        if index < 0 or index >= len(self.tracks):
            print(f"Ошибка: Индекса {index} нет в списке.")
            return
        removed = self.tracks.pop(index)
        print(f"Удален трек: {removed.title}")

    def shuffle_playlist(self):
        if len(self.tracks) < 2:
            print("Мало треков для перемешивания.")
            return
        random.shuffle(self.tracks)
        print("Плейлист перемешан.")

    def set_repeat(self, mode):
        if mode in ["none", "one", "all"]:
            self.repeat_mode = mode
            print(f"Режим повтора: {mode}")
        else:
            print(f"Ошибка: Неверный режим '{mode}'.")

    # задание 2: загрузка из base64
    def load_from_base64_file(self, filename):
        try:
            self.tracks = []  # чистим старое перед загрузкой
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    # декодируем строку обратно в текст
                    base64_bytes = line.encode("utf-8")
                    decoded_bytes = base64.b64decode(base64_bytes)
                    text_data = decoded_bytes.decode("utf-8")

                    parts = text_data.split(";")
                    if len(parts) == 4:
                        t_title = parts
                        t_duration = int(parts)
                        t_genre = parts
                        t_rating = float(parts)

                        self.tracks.append(Track(t_title, t_duration, t_genre, t_rating))
            print(f"Плейлист загружен из файла: {filename}")
        except FileNotFoundError:
            print(f"Ошибка: Файл '{filename}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    # задание 5: фильтр по жанру
    def filter_by_genre(self, search_genre):
        print(f"\n--- Фильтр по жанру '{search_genre}' ---")
        found_count = 0
        for i, track in enumerate(self.tracks):
            # приводим к нижнему регистру для поиска
            if track.genre.lower() == search_genre.lower():
                print(f" [{i}] {track.title} ({track.get_formatted_time()}) ★{track.rating}")
                found_count += 1
        if found_count == 0:
            print(" Ничего не найдено.")

    def display_playlist(self):
        if len(self.tracks) == 0:
            print("Плейлист пуст.")
            return
        print("\n--- Список треков ---")
        for i, track in enumerate(self.tracks):
            print(f"#{i} {track.title} — {track.genre} ({track.get_formatted_time()}) [★ {track.rating}]")
        print(f"Режим повтора: {self.repeat_mode}")
        print("--------------------")


def run_tests():
    print("=== Старт тестов ===")
    my_playlist = Playlist()

    print("\n1. Добавление треков:")
    my_playlist.add_track("In the End", 216, "Rock", 4.9)
    my_playlist.add_track("Lose Yourself", 326, "Rap", 4.8)
    my_playlist.add_track("Numb", 185, "Rock", 4.7)
    my_playlist.add_track("Believer", 204, "Rock", 4.5)
    my_playlist.display_playlist()

    print("\n2. Режим повтора:")
    my_playlist.set_repeat("one")

    print("\n3. Перемешивание:")
    my_playlist.shuffle_playlist()
    my_playlist.display_playlist()

    print("\n4. Удаление:")
    my_playlist.remove_track(2)
    my_playlist.display_playlist()

    print("\n5. Фильтрация:")
    my_playlist.filter_by_genre("Rock")

    print("\n6. Граничные случаи и ошибки:")
    my_playlist.remove_track(99)
    my_playlist.filter_by_genre("Jazz")
    my_playlist.load_from_base64_file("not_found.txt")

    print("\n Проверка на пустой список:")
    test_empty = Playlist()
    test_empty.remove_track(0)
    test_empty.shuffle_playlist()

    print("\n=== Тесты завершены ===")


if __name__ == "__main__":
    run_tests()
