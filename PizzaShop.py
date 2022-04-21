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
        print(f'{exc_val=}')   # exception值
        print(f'{exc_tb=}')    # traceback
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


if __name__ == '__main__':
    M = ['燻雞', '臘腸', '蝦仁', '蟹肉棒', '鳳梨']
    customer_info = {'name': 'Nick', 'phone': '0974000111', 'email': 'abc@gmail.com'}

    with PizzaShop(shop_name='尼克披薩', shop_phone='04-26667777', is_open=True) as Ni:
        Ni.make_pizza(*M, sauce=SAUCE.cream, cheese=CHEESE.Cheddar, crust=CRUST.thin, **customer_info)
