from pages.google_search_page import GoogleSearch
from pages.google_table_result import GoogleTableResult
from pages.google_pictures import GooglePictures
from base.base_class import BaseClass


def test_case_1(call_driver):

    """Инициализация классов"""

    base = BaseClass(call_driver)
    search_page = GoogleSearch(call_driver)
    google_table = GoogleTableResult(call_driver)

    """Действия  теста"""

    base.go_to_page('https://www.google.ru/')   # Переход на страницу Google

    search_page.searchline_input_text('Совкомбанк')     # Ввод слова "Совкомбанк" в поисковой строке

    print(search_page.ad_text_search_tips_list())       # Выводим список подсказок. P.S по ТЗ непонятно какой результат после проверки ожидается

    search_page.find_word_in_tips('совкомбанк')     # Поиск слова "совкомбанк" в подсказках. Регистр не учитывал, т.е в тз задается с маленькой
    search_page.click_search_in_google()        # Клик "Поиск в Google"
    google_table.comparison_first_five_have_links('https://sovcombank.ru/')     # Сравнение первых пяти ссылок


def test_case_2(call_driver):

    """Инициализация классов"""

    base = BaseClass(call_driver)
    search_page = GoogleSearch(call_driver)
    google_pictures = GooglePictures(call_driver)
    google_table = GoogleTableResult(call_driver)

    """Действия  теста"""

    base.go_to_page('https://www.google.ru/')  # Переход на страницу Google

    search_page.searchline_input_text('Совкомбанк')  # Ввод слова "Совкомбанк" в поисковой строке

    print(search_page.ad_text_search_tips_list())  # Выводим список подсказок. P.S по ТЗ непонятно какой результат после проверки ожидается

    search_page.find_word_in_tips('совкомбанк')  # Поиск слова "совкомбанк" в подсказках. Регистр не учитывал, т.е в тз задается с маленькой
    search_page.click_search_in_google()  # Клик "Поиск в Google"

    google_table.click_button_pictures()    # Клик кнопки "Картинки"

    google_pictures.click_second_photo()    # Клик на вторую картинку

    text_second_photo = google_pictures.text_second_photo_()    # Сохраняется текст с превью, чтобы потом понять, что именно эта картинка

    google_pictures.click_right_arrow()     # Нажатие кнопки "Вперед"

    assert google_pictures.text_second_photo_() != text_second_photo, 'картинка не поменялась'   # Проверка, что картинка сменилась

    google_pictures.click_left_arrow()      # Нажатие кнопки "Назад"

    assert google_pictures.text_second_photo_() == text_second_photo, 'картинка не вернулась обратно на вторую' # Проверка, что произошел возврат к картинке