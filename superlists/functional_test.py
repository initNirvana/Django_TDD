from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """설치되어 있는 크롬으로 설정"""
        chrome_options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")


        # 타이틀 확인
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 작업 추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        inputbox.send_keys('공작깃털 사기')

        # 공작 깃털 사기 추가
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
        )


        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')