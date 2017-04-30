from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# check home page
		self.browser.get('http://localhost:8000')

		# Check page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

"""# Invited to enter a to-do item straight away
		[...rest of comments as before]
"""

if __name__ == '__main__':
	unittest.main(warnings='ignore')

"""browser = webdriver.Chrome()

# Check home page availability
browser.get('http://localhost:8000')

# Notice the title and header
assert 'To-Do' in browser.title, "Browser title was " + browser.titlee

browser.quit()
"""
