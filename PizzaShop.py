import traceback

from PizzaOrder import SAUCE, CHEESE, CRUST


class PizzaShop:
    def __init__(self, shop_name: str, shop_phone: str, is_open: bool = True):
        self.shop_name = shop_name
        self.shop_phone = shop_phone
        self.is_open = is_open
        self.star = 0

    def __call__(self, *args, **kwargs):
        print(f'你好! 這裡是{self.shop_name}，請問要點什麼')

    def __len__(self):
        return len(self.shop_name)

    def __str__(self):
        return self.shop_name

    def __repr__(self):
        return self.shop_name

    def __bool__(self):
        return self.is_open

    # def __getattr__(self, item):
    #     return f'{self}沒有{item}屬性'
    #
    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value
    #     print(f'{key} 設置完成')

    def __enter__(self):
        print(f'{self.shop_name} 開店囉!!!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{exc_type=}')  # exception類型
        print(f'{exc_val=}')  # exception值
        print(f'{exc_tb=}')  # traceback
        if exc_tb:
            print(traceback.format_exc())

    def make_pizza(self, *args, sauce: SAUCE, cheese: CHEESE, crust: CRUST, **kwargs):
        pizza_name = ''
        for material in args:
            assert material != '鳳梨', '製作披薩失敗，你請的義大利籍廚師氣得不做了'
            pizza_name += material

        pizza_name += (sauce.value + cheese.value + crust.value + '披薩')
        order = {'店名': self.shop_name, '披薩': pizza_name}
        order.update(kwargs)

        return order

    def __lt__(self, other):
        return self.star < other.star

    def __le__(self, other):
        return self.star <= other.star

    def __eq__(self, other):
        return self.star == other.star

    def __gt__(self, other):
        return self.star > other.star

    def __ge__(self, other):
        return self.star >= other.star

    def __hash__(self):
        return hash(self.shop_name)


if __name__ == '__main__':
    Da = PizzaShop(shop_name='達美樂', shop_phone='04-26655252')
    Da2 = PizzaShop(shop_name='達美樂', shop_phone='04-26231855')
    Na = PizzaShop(shop_name='拿坡里', shop_phone='04-26633003')
    Bi = PizzaShop(shop_name='必勝客', shop_phone='04-26623300')

    my_favorite = [Da, Da2, Na, Bi]

    print(set(my_favorite))
