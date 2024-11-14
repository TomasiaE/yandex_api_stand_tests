# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body

# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов

def test_create_user_2_letter_in_first_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса с именем "Аа"
    user_body = get_user_body("Аа")
    # В переменную user_response сохраняется результат запроса на создание пользователя
    user_response = sender_stand_request.post_new_user(user_body)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert user_response.json()["authToken"] != ""

    # Конструирование строки str_user с данными пользователя и токеном авторизации.
    # Сначала добавляется имя пользователя из словаря user_body.
    # Затем через запятую добавляется номер телефона пользователя из того же словаря.
    # После этого добавляется адрес пользователя, также из словаря user_body.
    # Далее следуют три запятые, разделяющие данные пользователя от токена авторизации.
    # В конце добавляется токен авторизации, извлеченный из JSON-ответа сервера после выполнения запроса к API.
    # Использование обратной косой черты (\) в конце первой строки позволяет перенести часть кода на новую строку для лучшей читаемости.
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

    # Функция для позитивной проверки
def positive_assert(first_name):
        # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(first_name)
        # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response = sender_stand_request.post_new_user(user_body)

        # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
        # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert user_response.json()["authToken"] != ""

        # В переменную users_table_response сохраняется результат запроса на получение данных из таблицы user_model
    users_table_response = sender_stand_request.get_users_table()

        # Строка, которая должна быть в ответе
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
                + user_body["address"] + ",,," + user_response.json()["authToken"]

        # Проверка, что такой пользователь есть и он единственный
    assert users_table_response.text.count(str_user) == 1

    # Тест 1. Успешное создание пользователя
    # Параметр fisrtName состоит из 2 символов
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")


def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Ааааааааааааааа")

def negative_assert_symbol(first_name):

    user_body = get_user_body(first_name)

    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_user(user_body)

    # Проверка, что код ответа равен 400
    assert response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 2 и не более 15 символов"

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("А")

 # Тест 4. Ошибка
    # Параметр fisrtName состоит из 16 символов
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")

def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")

def test_create_user_russian_letter_in_first_name_get_success_response():
    positive_assert("Мария")

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("Человек и Ко")

    # Параметр fisrtName состоит из строки спецсимволов
def test_create_user_has_special_symbol_in_first_name_get_error_response():
        negative_assert_symbol("№%@")

    # Параметр fisrtName состоит из строки с цифрами
def test_create_user_has_number_in_first_name_get_error_response():
        negative_assert_symbol("123")

    # Функция для негативной проверки
    # В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_first_name(user_body):
        # В переменную response сохрани результат вызова функции
    response = sender_stand_request.post_new_user(user_body)

        # Проверь, что код ответа — 400
    assert response.status_code == 400

        # Проверь, что в теле ответа атрибут "code" — 400
    assert response.json()["code"] == 400

        # Проверь текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 10. Ошибка
# В запросе нет параметра firstName
def test_create_user_no_first_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    # Иначе можно потерять данные из исходного словаря
    user_body = data.user_body.copy()
    # Удаление параметра firstName из запроса
    user_body.pop("firstName")
    # Проверка полученного ответа
    negative_assert_no_first_name(user_body)

    # Тест 11. Ошибка
    # Параметр fisrtName состоит из пустой строки
def test_create_user_empty_first_name_get_error_response():
        # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body("")
        # Проверка полученного ответа
    negative_assert_no_first_name(user_body)

    # Тест 12. Ошибка
    # Тип параметра firstName: число
def test_create_user_number_type_first_name_get_error_response():
        # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(12)
        # В переменную user_response сохраняется результат запроса на создание пользователя:
    response = sender_stand_request.post_new_user(user_body)

        # Проверка кода ответа
    assert response.status_code == 400