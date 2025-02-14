import os

class Constants:
    CHROME_PATH = os.getenv('CHROME_PATH', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH', 'C:\\WebDriver\\chromedriver.exe')
