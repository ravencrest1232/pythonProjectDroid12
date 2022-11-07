# importing all necessary modules
# like MDApp, MDLabel Screen, MDTextField
# and MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton




# creating Demo Class(base class)
class Demo(MDApp):

    def build(self):
        screen = Screen()

        # defining label with all the parameters
        l = MDLabel(text="HI PEOPLE!", halign='center',
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0.7, 1),
                    font_style='Caption')

        screen.add_widget(l)

        # defining Text field with all the parameters
        login = MDTextField(text="Ваш логин", pos_hint={
            'center_x': 0.5, 'center_y': 0.5},
                            size_hint_x=None, width=200)

        password = MDTextField(text="", pos_hint={
            'center_x': 0.5, 'center_y': 0.4},
                               size_hint_x=None, width=200)

        # defining Button with all the parameters
        btn = MDRectangleFlatButton(text="Войти", pos_hint={
            'center_x': 0.5, 'center_y': 0.3},
                                    on_release=self.btnfunc)
        # adding widgets to screen
        screen.add_widget(login)
        screen.add_widget(password)
        screen.add_widget(btn)

        # returning the screen
        return screen

    # defining a btnfun() for the button to
    # call when clicked on it
    def btnfunc(self, obj):
        print("button is pressed!!")


if __name__ == "__main__":
    Demo().run()
