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
        assert len(collector.books_genre.keys()) == 2

    # --------------------------------------- М О И  Т Е С Т Ы ------------------------------------------------------------

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1. добавление 5 книг
    def test_add_new_book_add_five_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Как воспитать послушного зомби')
        collector.add_new_book('Рецепты для маленьких зомби')
        collector.add_new_book('Эволюция зомби')

        assert len(collector.books_genre.keys()) == 5

    # 2. установка жанра
    def test_set_book_genre_sets_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    # 3. получение  жанра книги по её имени
    def test_set_book_genre_get_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # 4. выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_returns_books_with_given_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Фантастика")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Комедии")

        result = collector.get_books_with_specific_genre("Фантастика")

        assert sorted(result) == ["Книга1", "Книга2"]

    # 5. получаем словарь books_genre
    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")

        assert collector.get_books_genre() == {"Книга": ""}

    # 6. Книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children_only(self):
        collector = BooksCollector()

        collector.add_new_book("Приключения Буратино")
        collector.set_book_genre("Приключения Буратино", "Мультфильмы")

        collector.add_new_book("Волшебник Изумрудного города")
        collector.set_book_genre("Волшебник Изумрудного города", "Мультфильмы")

        collector.add_new_book("Очень страшное кино XVII")
        collector.set_book_genre("Очень страшное кино XVII", "Ужасы")

        collector.add_new_book("Plants vs Zombies")
        collector.set_book_genre("Plants vs Zombies", "Фантастика")

        assert collector.get_books_for_children() == ["Приключения Буратино", "Волшебник Изумрудного города",
                                                      "Plants vs Zombies"]

    # 7. У добавленной книги нет жанра
    def test_set_book_genre_sets_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Очень страшное кино XVII")
        collector.set_book_genre("Очень страшное кино XVII", "Ужасы")

        collector.add_new_book('Анатомия и болезни зомби')
        collector.set_book_genre('Анатомия и болезни зомби', "Медицина")

        collector.add_new_book("Приключения Буратино")
        collector.set_book_genre("Приключения Буратино", "Мультфильмы")

        # получаем все книги что добавили
        all_books = collector.get_books_genre()

        # считаем количество книг без жанра
        without_genre_cnt = 0

        for book in all_books.keys():
            if not collector.get_book_genre(book):
                without_genre_cnt += 1

        assert without_genre_cnt == 1

    # 8. добавляем книгу в Избранное без двойного добавления
    def test_add_book_in_favorites_adds_only_once(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books() == ["Книга"]

    # 9. удаляем книгу из Избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert collector.get_list_of_favorites_books() == []

    # 10. получаем список Избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books() == ["Книга"]
