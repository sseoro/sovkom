import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def call_driver():
    from sys import platform
    print(platform)
    driver = None
    if platform == "linux" or platform == "linux2":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-breakpad")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-default-apps")
        options.add_argument("--window-size=1920,1080")
        driver_path = "//usr//bin//chromedriver"
        service = Service(driver_path)
        driver = webdriver.Chrome(options=options, service=service)

    elif platform == "win32" or platform == "windows" or platform == "win64":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--allow-running-insecure-conten")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-breakpad")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-default-apps")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.close()
