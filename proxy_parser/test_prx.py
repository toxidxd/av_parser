import requests, time, bs4, re
from fake_useragent import UserAgent

link = "https://yandex.ru/internet"

print("Подключение без прокси")
time.sleep(0.5)
soup = requests.get(link, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
soup = bs4.BeautifulSoup(soup.text, "html.parser")
soup = str(soup)

ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", soup)
print("IP without proxy: ", ip[0])
time.sleep(0.5)

print("Пробуем авито без прокси")
time.sleep(0.5)
link = "https://www.avito.ru/zernograd/tovary_dlya_kompyutera/protsessor_amd_athlon_ii_x3_450_1658209131"
soup = requests.get(link, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
soup = bs4.BeautifulSoup(soup.text, "html.parser")
title = soup.select('.title-info-title-text')
print(title[0].getText())
time.sleep(0.5)

print("Подключение с прокси")
time.sleep(0.5)
proxies = {"https": "194.186.135.74:3130"}
soup = requests.get(link, proxies=proxies, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
soup = bs4.BeautifulSoup(soup.text, "html.parser")
soup = str(soup)

ipwp = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", soup)
print("IP with proxy: ", ipwp[0])
time.sleep(0.5)

print("Пробуем авито с прокси")
time.sleep(0.5)
link = "https://www.avito.ru/zernograd/tovary_dlya_kompyutera/protsessor_amd_athlon_ii_x3_450_1658209131"
soup = requests.get(link, proxies=proxies, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
soup = bs4.BeautifulSoup(soup.text, "html.parser")
title = soup.select('.title-info-title-text')
print(title[0].getText())
time.sleep(0.5)
