import requests
import bs4
import random
import time
import csv
from fake_useragent import UserAgent


def page_counter(link):
	soup = requests.get(link, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
	soup = bs4.BeautifulSoup(soup.text, "html.parser")
	print(soup)
	pages_links = soup.select('.pagination-page')
	try:
		pages_last = pages_links[len(pages_links) - 1].get('href').split('?p=')
		pages_last = int(pages_last[1])
	except Exception:
		print("its 1 page?")
		pages_last = 1

	return pages_last


def links_parser(link, pcount):
	all_links = []
	page = 1
	while page <= pcount:
		print("Current page: ", page)
		soup = requests.get(link + "?p=" + str(page), headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
		soup = bs4.BeautifulSoup(soup.text, "html.parser")
		item_links_temp = soup.select('.snippet-link')

		for itm in item_links_temp:
			all_links.append("https://www.avito.ru" + itm.get('href'))

		print("Links parsed", len(all_links))
		sl = random.randint(1, 2)
		print("Sleep ", sl, " sec")
		time.sleep(sl)
		page += 1
	return all_links


def title_parser(soup):
	item = soup.select('.title-info-title-text')
	try:
		item_name = item[0].getText()
	except Exception:
		print("No title!")
		item_name = "No title!"
	return item_name


def price_parser(soup):
	price = soup.select('.price-value-string .js-item-price')
	try:
		item_price = price[0].get('content')
	except Exception:
		print("No price!")
		item_price = "No price!"
	return item_price


def descript_parser(soup):
	descript = soup.select('.item-description-text')
	try:
		item_descript = descript[0].getText()
		des_temp = item_descript.split('\n')
		item_descript = des_temp[1]
	except Exception:
		print("No description!")
		item_descript = "No description!"
	return item_descript


def items_parser(all_links):
	all_items = []

	c_lnk = 1
	for lnk in all_links:
		# cur_item = []
		print("\nCur link:", c_lnk, "\n", lnk)

		try:
			soup = requests.get(lnk, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
			soup = bs4.BeautifulSoup(soup.text, "html.parser")

			item_name = title_parser(soup)
			item_price = price_parser(soup)
			item_descript = descript_parser(soup)

			cur_item = [lnk, item_name, item_price, item_descript]

		except Exception:
			page_error = "Error! Link not downloaded!!"
			print(page_error)
			cur_item = [page_error]

		all_items.append(cur_item)

		c_lnk += 1

		sl = random.randint(2, 10)
		print("Sleep ", sl, " sec")
		time.sleep(sl)

	return all_items


print("Hello, Johny!\nThis is avito parser.\nLink example: https://www.avito.ru/zernograd/tovary_dlya_kompyutera")

# link = input("input_link: ")

# link = "https://www.avito.ru/zernograd/tovary_dlya_kompyutera"
link = "https://www.avito.ru/zernograd/tovary_dlya_kompyutera"
print("\nCounting pages")
pcount = page_counter(link)
print("Count pages: ", pcount)

print("\nParsing links")
all_links = links_parser(link, pcount)
print("Overal links parsed: ", len(all_links))

print("\nParsing items\n")
all_items = items_parser(all_links)
print("Overal items parser: ", len(all_items))

print(all_items)
print(type(all_items))
with open("zalupa_test.csv", "w", newline='') as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	writer.writerow(["link", "title", "price", "description"])
	for line in all_items:
		writer.writerow(line)
print("File writed!")

# end of script
