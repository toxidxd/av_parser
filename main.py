import requests, bs4

s = requests.get('https://sinoptik.com.ru/погода-ростов-на-дону')
b = bs4.BeautifulSoup(s.text, "html.parser")

p3 = b.select('.temperature .p3')
pogoda1 = p3[0].getText()
p4 = b.select('.temperature .p4')
pogoda2 = p4[0].getText()
p5 = b.select('.temperature .p5')
pogoda3 = p5[0].getText()
p6 = b.select('.temperature .p6')
pogoda4 = p6[0].getText()

print('Погода в Р-н-Д сегодня')
print('Morning: ' + pogoda1 + ' ' + pogoda2)
print('Day: ' + pogoda3 + ' ' + pogoda4)
p=b.select('.rSide .description')
pogoda=p[0].getText()
print(pogoda.strip())
p=b.select('.rSide .description')
pogoda=p[1].getText()
print(pogoda.strip())




#---
