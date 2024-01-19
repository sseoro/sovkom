from selenium.webdriver.common.by import By
from base.base_class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleTableResult(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    table_result = '//div[@id="center_col"]'    # локатор таблицы результатов
    button_pictures = ".LatpMc:nth-child(1) .FMKtTb"    # локатор кнопки "Картинки"

    url_first_result = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'    # локатор ссылки первого результата поиска
    url_second_result = '//*[@id="rso"]/div[2]/div[1]/div/div/div/div[1]/div/div/span/a'    # локатор ссылки второго результата поиска
    url_third_result = '//*[@id="rso"]/div[2]/div[4]/div/div/div/div[1]/div/div/span/a' # локатор ссылки третьего результата поиска
    url_fourth_result = '//*[@id="rso"]/div[2]/div[5]/div/div/div/div[1]/div/div/span/a'    # локатор ссылки четвертого результата поиска
    url_fifth_result = '//*[@id="rso"]/div[2]/div[6]/div/div/div/div[1]/div/div/span/a' # локатор ссылки пятого результата поиска

    """Getters"""

    def get_table_result(self):     # Получение локатора таблицы результатов
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.table_result)))

    def get_button_pictures(self):     # Получение локатора кнопки "Картинки"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_pictures)))

    def get_url_first_result(self):    # Получение локатор ссылки первого результата поиска
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.url_first_result)))

    def get_url_second_result(self):    # Получение локатор ссылки второго результата поиска
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.url_second_result)))

    def get_url_third_result(self):     # Получение локатор ссылки третьего результата поиска

        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.url_third_result)))

    def get_url_fourth_result(self):        # Получение локатор ссылки четвертого результата поиска
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.url_fourth_result)))

    def get_url_fifth_result(self):        # Получение локатор ссылки пятого результата поиска
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.url_fifth_result)))

    """Actions"""

    def click_button_pictures(self):    # Клик на кнопку "Картинки"
        return self.get_button_pictures().click()

    """Methods"""

    def comparison_first_five_have_links(self, need_url):  # Метод, который сравнивает первые пять ссылок с необходимой ссылкой

        # need_url - ссылка, с которой необходимо сравнивать

        self.get_table_result()

        first_result = self.get_url_first_result().get_attribute("href")    # Получаем ссылку из атрибута
        second_result = self.get_url_second_result().get_attribute("href")
        third_result = self.get_url_third_result().get_attribute("href")
        fourth_result = self.get_url_fourth_result().get_attribute("href")
        fifth_result = self.get_url_fifth_result().get_attribute("href")

        comparison_result = bool

        if (first_result == need_url        # Сравниваем полученные ссылки в результатах с необходимой
                or second_result == need_url
                or third_result == need_url
                or fourth_result == need_url
                or fifth_result == need_url
                ):
                    print(f"В первых пяти результатах поиска есть ссылка на {need_url}")
                    comparison_result = True
        else:
            assert comparison_result == True, 'Нет ссылки в первых пяти результатах'