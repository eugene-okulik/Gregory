class Flower:
    def __init__(self, name, color, freshness, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan

    def __str__(self):
        return (f"{self.color} {self.name} (свежесть: {self.freshness}/10, стебель: {self.stem_length}см, "
                f"цена: {self.price}р, живет: {self.lifespan} дней)")


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan=7):
        super().__init__("Роза", color, freshness, stem_length, price, lifespan)


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan=5):
        super().__init__("Тюльпан", color, freshness, stem_length, price, lifespan)


class Daisy(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan=10):
        super().__init__("Ромашка", color, freshness, stem_length, price, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness, reverse=True)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def find_by_lifespan(self, min_days, max_days):
        return [flower for flower in self.flowers if min_days <= flower.lifespan <= max_days]

    def __str__(self):
        return "\n".join(str(flower) for flower in
                         self.flowers) + (f"\nОбщая стоимость: {self.total_price()}р, "
                                          f"среднее время увядания: {self.average_lifespan():.1f} дней")


rose1 = Rose("красная", 9, 40, 150)
rose2 = Rose("белая", 8, 35, 120)
tulip = Tulip("желтый", 7, 30, 80)
daisy = Daisy("белая", 10, 25, 50)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip)
bouquet.add_flower(daisy)

print("Букет до сортировки:")
print(bouquet)

print("\nСортировка по свежести:")
bouquet.sort_by_freshness()
print(bouquet)

print("\nСортировка по цене:")
bouquet.sort_by_price()
print(bouquet)

print("\nПоиск цветов, которые живут от 5 до 8 дней:")
for flower in bouquet.find_by_lifespan(5, 8):
    print(flower)
