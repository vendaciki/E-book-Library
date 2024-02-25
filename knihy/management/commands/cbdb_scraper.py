from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CBDBReviewScraper:
    def __init__(self, isbn):
        webpage_url = "https://www.cbdb.cz/muj-prehled"
        self.isbn = isbn

        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(webpage_url)
        time.sleep(2)

    def get_review(self):
        searchbar = self.driver.find_element(
            By.XPATH,
            value='/html/body/header/div/div[4]/div/form/input[1]'
        )
        searchbar.send_keys(self.isbn)
        self.driver.implicitly_wait(5)
        searchbar.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(5)

        try: 
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="item_rating"]'))
)
            # review = self.driver.find_element(
            #     By.XPATH,
            #     value='/html/body/div[3]/div/div[5]/div[2]/a'
            # )
            print(element.text)
        except Exception as e:
            print(e)
        else:
            return int(element.text.replace("%", ""))
        finally:
            self.driver.quit()
        return 0

        

    


