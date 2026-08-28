from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver(browser):

    if browser.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        return webdriver.Firefox(options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Edge(options=options)

    elif browser.lower() == "safari":
        return webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")