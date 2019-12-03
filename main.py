from kivy.app import App
from kivy.uix.button import Button
from random import randint
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

Config.set("graphics", "width", 600)
Config.set("graphics", "heigth", 300)
Config.set("graphics", "resizable", 0)


class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation="vertical")
        self.visor = Label(text="First turn")
        bl.add_widget(self.visor)
        gl = GridLayout(cols=3)
        self.turn = 0;
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(9):
            gl.add_widget(Button(on_press=self.callback_press, font_size=100))
        bl.add_widget(gl)
        return bl

if __name__ == '__main__':
    MyApp().run()