import requests, bs4

s = requests.get('https://www.avito.ru/rostov-na-donu/tovary_dlya_kompyutera/komplektuyuschie/videokarty?s_trg=7')

b = bs4.BeautifulSoup(s.content)

print(b)

p1 = b.select('.price')

#select all classes .item-descript-title-link
d1 = b.select('.item-description-title-link')

#cycle to print all results
i = 0
for itm in p1:
    price = p1[i].getText()
    descript = d1[i].getText()
    print (descript + price)
    i+=1
