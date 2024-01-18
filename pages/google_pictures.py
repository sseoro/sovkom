from selenium.webdriver.common.by import By
from base.base_class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePictures(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    second_photo = '//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img'     # Локатор второй фотографии
    text_second_photo = '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[5]/div[1]/a[1]/h1' # Локатор текста, который появляется в превью
    left_arrow = '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[1]/div/div[2]/button[1]'  # Локатор стрелочки влево
    right_arrow = '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[1]/div/div[2]/button[2]' # Локатор стрелочки вправо


    """Getters"""

    def get_second_photo(self):     # Получение локатор второй фотографии
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_photo)))

    def get_text_second_photo(self):    # Получение локатора текста, который появляется в превью
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_second_photo)))

    def get_left_arrow(self):   # Получение локатора стрелочки влево
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.left_arrow)))

    def get_right_arrow(self):    # Получение локатора стрелочки вправо
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.right_arrow)))




    """Actions"""

    def click_second_photo(self):   # Клик по второй фотографии
        return self.get_second_photo().click()

    def text_second_photo_(self):   # Получение текста в преью
        return self.get_text_second_photo().text

    def click_left_arrow(self):     # Клик стрелочки влево
        return self.get_left_arrow().click()

    def click_right_arrow(self):    # Клик стрелочки вправо
        return self.get_right_arrow().click()

    """Methods"""



