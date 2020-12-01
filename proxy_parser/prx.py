# -*- coding: utf-8 -*-

import requests, bs4, random, time, csv, re
import cfscrape
import subprocess
from fake_useragent import UserAgent

link = "https://hidemyna.me/ru/proxy-list/?country=RU&maxtime=2000&type=hs#list"

scraper = cfscrape.create_scraper()

page = scraper.get(link)

soup = bs4.BeautifulSoup(page.text, "html.parser")
#print(soup)
#prx = soup.select('.proxy__t')

#prx = soup.select(".d")
#print(soup)

soup = str(soup)

reg_res = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{1,5}", soup)
print(len(reg_res))
print(type(reg_res))
print(reg_res)

print("----splitting----")
all_prx = []

for prx in reg_res:
    cur_prx = re.split("</td><td>", prx)
    #print(res2)
    all_prx.append(cur_prx)


with open("proxies.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["IP", "port"])
    for line in all_prx:
        print(line)
        print(type(line))
        writer.writerow(line)


#i=0
#for x in prx:
#    prx[i] = str(prx[i])
#    res = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", prx[i])
#    print(res)
#    i+=1

#i=0
#for x in prx:
#    print(i)
#    print("===")
#    print(x)
#    i+=1
#print("===")


#res = re.findall("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", prx[1])
#print(res)

#tag = soup.find("td", class_="tdl").next_sibling
#print(tag)

#tag = soup.find("tr", class_="d").next_sibling
#print(tag)

#for sibling in soup.find("td", class_="tdl").previous_siblings:
    #print(sibling)

#prx = soup.find_all("tr", {"class":"d"})
