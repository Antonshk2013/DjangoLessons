import os
from datetime import timedelta

import django
from django.db.models.functions import TruncMonth
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# ИМПОРТЫ НАШЕГО ФУНКЦИОНАЛА ДОЛЖНЫ БЫТЬ СТРОГО ПОСЛЕ СИСТЕМНОЙ НАСТРОЙКИ ВЫШЕ
from src.library.models import Book, Category, Author, Post, Borrow, book
from src.users.models import User
from src.choices.base import Genre

from django.db.models.query import QuerySet
from django.db.models import Q, F, Count, Avg, Min, Max

# books = Book.objects.all()
#
#
# print(books)
# print(books[0].title)


# pub = User.objects.get(username='ich1')
# author = Author.objects.get(last_name='Sapkowski')
# cat = Category.objects.get(pk=4)

# new_book = Book(
#     title='Test Book from ORM system',
#     genre=Genre.FANTASY,
#     pages=215,
#     publisher=pub,
#     author=author,
#     category=cat,
# )
#
# new_book.save()

# print(new_book)
# print(new_book.title)
# print(new_book.genre)
# print(new_book.publisher)
# print(new_book.author)
# print(new_book.category)


# pub = User.objects.get(username='ich1')
# author = Author.objects.get(last_name='Sapkowski')
# cat = Category.objects.get(pk=5)
#
# new_book = Book.objects.create(
#     title='NEW BOOK',
#     genre=Genre.BIOGRAPHY,
#     pages=400,
#     publisher=pub,
#     author=author,
#     category=cat,
# )
#
# print(new_book)
# print(new_book.genre)
# print(new_book.publisher)
# print(new_book.author)
# print(new_book.category)


# books: QuerySet = Book.objects.all()
#
# print(type(books))
# print(books)
#
# print(books.query)
#
# for i in range(5):
#     print(books[i].title)

# first_book: Book = Book.objects.first()
#
# print(first_book)


# last_book: Book = Book.objects.last() # The Witcher: The Last Wish
#
# print(last_book)

# latest_book: Book = Book.objects.latest() # The Witcher: The Last Wish
#
# print(latest_book)


# books_count = Book.objects.count()
#
# print(f"Кол-во книг в базе = {books_count}")




# books_exists: bool = Book.objects.all().exists()
#
# print(f"Набор данных наполнен - {books_exists}")

#
# books: QuerySet = Book.objects.values(
#     'title',
#     'genre',
#     'published_date',
#     'language'
# )
#
#
# print(books.query)
#
# for i in range(10):
#     print(
#         books[i]['title'],
#         books[i]['genre'],
#         books[i]['published_date'],
#         books[i]['language']
#     )

# filtered_books: QuerySet = Book.objects.filter(
#     genre='BIOGRAPHY',
#     publisher_id=2
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     genre__in=[Genre.FANTASY, Genre.BIOGRAPHY],
#     publisher_id__in=[17, 25, 35, 43, 50, 20]
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     title__iexact='the' # the The THE
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     title__istartswith='the' # the The THE
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     title__icontains='the' # the The THE
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     pages__gt=250,
#     pages__lte=500
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     published_date__gt="2023-04-01"
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     description__isnull=True
# )
#
# print(filtered_books.query)
# print(filtered_books)


# filtered_books: QuerySet = Book.objects.filter(
#     published_date__range=["2023-01-01", "2023-12-31"]
# )
#
# print(filtered_books.query)
# print(filtered_books.count())



# filtered_books: QuerySet = Book.objects.filter(
#     description__isnull=True,
#     category_id=5
# )
#
# print(filtered_books.query)
# print(filtered_books.count())

# filtered_books: QuerySet = Book.objects.filter(
#     Q(description__isnull=True) & ~Q(category_id=5)
# )
#
# print(filtered_books.query)
# print(filtered_books)



# filtered_books: QuerySet = Post.objects.filter(
#     ~Q(moderated=True) | (Q(title__istartswith='F') & Q(author_id=21))
# )
#
# print(filtered_books.query)
# print(filtered_books)



# req_author: Author = Author.objects.get(
#     last_name='Sapkowski',
#     first_name='Andrzej'
# )
#
# print(req_author)
#
# print(req_author.rating)
#
#
# req_author.rating = 9.5
#
# req_author.save()


# req_authors = Author.objects.filter(
#     rating__lt=8
# )
#
# req_authors.update(rating=8.2)  # UPDATE table SET rating=8.2 WHERE rating < 8;
#
# req_authors.update()


# req_authors = Author.objects.filter(
#     rating__lt=8.5
# )
#
# print(req_authors.query)
#
# req_authors.update(rating=F('rating') * 0.90)  # UPDATE table SET rating=8.2 WHERE rating < 8;
#
# req_authors.update(discounted_price=F('price') * 0.85)
#
#
# Book.objects.filter(
#     discounted_price__lt=F('price')
# )


# req_obj = Book.objects.get(title='Test Book from ORM system')
#
# print(type(req_obj))
#
# deleted_obj = req_obj.delete()
#
# req_obj.save()

# ## Задача 1: Создание нового пользователя
# 1. Создать нового пользователя с username='new_user'
# 2. Установить обязательные поля: email='new_user@test.com', role='reader'
# 3. Добавить дополнительные данные: first_name='John', last_name='Doe', gender='male', age=25
# 4. Сохранить в базе данных

# new_user = User.objects.create(
#     username = 'AntonShk',
#     email='antonshk2013@gmail.com',
#     role=Role.reader,
#     first_name='Anton',
#     last_name='Shkarupa',
#     gender=Gender.male,
#     age=37)

# new_user = User.objects.get(username='Antonshk')
#
# new_user.set_password('QWERTY1234!')
# new_user.save()
#
# print(new_user)

# ## Задача 2: Получение конкретного автора и обновление рейтинга
# **ТЗ:**
# 1. Найти автора с id=1 (Andrzej Sapkowski)
# 2. Обновить его рейтинг на 9.5
# 3. Сохранить изменения в базе данных

# author = Author.objects.get(id=3)
# print(author.rating)
# print(author)
# author.rating = 9.5
# author.save()
# print(author.rating)


## Задача 3: Фильтрация книг по жанру и языку с подсчетом
# **ТЗ:**
# 1. Найти все книги жанра 'FICTION' на английском языке
# 2. Подсчитать количество таких книг
# 3. Проверить, существуют ли такие книги в базе
#
#
# books = Book.objects.filter(Q(genre=Genre.FICTION.value) & Q(language=Language.en.name))
# print(books.count())
# print(books.exists())


## Задача 4: Поиск пользователей с использованием Q-объектов
# **ТЗ:**
# 1. Найти всех пользователей, которые являются либо администраторами, либо сотрудниками
# 2. Исключить неактивных пользователей
# 3. Отсортировать по дате регистрации (новые первыми)

# users = User.objects.filter(
#     Q(role=Role.admin.value)
#     | Q(role=Role.employee.value)
#     & Q(is_active=False)).order_by('-date_joined')
## Задача 5: Поиск авторов с использованием field lookups
# **ТЗ:**
# 1. Найти всех авторов, чье имя начинается с 'A'
# 2. Найти авторов с рейтингом выше 8.5
# 3. Найти авторов, родившихся после 1950 года
# 4. Получить первого автора из результата

# authors = Author.objects.filter(first_name__startswith='A')
# authors_rating = Author.objects.filter(rating__gt=8.5)
# authors_birth_days = Author.objects.filter(birth_date__gt=1950).first()

# new_categories = [
#     Category(title='Детективы'),
#     Category(title='Биографии'),
#     Category(title='Поэзия'),
#     Category(title='Учебники'),
#     Category(title='Справочники')
# ]
#
# Category.objects.bulk_create(new_categories)
# Массовое обновление пользователей
# **ТЗ:**
# 1. Найти всех пользователей с ролью 'reader'
# 2. Массово обновить их статус is_staff на True
# 3. Использовать bulk_update для оптимизации
#
# users = User.objects.filter(role=Role.reader.value)
# for user in users:
#     user.is_staff = True
# User.objects.bulk_update(users, ['is_staff'])

# ## Задача 11: Создание связи пользователя с библиотекой через промежуточную модель
# **ТЗ:**
# 1. Найти пользователя с id=15
# 2. Найти библиотеку с id=2
# 3. Создать запись в промежуточной модели LibrariesMembers для связи пользователя с библиотекой
# 4. Проверить, что запись была создана успешно

# user15 = User.objects.get(pk=15)
# library2 = Library.objects.get(pk=2)
#
# library_member = LibrariesMembers.objects.create(member=user15, library=library2)
# print(library_member.id)


## Задача 13: Массовое обновление статуса займов
# **ТЗ:**
# 1. Найти все займы с return_date до 2022-01-01 включительно
# 2. Среди них найти те, которые еще не помечены как возвращенные
# 3. Массово обновить их статус is_returned на True
# 4. Подсчитать количество обновленных записей
#
# borrows = Borrow.objects.filter(Q(return_date__lte='2022-01-01') & Q(is_returned=False))
# borrows.update(is_returned=True)

## Задача 15: Поиск библиотек с фильтрацией по местоположению
# **ТЗ:**
# 1. Найти все библиотеки, в названии которых есть слово "Central" (регистронезависимо)
# 2. Найти библиотеки, расположенные в городах, содержащих "New" в названии
# 3. Объединить результаты с помощью Q-объектов
# 4. Исключить библиотеки без веб-сайта

# central_libraries = Library.objects.filter(
#     Q(name__icontains="Central")
#     & Q(location__icontains="New")
#     & Q(website__isnull=False))
# print(central_libraries)

## Задача 16: Сложная фильтрация авторов по активности и рейтингу
# **ТЗ:**
# 1. Найти активных авторов с рейтингом от 8.0 до 9.5 включительно
# 2. Среди них найти тех, кто родился в XX веке (1901-2000 годы)
# 3. Исключить авторов без указанной даты рождения
# 4. Получить только первые 10 результатов

# authors_report = Author.objects.filter(
#     Q(rating__gte=8.0)
#     & Q(rating__lte=9.5)
#     & Q(birth_date__year__range=(1901, 2000))
#     & ~Q(birth_date=None)
# )[:10]
# print(authors_report)

# ## Задача 17: Создание и поиск категорий с проверкой дубликатов
# **ТЗ:**
# 1. Проверить, существует ли категория с названием "Фантастика"
# 2. Если не существует - создать новую категорию
# 3. Если существует - получить существующую категорию
# 4. Вывести информацию о категории и количестве связанных книг

# fantastic_category_exists = Category.objects.filter(title="Фантастика").exists()
# if fantastic_category_exists:
#     fantastic_category=Category.objects.get(title="Фантастика")
# else:
#     fantastic_category=Category.objects.create(title="Фантастика")
# print(fantastic_category.books)


# ## Задача 18: Поиск пользователей с множественными условиями
# **ТЗ:**
# 1. Найти пользователей женского пола в возрасте от 25 до 45 лет
# 2. Среди них найти тех, кто зарегистрировался в 2023 году
# 3. Исключить неактивных пользователей
# 4. Получить только тех, у кого указан номер телефона

# users_report = User.objects.filter(
#     Q(age__range=(25, 45))
#     & Q(date_joined__year=2023)
#     & Q(is_active=True)
#     & ~Q(phone=None)
# )

# ## Задача 19: Массовое создание библиотечных записей
# **ТЗ:**
# 1. Найти всех пользователей с ролью 'reader'
# 2. Найти библиотеку с id=1
# 3. Создать массово записи LibraryRecord для связи этих пользователей с библиотекой
# 4. Исключить пользователей, которые уже связаны с этой библиотекой
#
# users_readers = User.objects.filter(role=Role.reader.value)
# library_1 = Library.objects.get(pk=1)
# library_members_list = [LibraryRecord(member=user, library=library_1) for user in users_readers ]
# LibraryRecord.objects.bulk_create(library_members_list)

# ## Задача 20: Сложный поиск займов с временными условиями
# **ТЗ:**
# 1. Найти все займы, сделанные в 2022 году
# 2. Среди них найти те, которые были возвращены вовремя (до или в дату return_date)
# 3. Исключить займы без указанной даты возврата
# 4. Сгруппировать результаты по месяцам и посчитать количество в каждом месяце

# borrows_repport = Borrow.objects.filter(
#     Q(borrow_date__year=2022)
#     & Q(return_date__lte=timezone.now())
#     & Q(return_date__isnull=False)
# ).annotate(
#     month=TruncMonth("borrow_date")
# ).values("month").annotate(
#     count=Count("id")
# )
# print(borrows_repport)


# ## Задача 21: Поиск книг по связанным моделям с множественными условиями
# **ТЗ:**
# 1. Найти все книги, написанные авторами с рейтингом выше 7.5
# 2. Среди них найти те, которые опубликованы пользователями с ролью 'admin' или 'employee'
# 3. Исключить книги без автора и без издателя
# 4. Отсортировать по дате публикации (новые первыми)
# ## Задача 21
# books_report = Book.objects.filter(
#     Q(author__rating__gt=7.5)
#     & (Q(publisher__role=Role.admin.value) | Q(publisher__role=Role.employee.value))
#     & (Q(author__isnull=False) | Q(publisher__isnull=False))).order_by('-published_date')
# for book in books_report:
#     print(book.published_date)


## Задача 22: Создание постов с валидацией и связями
# **ТЗ:**
# 1. Найти активного автора с наивысшим рейтингом
# 2. Создать для него 3 поста с разными заголовками
# 3. Проверить, что все посты были созданы успешно
# 4. Получить общее количество постов этого автора

# author_max_rating = Author.objects.all().order_by('-rating').first()
# posts = [
#     Post(title="простой заголовок" ,author=author_max_rating),
#     Post(title="такой себе заголовок" ,author=author_max_rating),
#     Post(title="сложный заголовок" ,author=author_max_rating),
# ]
#
# Post.objects.bulk_create(posts)
#
# author = Post.objects.filter(author__pk=author_max_rating.id).count()

## Задача 23: Сложная фильтрация займов по датам и статусам
# **ТЗ:**
# 1. Найти займы, сделанные в последние 6 месяцев от текущей даты
# 2. Среди них найти те, которые должны были быть возвращены более 30 дней назад
# 3. Исключить уже возвращенные займы
# 4. Получить информацию о библиотеке и пользователе для каждого займа
#
# ## Задача 23:
# borrows_repport = Borrow.objects.filter(
#     # Q(borrow_date__gte=timezone.now()-timedelta(days=180))
#     # & Q(return_date__lte=timezone.now()-timedelta(days=30))
#     # & Q(is_returned=False)
# ).values('book__libraries', 'library_record__member')
# for borrow in borrows_repport:
#     print(borrow)

## Задача 24: Массовое обновление авторов с условной логикой
# **ТЗ:**
# 1. Найти всех авторов без указанной даты рождения
# 2. Найти авторов с рейтингом ниже 5.0
# 3. Объединить эти группы с помощью Q-объектов
# 4. Массово установить им рейтинг 5.0 и статус is_active=False

# report_authors = Author.objects.filter(
#     Q(birth_date__isnull=True)
#     & Q(rating__lt=5.0)
# )
# print(report_authors.count())
#
# ## Задача 25: Поиск пользователей по активности в библиотеках
# **ТЗ:**
# 1. Найти всех пользователей, которые связаны с более чем одной библиотекой
# 2. Среди них найти тех, кто имеет активные займы (не возвращенные)
# 3. Исключить пользователей с ролью 'admin'
# 4. Отсортировать по дате регистрации
#
# ## Задача 26: Создание связей между книгами и библиотеками
# **ТЗ:**
# 1. Найти все книги жанра 'SCIENCE_FICTION'
# 2. Найти библиотеки, в названии которых есть слово "Tech"
# 3. Создать связи many-to-many между этими книгами и библиотеками
# 4. Проверить, что связи были созданы
#
# ## Задача 27: Анализ займов по временным периодам
# **ТЗ:**
# 1. Найти все займы за 2023 год
# 2. Разделить их на кварталы (Q1: янв-март, Q2: апр-июнь, Q3: июль-сен, Q4: окт-дек)
# 3. Для каждого квартала посчитать количество займов и возвратов
# 4. Найти квартал с наибольшей активностью
#
# ## Задача 28: Поиск и создание категорий с иерархией
# **ТЗ:**
# 1. Проверить существование категорий: "Классическая литература", "Современная проза", "Детская литература"
# 2. Создать отсутствующие категории
# 3. Найти книги без категории и присвоить им категорию "Без категории"
# 4. Вывести статистику по количеству книг в каждой категории
#
# ## Задача 29: Сложный поиск с множественными связями
# **ТЗ:**
# 1. Найти пользователей, которые зарегистрированы в библиотеках с веб-сайтом
# 2. Среди них найти тех, кто брал книги автора с рейтингом выше 8.0
# 3. Исключить пользователей младше 21 года
# 4. Получить уникальный список таких пользователей
#
# ## Задача 30: Комплексная работа с датами и статусами
# **ТЗ:**
# 1. Найти все займы, которые были сделаны в выходные дни (суббота/воскресенье)
# 2. Среди них найти те, которые длились более 45 дней
# 3. Проверить статус возврата и подсчитать просроченные
# 4. Создать отчет по библиотекам с наибольшим количеством проблемных займов
#
# from rest_framework import serializers
# class CustomerSerialiyersClass(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     age = serializers.IntegerField(min_value=0)
#     is_active = serializers.BooleanField()
#     created_at = serializers.DateTimeField()
#
#
# customer_serializer = CustomerSerialiyersClass(
#     data={
#         "name": "Anton",
#         "age": 30,
#         "is_active": True,
#         "created_at": timezone.now()
#     }
# )

# ### **Задача 6: Топ-5 читателей по количеству активных займов**
# # **ТЗ:** Найти 5 пользователей с наибольшим количеством невозвращенных книг
#
# report = User.objects.annotate(borg_count=Count('borrows')).order_by('-borg_count')[:5]
# print(report.query)
# for i in report:
#     print(f"{i.username} {i.borg_count}")


# ### **Задача 1: Общее количество книг и их средняя цена**
# **ТЗ:** Получить общее количество книг в базе данных и среднюю цену всех книг в одном запросе
#
# report = Book.objects.aggregate(
#     count=Count('id'),
#     average_page=Avg('pages'),
# )
#
# print(f"Count books: {report['count']}")
# print(f"Averege pages: {round(report['average_page'])}")

### **Задача 2: Диапазон цен и общее количество страниц**
# **ТЗ:** Найти минимальную, максимальную цену книг и общее количество страниц всех книг

# report = Book.objects.aggregate(
#     min_price=Min('price'),
#     max_price=Max('price'),
#     count_pages=Count('pages')
# )
#
# print(report)


### **Задача 7: Библиотеки с общим количеством страниц и средней ценой книг**
# **ТЗ:** Для каждой библиотеки вычислить общее количество страниц всех
# книг и среднюю цену













