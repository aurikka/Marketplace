from decimal import Decimal
from django.conf import settings
from app_goods.models import Item


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, price, shop_id, quantity=1):
        """
        Добавить продукт в корзину
        """
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0,
                                  'price': str(price),
                                  'shop': str(shop_id),
                                  }
        self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        item_ids = self.cart.keys()
        # получение объектов item и добавление их в корзину
        items = Item.objects.filter(id__in=item_ids)
        for product in items:
            # по ключу item хранится экземпляр модели Item
            self.cart[str(product.id)]['item'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True