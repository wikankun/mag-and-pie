import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TokopediaScraper:

    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

        # self.service = Service(executable_path='/opt/homebrew/bin/geckodriver')
        self.driver = webdriver.Firefox(
            options=self.options,
            # service=self.service
        )
        self.driver.get("https://www.tokopedia.com/")

    def search_product(self, keyword):
        wait = WebDriverWait(self.driver, 10)
        search_bar = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/input"
                )
            )
        )
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.RETURN)
    
    def scroll_down(self):
        i = 1
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom smoothly
            # Scroll step is set to 100 pixels
            for i in range(0, last_height, 100):
                self.driver.execute_script(f"window.scrollTo(0, {i});")
                # Small delay to mimic smooth scrolling
                time.sleep(0.05)
                # Check next page button exist or not, if exist it will stop scrolling
                try:
                    next_btn = self.driver.find_element(
                        By.XPATH,
                        f'/html/body/div[1]/div/div[2]/div/div[2]/div[5]/nav/ul/li[11]/button'
                    )
                    if next_btn:
                        break
                except:
                    next_btn = None
                    pass

            # Wait to load page
            wait = WebDriverWait(self.driver, 2)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height or next_btn != None:
                break
            last_height = new_height

    def scrape_page(self,page):
        product_data = []
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f'/html/body/div[1]/div/div[2]/div/div[2]/div[4]'
                )
            )
        )
        
        all_batch_product_parent = self.driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div/div[2]/div/div[2]'
        )
        all_batch_product = all_batch_product_parent.find_elements(
            By.XPATH,
            f'./div[@data-ssr="contentProductsSRPSSR"]/div'
        )

        for batch_product in all_batch_product:
            products = batch_product.find_elements(
                By.XPATH,
                "./div"
            )

            for product in products:
                # Search product
                try:
                    parent_metadata = product.find_element(
                        By.XPATH,
                        "./div/div/div/div/div/div[2]/a"
                    )
                except:
                    # Shop nearby
                    parent_metadata = product.find_element(
                        By.XPATH,
                        "./div[2]/div[1]/div/div/div/div/div/div[2]/a"
                    )

                sku_name = parent_metadata.find_element(
                    By.XPATH,
                    "./div[contains(@class, 'prd_link-product-name')]"
                ).text

                price = parent_metadata.find_element(
                    By.XPATH,
                    "./div[@class='']/div[@class='']/div[contains(@class, 'prd_link-product-price')]"
                ).text

                # If element is empty, that means sold is 0
                try:
                    sold = parent_metadata.find_element(
                        By.XPATH,
                        "./div[@data-productinfo='true']/div[2]/span[3]"
                    ).text
                except:
                    sold = 0

                product_data.append(
                    {
                        "page": page, 
                        "sku_name": sku_name,
                        "price": price,
                        "sold": sold
                    }
                )

        return pd.DataFrame(product_data)
    
    def next_page(self):
        stop_flag = False
        wait = WebDriverWait(self.driver, 10)
        try:
            parent_next_btn = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f'/html/body/div[1]/div/div[2]/div/div[2]/div[5]'
                    )
                )
            ).find_element(
                By.XPATH,
                "./nav/ul"
            )
        except:
            parent_next_btn = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f'/html/body/div[1]/div/div[2]/div/div[2]/div[4]'
                    )
                )
            ).find_element(
                By.XPATH,
                "./nav/ul"
            )

        next_btn = parent_next_btn.find_elements(
            By.XPATH,
            "./li"
        )[-1].find_element(
            By.XPATH,
            "./button"
        )

        if next_btn.is_enabled():
            self.driver.execute_script("arguments[0].scrollIntoView();",next_btn)
            self.driver.execute_script("arguments[0].click();",next_btn)
        else:
            stop_flag = True
        return stop_flag

    def close_browser(self):
        self.driver.quit()