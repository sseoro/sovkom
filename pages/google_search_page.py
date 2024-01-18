import time
from selenium.webdriver.common.by import By
from base.base_class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleSearch(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    search_line = '//textarea[@id="APjFqb"]'    # Локатор поисковой строки
    search_tips_list = '//div[@class="erkvQe"]'     # Локатор подсказок по поиску
    search_in_google = '//input[@class="gNO89b"]'   # Локатор кнопки "Найти в Google"

    """Getters"""

    def get_search_line(self):      # Получение локатора поисковой строки
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_line)))

    def get_search_tips_list(self):      # Получение локатора подсказок по поиску
        locator_dom = (WebDriverWait(self.driver, 30).
                       until(EC.element_to_be_clickable((By.XPATH, self.search_tips_list))))
        locator_list = locator_dom.find_elements(By.TAG_NAME, 'li')
        return locator_list     # Возвращается список всех подсказок

    def get_search_in_google(self):     # Получение локатора кнопки "Найти в Google"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_in_google)))


    """Actions"""

    def send_search_line(self, text):       # Вставляется текст в поисковую строку
        return self.get_search_line().send_keys(text)

    def click_search_in_google(self):       # Клик кнопки "Найти в Google"
        return self.get_search_in_google().click()

    """Methods"""

    def searchline_input_text(self, text):  # Метод по вводу текста
        self.get_search_line().click()
        self.send_search_line(text)
        time.sleep(0.5)     # Тайм  слип нужен, чтобы дождаться загрузки всех подсказок

    def ad_text_search_tips_list(self):     # Идет поиск рекламных блоков
        __list = []
        num = 0

        for i in self.get_search_tips_list():
            num += 1
            text = i.get_attribute("data-entityname")
            class_name = i.get_attribute("class")
            if "sbre" in class_name:       # По наблюдениям если classname имеет sbre - то это рекламный/инф. блок
                text = f'Рекламная строка - {text}'
            __list.append(f"{num} подсказка - {text}")

        print(type(__list))
        return __list

    def find_word_in_tips(self, word):      # Поиск слова в подсказке. Учитывается регистр или нет - непонятно. В тз именно это задание с маленькой
        num = 0
        __list = self.ad_text_search_tips_list()
        for i in range(len(__list)):
            if word in __list[i]:
                print(f'{i} подсказка - есть слово {word}')
            else:
                print(f'{i} подсказка - нет слова {word}')