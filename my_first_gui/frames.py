from breezypythongui.breezypythongui import EasyFrame, W, E, N, S


# welcome window
class WelcomeWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title='Welcome!', width=350, height=200)
        self.addLabel(text='Welcome!', row=0, column=0, rowspan=3, columnspan=3, sticky=W + E + N + S)


# login window
class LoginWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title='Login', width=350, height=200)

        # email text field
        self.addLabel(text='Email', row=0, column=0, sticky=W + N + S)
        self.email_field = self.addTextField(text='', row=0, column=1, columnspan=2, sticky=W)

        # password text field
        self.addLabel(text='Password', row=1, column=0, sticky=W + N + S)
        self.password_field = self.addTextField(text='', row=1, column=1, columnspan=2, sticky=W)

        self.addButton(text='Login', row=2, column=0, columnspan=3, command=self.on_login_click)

    def on_login_click(self):
        email = self.email_field.getValue()
        password = self.password_field.getValue()

        if email == 'test@tester.com' and password == 'test1234':
            # destroy current window and all child components
            self.destroy()

            # open new window
            welcome_window = WelcomeWindow()
            welcome_window.mainloop()
        else:
            self.messageBox(title='Login Failed!', message='Invalid email or password')


if __name__ == '__main__':
    main_window = LoginWindow()
    main_window.mainloop()
