import os
import random

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


from util import Constants

constants = Constants()


class Configuration:
    def __init__(self):
        pass

    def configure_webdriver(self, url, open_pdf_externally=True, pasta_diaria=None, start_automatically=True, headless=True):

        if not pasta_diaria:
            user_dir = os.path.expanduser("~")
            pasta_diaria = os.path.join(user_dir, "OneDrive - Dadoteca",
                                        "Documentos Compartilhados - Hidrolicencas DOSP", "pdfs_doe")

        download_directory = pasta_diaria

        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:93.0) Gecko/20100101 Firefox/93.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        ]
        userAgent = random.choice(user_agent_list)

        chrome_options = Options()
        # chrome_options.binary_location = constants.CHROME_PATH
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920x1080")

        chrome_options.add_argument("--disable-features=InsecureDownloadWarning")
        chrome_options.add_argument(f"--unsafely-treat-insecure-origin-as-secure={url}")
        chrome_options.add_argument(f'--user-agent={userAgent}')

        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_directory,
            "savefile.default_directory": download_directory,
            "plugins.always_open_pdf_externally": open_pdf_externally,
            "safebrowsing.enabled": True,
            "profile.default_content_settings.popups": 0,
            "profile.content_settings.pattern_pairs.*.multiple-automatic-downloads": 1,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "excludeSwitches": ["enable-automation"],
        })
        service = Service(constants.CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        if start_automatically:
            driver.get(url)
        return driver
