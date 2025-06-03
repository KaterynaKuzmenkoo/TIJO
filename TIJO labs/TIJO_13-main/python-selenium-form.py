import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')

    def test_TC01_add_single_digits(self):
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("2")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        print(f"RESULT: {result}")  # 👈 dodaj to
        self.assertEqual(result, "2 + 3 = 5")

    def test_TC02_add_single_and_double_digit(self):
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("7")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("12")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "7 + 12 = 19")

    def test_BUG01_add_negative_number(self):
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("1")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("-2")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "1 + -2 = -1")

    def test_BUG02_decimal_with_comma(self):
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("1.3")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("2")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "1.3 + 2 = 3.3")

    def tearDown(self):
        self.driver.quit()


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_TC02_invalid_email(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')
        self.driver.find_element(By.ID, "email").send_keys("testexample.com")
        self.driver.find_element(By.ID, "message").send_keys("Niepoprawny e-mail")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        email = self.driver.find_element(By.ID, "email")
        self.assertIn("@", email.get_attribute("validationMessage"))

    def test_BR01_message_length_limit(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')
        self.driver.find_element(By.ID, "email").send_keys("test@example.com")
        self.driver.find_element(By.ID, "message").send_keys("a" * 20)
        value = self.driver.find_element(By.ID, "message").get_attribute("value")
        self.assertGreaterEqual(len(value), 20)

    def test_BR02_missing_team_photo(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/team.html')
        time.sleep(1)  # ⏳ Opcjonalnie: dodaj, jeśli strona ładuje się dynamicznie
        imgs = self.driver.find_elements(By.TAG_NAME, "img")
        found = any("graphic-designer" in img.get_attribute("alt").lower() or
                    "graphic-designer" in img.get_attribute("src").lower()
                    for img in imgs)
        self.assertTrue(found, "Nie znaleziono zdjęcia Piotra Wiśniewskiego.")

    def test_BR04_font_size_experience(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')
        p = self.driver.find_element(By.TAG_NAME, 'p')

        self.assertEqual(p.value_of_css_property('font-size'), "18px")

    def test_BR05_missing_company_name(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')
        header = self.driver.find_element(By.TAG_NAME, 'header')
        a = header.find_element(By.TAG_NAME, 'a')
        img = a.find_element(By.TAG_NAME, 'img')

        self.assertEqual(img.get_property('src'),
                         "https://tgadek.bitbucket.io/app/portfolio/prod/img/it-design-logo.png")
        self.assertEqual(header.find_element(By.TAG_NAME, 'h1').text, "IT Design")


    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
