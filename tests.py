import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollect

    @pytest.mark.parametrize("book_name", [
        "",  # Пустое имя
        "A" * 41,  # Имя длиннее 40 символов
    ])
    def test_add_new_book_invalid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # Тест для установки жанра книги
    @pytest.mark.parametrize("book_name, genre", [
        ("Властелин колец", "Фантастика"),
        ("1984", "Комедии"),
    ])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест для проверки, что некорректный жанр не устанавливается
    @pytest.mark.parametrize("book_name, genre", [
        ("1984", "Несуществующий жанр"),
        ("Мастер и Маргарита", "Триллеры"),
    ])
    def test_set_book_genre_invalid(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == ""

    # Тест для получения жанра несуществующей книги
    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Несуществующая книга") is None

    # Тест для получения списка книг с определённым жанром
    @pytest.mark.parametrize("book_name, genre, expected_books", [
        ("Мастер и Маргарита", "Фантастика", ["Мастер и Маргарита"]),
        ("Золушка", "Мультфильмы", ["Золушка"]),
    ])
    def test_get_books_with_specific_genre(self, book_name, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == expected_books

    # Тест для получения списка книг, подходящих детям
    @pytest.mark.parametrize("book_name, genre, expected_books", [
        ("Золушка", "Мультфильмы", ["Золушка"]),
        ("Оно", "Ужасы", []),
    ])
    def test_get_books_for_children(self, book_name, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == expected_books

    # Тест для добавления книги в избранное
    @pytest.mark.parametrize("book_name", [
        "Маленький принц",
        "Алиса в Стране чудес",
    ])
    def test_add_book_in_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    # Тест для проверки, что книга не добавляется в избранное, если её нет в коллекции
    def test_add_book_in_favorites_nonexistent(self):
        collector = BooksCollector()
        book_name = "Несуществующая книга"
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    # Тест для удаления книги из избранного
    @pytest.mark.parametrize("book_name", [
        "Маленький принц",
        "Алиса в Стране чудес",
    ])
    def test_delete_book_from_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    # Тест для получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер и узник Азкабана"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]