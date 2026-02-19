PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

result = {
    x: int(price[:-1])
    for x, price in (line.split() for line in PRICE_LIST.split('\n'))
}

print(result)
