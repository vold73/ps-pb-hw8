# создаем базовый класс с проверкой title на заполненность
class BaseClass():

    def __init__(self, title):
        if BaseClass.check_title(title):
            self.title = title
        else:
            raise ValueError

    @staticmethod
    def check_title(title):
        return len(title) > 0


class Product(BaseClass):

    def __init__(self, title, calorific, cost):
        BaseClass.__init__(self, title)
        self.calorific = calorific
        self.cost = cost


class Ingredient:

    def __init__(self, product, weight):
        self.product = product
        self.weight = weight

    @property
    def get_kkal(self):
        return self.weight / 100 * self.product.calorific

    @property
    def get_cost(self):
        return self.weight / 100 * self.product.cost


class Pizza(BaseClass):

    def __init__(self, title, ingredients):
        BaseClass.__init__(self, title)
        self.ingredients = ingredients
        self.sum_kkal = 0
        self.sum_cost = 0
        for prod in self.ingredients:
            self.sum_kkal += prod.get_kkal
            self.sum_cost += prod.get_cost

    @property
    def get_cost(self):
        return self.sum_cost

    @property
    def get_kkal(self):
        return self.sum_kkal


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт,
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

products = [dough_ingredient, tomato_ingredient, cheese_ingredient]

# Из ингредиентов создаем пиццу
margarita = Pizza('Маргарита', products)

# Выводим экземпляр пиццы
print(margarita.title + ' ( ' + str(margarita.get_kkal) +
      'kkal ) - ' + str(margarita.get_cost) + ' руб')