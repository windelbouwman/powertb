
import powertb
powertb.enable()


def my_func(x):
    y = x + 200
    print(y)
    if x > 0:
        my_func(x-1)
    else:
        return 1 / x


my_func(2)
