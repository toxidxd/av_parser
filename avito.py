

import requests, bs4, random, time, csv

def page_counter (link):
    soup = requests.get(link)
    soup = bs4.BeautifulSoup(soup.text, "html.parser")
    print(soup)
    pages_links = soup.select('.pagination-page')
    try:
        pages_last = pages_links[len(pages_links)-1].get('href').split('?p=')
    except Exception:
        print("Page not found!")
        quit()
    pages_last = int(pages_last[1])
    return pages_last

def links_parser (link, pcount):
    all_links = []
    page = 1
    while page <= pcount:
        print ("Current page: ", page)
        soup = requests.get(link+"?p="+str(page))
        soup = bs4.BeautifulSoup(soup.text, "html.parser")
        item_links_temp = soup.select('.item-description-title-link')

        for itm in item_links_temp:
            all_links.append("https://www.avito.ru"+itm.get('href'))

        print ("Links parsed", len(all_links))
        page += 1
    return all_links

def items_parser (all_links):
    all_items = []

    c_lnk = 0
    for lnk in all_links:
        #cur_item = []
        print("\nCur link:", c_lnk, "\n", lnk)

        try:
            soup = requests.get(lnk)
            soup = bs4.BeautifulSoup(soup.text, "html.parser")
            item = soup.select('.title-info-title-text')
            try:
                item_name = item[0].getText()
            except Exception:
                print("No title!")
                item_price = "No title!"

            price = soup.select('.price-value-string .js-item-price')
            try:
                item_price = price[0].get('content')
            except Exception:
                print("No price!")
                item_price = "No price!"

            descript = soup.select('.item-description-text')
            try:
                item_descript= descript[0].getText()
            except Exception:
                print("No description")
                item_descript = ("No description")
            cur_item = [lnk, item_name, item_price, item_descript]
        except Exception:
            lnk = "Error! Link not downloaded!!"
            print(lnk)
            cur_item = [lnk]


        #print(item_name)
        #print(item_price)
        #print(item_descript)



        #print (item_name)
        #print("\n\n\ncur!!!!!!!!!", cur_item)
        all_items.append(cur_item)
        #print("\n\n\nall!!!!!!!!", all_items)
        c_lnk += 1

        sl = random.randint(3,6)
        print("Sleep ", sl, " sec")
        time.sleep(sl)


    return all_items


print ("Hello, Johny!\nThis is avito parser.\nLink example: https://www.avito.ru/zernograd/tovary_dlya_kompyutera")

#link = input("input_link: ")
link = "https://www.avito.ru/zernograd/bytovaya_elektronika"
print ("\nCounting pages")
pcount = page_counter(link)
print ("Count pages: ", pcount)

print ("\nParsing links")
all_links = links_parser(link, pcount)
print("Overal links parsed: ", len(all_links))

print("\nParsing items\n")
all_items = items_parser(all_links)
print("Overal items parser: ", len(all_items))


with open("zalupa_test.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in all_items:
        writer.writerow(line)
print("File writed!")

#f = open("parsed.csv", "a")
#for itm in all_items:
    #f.write(itm+"\n")
#print("file parsed.csv wtited (_Y_)")
#f.close()



#i = 0
#flinks = open("links.txt", "a")
#for itm in item_links:
    #print(item_links[i].get('href'))
    #flinks.write("https://www.avito.ru"+item_links[i].get('href')+"\n")
    #i+=1


#zz = 0
#for itm in all_links:
#    print(all_links[zz])
#    zz += 1
#print(all_links)


#zz = 0
#print("==================================")
#for itm in all_links:
    #print(all_links[zz])
    #zz += 1
#print(all_links)
#print("Overal links parsed: ", len(all_links))

#print(links_parser(link))
#print(len(links_parser(link)))


#write page to vairiable


#movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')

#item_links = soup.find('div', {'class': 'item_table-header'}).find('a').get('href')

#item_links = soup.select('.item-description-title-link')



#flinks.close


#print(len(item_links))
#print("https://www.avito.ru"+item_links)


#end of script
