import sqlite3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

website = 'https://books.toscrape.com/'

conn = sqlite3.connect('books.db')  # Create or connect to a database file
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT
    )
''')
conn.commit()

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get(website)

time.sleep(3)

producten = driver.find_elements(By.CLASS_NAME, 'product_pod')

for product in producten:
    # Zoek de titel van het product
    titel = product.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('title')

    # Zoek de prijs van het product
    prijs = product.find_element(By.CLASS_NAME, 'price_color').text

    # Print de gegevens
    print(f"Product: {titel} - Prijs: {prijs}")

    cursor.execute('INSERT INTO books (title, price) VALUES (?, ?)', (titel, prijs))

conn.commit()
conn.close()

driver.quit()

print("Data successfully scraped and stored in 'books.db'")
