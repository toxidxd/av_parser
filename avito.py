import requests, bs4

s = requests.get('https://www.avito.ru/rostov-na-donu/tovary_dlya_kompyutera/komplektuyuschie/videokarty?s_trg=7')
b = bs4.BeautifulSoup(s.text, "html.parser")
#len = length.p1

p1 = b.select('.price')
#price = p1[0].getText()

d1 = b.select('.item-description-title-link')
#descript = d1[0].getText()
i = 0
for itm in p1:
    price = p1[i].getText()
    descript = d1[i].getText()
    print (descript + price)
    i+=1
#print(descript + price + '\n')

##


#---
