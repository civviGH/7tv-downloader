from selenium import webdriver
from selenium.webdriver.common.by import By

import requests

driver = webdriver.Chrome()

for i in range(1,10):
    driver.get(f"https://7tv.app/emotes?page={i}")
    driver.implicitly_wait(50)
    element = driver.find_element(By.CLASS_NAME, "cards-list-wrapper")
    print(element.text)
    emotes = element.find_elements(By.CSS_SELECTOR, 'div.emote-card > a.unstyled-link')
    for e in emotes:
        emote_link = e.find_element(By.CSS_SELECTOR, 'div.img-wrapper > img').get_attribute('src')
        name = e.find_element(By.CSS_SELECTOR, 'div.title-banner > span').text
        print(f"{name} | {emote_link}")
        response = requests.get(emote_link)
        with open(f"emotes/{name.lower()}.webp", 'wb') as f:
            f.write(response.content)
driver.quit()
