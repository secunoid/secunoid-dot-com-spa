from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time

# Path to your local HTML file
HTML_FILE = 'file:///d:/Users/smsha/Github/secunoid-dot-com-spa/index.html'

# Set up Chrome WebDriver (make sure chromedriver is installed and in PATH)
service = Service()
driver = webdriver.Chrome(service=service)
driver.get(HTML_FILE)
time.sleep(2)  # Wait for page to load

# Find all anchor tags
links = driver.find_elements(By.TAG_NAME, 'a')

results = []
for link in links:
    href = link.get_attribute('href')
    text = link.text.strip()
    if not href:
        results.append((text, 'No href'))
        continue
    try:
        driver.execute_script(f"window.open('{href}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        # Check if page loaded
        if driver.current_url == href or href.startswith('mailto:') or href.startswith('tel:'):
            results.append((text, 'OK'))
        else:
            results.append((text, f'Unexpected URL: {driver.current_url}'))
    except WebDriverException as e:
        results.append((text, f'Error: {str(e)}'))
    finally:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

# Print results
for text, status in results:
    print(f'Link text: "{text}" - Status: {status}')

driver.quit()
