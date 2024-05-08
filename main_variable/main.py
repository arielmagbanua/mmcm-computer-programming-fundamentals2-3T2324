def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def say_hi():
    print('Hi!')


class MyClass:
    def __init__(self, arg):
        self.arg = arg


if __name__ == '__main__':
    say_hi()

    my_class = MyClass('Foo')
    print(my_class.arg)
