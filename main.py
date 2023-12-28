from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="path/to/chromedriver")

driver.get("https://glitch.com/edit/#!/remix/glitch-blank-website")

search_bar = driver.find_element_by_id("search_bar_id")
search_bar.send_keys("Hello, World!")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "element_id")))

link = driver.find_element_by_link_text("index.html")
link.click()

driver.switch_to.window(driver.window_handles[1])

driver.quit()
