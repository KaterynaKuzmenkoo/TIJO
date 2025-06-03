import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestWebPage(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Chrome
        """
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_page_heading(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i zawartość (assertEqual) nagłówka na stronie
        """
        # Given
        self.driver.get('https://example.com')

        # When
        heading = self.driver.find_element(By.TAG_NAME, 'h1')

        # Then
        self.assertIsNotNone(heading)
        self.assertEqual(heading.text, "Example Domain")

    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
