from selenium import webdriver

browser = webdriver.Chrome()

# Check home page availability
browser.get('http://localhost:8000')

# Notice the title and header
assert 'To-Do' in browser.title

browser.quit()
