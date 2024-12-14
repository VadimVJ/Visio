import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL сайта для парсинга
url = 'https://www.divan.ru/category/divany'

# Получение страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Парсинг данных о ценах (обратите внимание, что структура сайта может изменяться)
prices = []
for price_tag in soup.find_all('div', class_='product-price'):  # Проверьте правильность класса
    price_text = price_tag.get_text(strip=True).replace(' ', '').replace('₽', '')
    try:
        price = int(price_text)  # Преобразование текста в целое число
        prices.append(price)
    except ValueError:
        continue

# Сохранение данных в CSV
df = pd.DataFrame(prices, columns=['Цена'])
df.to_csv('divan_prices.csv', index=False)

# Вычисление средней цены
average_price = df['Цена'].mean()
print(f'Средняя цена: {average_price:.2f} ₽')  # Форматируем вывод средней цены

# Построение гистограммы цен
plt.hist(prices, bins=30, alpha=0.7, color='red', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')
