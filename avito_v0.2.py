import requests, bs4


def page_counter (link):
    soup = requests.get(link)
    soup = bs4.BeautifulSoup(soup.text, "html.parser")
    pages_links = soup.select('.pagination-page')
    pages_last = pages_links[len(pages_links)-1].get('href').split('?p=')
    pages_last = int(pages_last[1])
    return pages_last

def links_parser (link_p):
    soup = requests.get(link_p)
    soup = bs4.BeautifulSoup(soup.text, "html.parser")
    item_links_temp = soup.select('.item-description-title-link')
    item_links = []
    i = 0
    for itm in item_links_temp:
        item_links.append("https://www.avito.ru"+item_links_temp[i].get('href'))
        i += 1
    return item_links



print ("Hello, pel_MEN!\nThis is avito parser.\nLink example: https://www.avito.ru/zernograd/tovary_dlya_kompyutera")
#link = input("input_link: ")
link = "https://www.avito.ru/zernograd/tovary_dlya_kompyutera"
pcount = page_counter(link)
print ("Count pages: ", pcount)


all_links = []
page = 1
while page <= pcount:
    print("Parsing page ", page)
    cur_page = link+"?p="+str(page)
    #print(links_parser(cur_link))
    parsed_links = links_parser(cur_page)
    #print(parsed_links)
    x = 0
    for itm in parsed_links:
        all_links.append(parsed_links[x])
        x += 1
    print("links parsed ", len(links_parser(cur_page)))
    page += 1

#zz = 0
#print("==================================")
#for itm in all_links:
    #print(all_links[zz])
    #zz += 1
#print(all_links)
print("Overal links parsed: ", len(all_links))

#print(links_parser(link))
#print(len(links_parser(link)))


#write page to vairiable


#movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')

#item_links = soup.find('div', {'class': 'item_table-header'}).find('a').get('href')

#item_links = soup.select('.item-description-title-link')

#i = 0
#flinks = open("links.txt", "a")
#for itm in item_links:
    #print(item_links[i].get('href'))
    #flinks.write("https://www.avito.ru"+item_links[i].get('href')+"\n")
    #i+=1

#flinks.close


#print(len(item_links))
#print("https://www.avito.ru"+item_links)


#end of script
