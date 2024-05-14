# if you installed via pip
from breezypythongui.breezypythongui import EasyFrame
# if you manually installed the library to your project directory
# from breezypythongui import EasyFrame


class MyApp(EasyFrame):
    def __init__(self, arg):
        # call original constructor and provide the initial width and length
        EasyFrame.__init__(self, title='My App', width=400, height=200)
        self.arg = arg


if __name__ == '__main__':
    my_app = MyApp(arg="test")
    my_app.mainloop()
