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
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'book_name',
        [
            '1',
            'Название книги 26 симловов',
            'В названии этой книги 40 символовввввввв'
        ]
    )
    def test_add_new_book_three_books_successfully(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre(), \
            'Книга не добавлена в словарь books_genre'

    @pytest.mark.parametrize(
        'book_name',
        [
            '',
            'В названии этой книги 41 символлллллллллл'
        ]
    )
    def test_add_new_book_name_book_0_and_41_characters(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre(), \
            'Книга не должна быть добавлена. Название книги отсутствует или превышает 40 символов'

    def test_set_book_genre_for_book_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Семь смертей Эвелины Хардкасл')
        collector.set_book_genre('Семь смертей Эвелины Хардкасл', 'Детективы')
        assert collector.get_book_genre('Семь смертей Эвелины Хардкасл') == 'Детективы', \
            f'Жанр для книги не установлен'

    def test_set_book_genre_for_not_added_books(self):
        collector = BooksCollector()
        collector.set_book_genre('Алладин', 'Мультфильмы')
        assert collector.get_book_genre('Алладин') != 'Мультфильмы', \
            'Установлен жанр для не существующей книги'

    def test_set_book_genre_no_genre_listed(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Триллеры')
        assert 'Триллеры' not in collector.get_books_genre(), \
            'Установлен не существующий жанр'

    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        assert collector.get_book_genre('Алладин') == 'Мультфильмы', \
            'Жанр книги не соответствует её названию'

    def test_books_with_genre_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('Алладин')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert 'Алладин' not in collector.get_books_with_specific_genre('Комедии'), \
            'У книги "Алладин" жанр не соответствует "Комедии"'

    def test_get_books_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        assert collector.get_books_genre() == {'Десять негритят': 'Детективы', 'Алладин': 'Мультфильмы'}, \
            "Не все книги были добавлены"

    @pytest.mark.parametrize(
        'book_name, genre_name',
        [
            ['Чип и Дэйл', 'Мультфильмы'],
            ['Горе от ума', 'Комедии'],
            ['Дюна', 'Фантастика']
        ]
    )
    def test_books_for_children_successfully(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_books_for_children() == [book_name], \
            "Книга подходит для детей"

    @pytest.mark.parametrize(
        'book_name, genre_name',
        [
            ['Дракула', 'Ужасы'],
            ['Семь смертей Эвелины Хардкасл', 'Детективы']
        ]
    )
    def test_books_for_children_age_restrictions(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_books_for_children() == [], \
            "Книга имеет возрастные ограничения и не подходит для детей"

    def test_add_book_in_favorites_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Алладин')
        collector.add_book_in_favorites('Алладин')
        assert collector.get_list_of_favorites_books() == ['Алладин']

    def test_add_book_in_favorites_book_not_add(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Дракула')
        assert collector.get_list_of_favorites_books() != ['Дракула'], \
            'Книга не может быть добавлена в "Избранное", так как она отсутствует в добавленных книгах'

    def test_add_book_in_favorites_book_is_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Пигмалион')
        collector.add_book_in_favorites('Пигмалион')
        collector.add_book_in_favorites('Пигмалион')
        favorites_books = collector.get_list_of_favorites_books()
        assert favorites_books == ['Пигмалион'], \
            "Книга уже добавлена в избранное"

    def test_delete_book_from_favorites_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Пигмалион')
        collector.add_book_in_favorites('Пигмалион')
        collector.delete_book_from_favorites('Пигмалион')
        favorites_books = collector.get_list_of_favorites_books()
        assert favorites_books == [], "Книга не удалена из избранного"
