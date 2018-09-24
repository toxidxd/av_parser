import requests, bs4

#get page
soup = requests.get('https://www.avito.ru/rostov-na-donu/tovary_dlya_kompyutera/komplektuyuschie/videokarty?s_trg=7')

#write page to vairiable
b = bs4.BeautifulSoup(soup.text, "html.parser")

#selec all classes .price
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


#end of script
