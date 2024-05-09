def print_hi(name):
    print(f'Hi, {name}')


def say_hi():
    print('Hi!')


class MyClass:
    def __init__(self, arg):
        self.arg = arg


if __name__ == '__main__':
    say_hi()

    my_class = MyClass('Foo')
    print(my_class.arg)
