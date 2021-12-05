import requests, bs4, random, time, csv, re
import cfscrape
import subprocess
from fake_useragent import UserAgent
########

def page_counter (link):
    i = 1
    for nxt_prx in s_all_prx:
        print("\nproxie", nxt_prx, " ", i, "of", len(s_all_prx))
        time.sleep(0.1)
        proxies = {"https": nxt_prx}
        i+=1
        try:
            
            soup = requests.get(link, proxies=proxies, timeout=3, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
            soup = bs4.BeautifulSoup(soup.text, "html.parser")
            #print(soup)
            strsoup = str(soup)
            ban_ip = re.findall(r"Доступ с вашего IP-адреса временно ограничен", strsoup)
            try:
                if ban_ip[0] == "Доступ с вашего IP-адреса временно ограничен":
                    print(ban_ip)
                    continue
            except Exception:
                print("No IP block")
                time.sleep(0.1)

            ban_ip = re.findall(r"Доступ временно заблокирован", strsoup)
            try:
                if ban_ip[0] == "Доступ временно заблокирован":
                    print(ban_ip)
                    time.sleep(0.1)
                    continue
            except Exception:
                print("No access block")
                time.sleep(0.1)

            pages_links = soup.select('.pagination-page')
            try:
                pages_last = pages_links[len(pages_links)-1].get('href').split('?p=')
                pages_last = int(pages_last[1])

            except Exception:
                print("its 1 page?")
                time.sleep(0.1)
                #print(soup)
                pages_last = 1
                #quit()
            break

        except requests.exceptions.ProxyError:
            print("ProxyError")
            time.sleep(0.1)
        except requests.exceptions.SSLError:
            print("SSLError")
            time.sleep(0.1)
        except requests.exceptions.ConnectTimeout:
            print("ConnectTimeout")
            time.sleep(0.1)
        except requests.exceptions.ReadTimeout:
            print("ReadTimeout")
            time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print("ConnetionError")
            time.sleep(0.1)

    return pages_last








def links_parser (link, pcount):
    all_links = []
    page = 1
    i = 1

    for nxt_prx in s_all_prx:
        print("\nproxie", nxt_prx, " ", i, "of", len(s_all_prx))
        time.sleep(0.1)
        proxies = {"https": nxt_prx}
        i+=1

        try:
            while page <= pcount:
                print ("\nCurrent page: ", page)
                time.sleep(0.1)
                soup = requests.get(link+"?p="+str(page), proxies=proxies, timeout=3, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
                soup = bs4.BeautifulSoup(soup.text, "html.parser")
                #print(soup)
                strsoup = str(soup)
                ban_ip = re.findall(r"Доступ с вашего IP-адреса временно ограничен", strsoup)
                try:
                    if ban_ip[0] == "Доступ с вашего IP-адреса временно ограничен":
                        print(ban_ip)
                        time.sleep(0.1)
                        break
                except Exception:
                    print("No IP block")
                    time.sleep(0.1)
                    #time.sleep(0.1)
                ban_ip = re.findall(r"Доступ временно заблокирован", strsoup)
                try:
                    if ban_ip[0] == "Доступ временно заблокирован":
                        print(ban_ip)
                        time.sleep(0.1)
                        break
                except Exception:
                    print("No access block")
                    time.sleep(0.1)
                    #time.sleep(0.1)

                item_links_temp = soup.select('.item-description-title-link')
                for itm in item_links_temp:
                    all_links.append("https://www.avito.ru"+itm.get('href'))

                print ("Links parsed", len(all_links))
                time.sleep(0.1)
                #sl = random.randint(1,2)
                #print("Sleep ", sl, " sec")
                #time.sleep(sl)
                page += 1

            if page > pcount:
                print("\nAll pages done\n")
                time.sleep(0.1)
                break

        except requests.exceptions.ProxyError:
            print("ProxyError")
            time.sleep(0.1)
        except requests.exceptions.SSLError:
            print("SSLError")
            time.sleep(0.1)
        except requests.exceptions.ConnectTimeout:
            print("ConnectTimeout")
            time.sleep(0.1)
        except requests.exceptions.ReadTimeout:
            print("ReadTimeout")
            time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print("ConnetionError")
            time.sleep(0.1)

    return all_links






def title_parser (soup):
    item = soup.select('.title-info-title-text')
    try:
        item_name = item[0].getText()
    except Exception:
        print("No title!")
        time.sleep(0.1)
        item_name = "No title!"
    return item_name

def price_parser (soup):
    price = soup.select('.price-value-string .js-item-price')
    try:
        item_price = price[0].get('content')
    except Exception:
        print("No price!")
        time.sleep(0.1)
        item_price = "No price!"
    return item_price

def descript_parser (soup):
    descript = soup.select('.item-description-text')
    try:
        item_descript = descript[0].getText()
        des_temp = item_descript.split('\n')
        item_descript = des_temp[1]
    except Exception:
        print("No description!")
        time.sleep(0.1)
        item_descript = ("No description!")
    return item_descript



def items_parser (all_links):
    all_items = []
    c_lnk = 1
    i = 1

    for nxt_prx in s_all_prx:
        print("\nproxie", nxt_prx, " ", i, "of", len(s_all_prx))
        time.sleep(0.1)
        proxies = {"https": nxt_prx}
        i+=1

        try:

            for lnk in all_links:
                print("\nCur link:", c_lnk, "\nProxie:", i, "\n", lnk)
                time.sleep(0.1)

                try:
                    soup = requests.get(lnk, proxies=proxies, timeout=3, headers={'User-Agent': UserAgent(verify_ssl=False).chrome})
                    soup = bs4.BeautifulSoup(soup.text, "html.parser")

                    strsoup = str(soup)
                    ban_ip = re.findall(r"Доступ с вашего IP-адреса временно ограничен", strsoup)

                    try:
                        if ban_ip[0] == "Доступ с вашего IP-адреса временно ограничен":
                            print(ban_ip)
                            time.sleep(0.1)
                            break
                    except Exception:
                        #print("No IP block")
                        #time.sleep(0.1)
                        pass
                    ban_ip = re.findall(r"Доступ временно заблокирован", strsoup)
                    try:
                        if ban_ip[0] == "Доступ временно заблокирован":
                            print(ban_ip)
                            time.sleep(0.1)
                            break
                    except Exception:
                        #print("No access block")
                        #time.sleep(0.1)
                        pass
                    item_name = title_parser(soup)
                    item_price = price_parser(soup)
                    item_descript = descript_parser(soup)

                    cur_item = [lnk, item_name, item_price, item_descript]
                    print(item_name)
                    time.sleep(0.1)

                except Exception:
                    page_error = "Error! Link not downloaded!!"
                    print(page_error)
                    time.sleep(0.1)
                    #print(soup)
                    break
                    cur_item = [page_error]

                all_items.append(cur_item)



                c_lnk += 1

            if c_lnk > len(all_links):
                print("\nAll links parsed\n")
                time.sleep(0.1)
                break

        except requests.exceptions.ProxyError:
            print("ProxyError")
            time.sleep(0.1)
        except requests.exceptions.SSLError:
            print("SSLError")
            time.sleep(0.1)
        except requests.exceptions.ConnectTimeout:
            print("ConnectTimeout")
            time.sleep(0.1)
        except requests.exceptions.ReadTimeout:
            print("ReadTimeout")
            time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print("ConnetionError")
            time.sleep(0.1)

    return all_items

################################################################
print ("Hello, Johny!\nThis is avito parser.\nLink example: https://www.avito.ru/zernograd/tovary_dlya_kompyutera")
time.sleep(0.1)
#link = input("input_link: ")

link = "https://www.avito.ru/zernograd/bytovaya_elektronika"
ya_link = "https://yandex.ru/internet"
prx_link = "https://hidemyna.me/ru/proxy-list/?country=BYITKZPLRUCHUA&maxtime=500&type=s#list"

################################################################
print("Receive page with proxie...")
time.sleep(0.1)
scraper = cfscrape.create_scraper()
page = scraper.get(prx_link)
print("Parsing prx page...")
time.sleep(0.1)
prx_soup = bs4.BeautifulSoup(page.text, "html.parser")
prx_soup = str(prx_soup)
#print(prx_soup)
print("Searching proxies...")
time.sleep(0.1)
all_prx = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{1,5}", prx_soup)
#print(all_prx)
print("Splitting...")
time.sleep(0.1)
s_all_prx = []
for prx in all_prx:
    cur_prx = re.split("</td><td>", prx)
    cur_prx = cur_prx[0]+":"+cur_prx[1]
    s_all_prx.append(cur_prx)
print("Proxies parsed:", len(s_all_prx))
time.sleep(0.1)
################################################################
print ("\nCounting pages")
time.sleep(0.1)
pcount = page_counter(link)
print ("Count pages: ", pcount)
time.sleep(0.1)
################################################################
print ("\nParsing links")
time.sleep(0.1)
all_links = links_parser(link, pcount)
print("Overal links parsed: ", len(all_links))
time.sleep(0.1)
################################################################
print("\nParsing items\n")
time.sleep(0.1)
all_items = items_parser(all_links)
print("Overal items parser: ", len(all_items))
time.sleep(0.1)
################################################################
#print (all_items)
print("Writting file...")
time.sleep(0.1)
print (type(all_items))
time.sleep(0.1)
with open("zalupa_test.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["link", "title", "price", "description"])
    for line in all_items:
        writer.writerow(line)
print("File writed!")
time.sleep(0.1)





#end of script
