class Flower:
    def __init__(self, name, color, stem_length, price, freshness, life_time):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.freshness = freshness
        self.life_time = life_time

    def __repr__(self):
        return (
            f"{self.name}(цвет={self.color}, длина={self.stem_length} см, "
            f"цена={self.price}р, время жизни={self.life_time} дней, свежесть={self.freshness})"
        )


class Rose(Flower):
    def __init__(self, color, stem_length, price, freshness):
        super().__init__("Rose", color, stem_length, price, freshness, life_time=7)
        # life_time захардкодил тут, и не выносил как самостоятельную переменную в дочерних классах для более удобного принта


class Chamomile(Flower):
    def __init__(self, color, stem_length, price, freshness):
        super().__init__("Chamomile", color, stem_length, price, freshness, life_time=5)


class Lily(Flower):
    def __init__(self, color, stem_length, price, freshness):
        super().__init__("Lily", color, stem_length, price, freshness, life_time=8)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def bouquet_price(self):
        return sum(f.price for f in self.flowers)

    def average_life_time(self):
        if not self.flowers:
            return 0
        return sum(f.life_time for f in self.flowers) / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.price)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda f: f.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda f: f.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda f: f.stem_length)

    def find_by_life_time(self, min_life, max_life):
        return [f for f in self.flowers if min_life <= f.life_time <= max_life]


rose1 = Rose("red", 30, 8, '1.fresh')
rose2 = Rose("yellow", 45, 7, '2.middle_fresh')
chamomile1 = Chamomile("yellow", 40, 3, '3.not_fresh')
lily1 = Lily("white", 35, 6, '4.expired')

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(chamomile1)
bouquet.add_flower(lily1)

print("Цветы в букете:", bouquet.flowers)
print("Стоимость букета:", bouquet.bouquet_price())
print("Среднее время жизни:", bouquet.average_life_time())

# Сортировка
bouquet.sort_by_price()
print("После сортировки по цене:", bouquet.flowers)
bouquet.sort_by_freshness()
print("После сортировки по свежести:", bouquet.flowers)

# Поиск
result = bouquet.find_by_life_time(6, 8)
print("Цветы с временем жизни 6-8 дней:", result)