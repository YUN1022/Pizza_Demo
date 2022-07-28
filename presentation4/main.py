from presentation4.decorator import say_hi, timer, logger


# @say_hi
# @timer
def fib(num: int):
    temp = [0, 1, 1]
    assert num > -1
    if num <= 2:
        return temp[num]

    for i in range(2, num):
        temp.append(temp[i - 1] + temp[i])

    return temp[-1]


if __name__ == '__main__':
    timer(say_hi(fib))(10)
