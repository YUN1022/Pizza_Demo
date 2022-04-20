from enum import Enum


class CHEESE(Enum):
    Cheddar = '切達'
    Parmesan = '帕瑪森'


class SAUCE(Enum):
    ketchup = '紅醬'
    cream = '奶油'
    pesto = '青醬'


class CRUST(Enum):
    thin = '薄皮'
    thick = '手拍'


def make_pizza(*args, sauce: SAUCE, cheese: CHEESE, crust: CRUST, **kwargs):
    pizza_name = ''
    for material in args:
        pizza_name += material

    pizza_name += (sauce.value + cheese.value + crust.value + '披薩')
    order = {'披薩': pizza_name}
    order.update(kwargs)

    return order


if __name__ == '__main__':
    M = ['燻雞', '臘腸', '蝦仁', '蟹肉棒', '鳳梨']
    customer_info = {'name': 'Nick', 'phone': '0974000111', 'email': 'abc@gmail.com'}
    order1 = make_pizza(*M, sauce=SAUCE.cream, cheese=CHEESE.Cheddar, crust=CRUST.thin,
                        **customer_info)
    print(f'{order1=}')
