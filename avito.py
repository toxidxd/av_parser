import requests, bs4

#get page
soup = requests.get('https://www.avito.ru/rostov-na-donu/tovary_dlya_kompyutera/komplektuyuschie/videokarty')

#write page to vairiable
soup = bs4.BeautifulSoup(soup.text, "html.parser")

#movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')

#item_links = soup.find('div', {'class': 'item_table-header'}).find('a').get('href')

item_links = soup.select('.item-description-title-link')

i = 0
flinks = open("links.txt", "a")
for itm in item_links:
    #print(item_links[i].get('href'))
    flinks.write("https://www.avito.ru"+item_links[i].get('href')+"\n")
    i+=1

flinks.close

pages_links = soup.select('.pagination-page')

print(pages_links[len(pages_links)-1].get('href'))

pages_last = pages_links[len(pages_links)-1].get('href').split('?p=')
pages_last = int(pages_last[1])
print(pages_last)
print(type(pages_last))
#print(len(item_links))
#print("https://www.avito.ru"+item_links)


#end of script
