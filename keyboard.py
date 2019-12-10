from kivy.app import App
from kivy.uix.button import Button
from random import randint
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from subprocess import Popen, PIPE

Config.set("graphics", "width", 1000)
Config.set("graphics", "heigth", 100)
Config.set("graphics", "resizable", 0)

class MyApp(App):
    def build(self):
        gl = GridLayout(cols=11)
        start = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.turn = 0
        self.field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.govno = [['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й'], ['к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф'], ['х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']]
        for i in range(33):
            gl.add_widget(Button(on_press=self.callback_press, font_size=90, text=start[i]))
        return gl
    
    def callback_press(self, instance):
        y, x = instance.pos
        print(x, y)
        x = int(x / 400)
        y = int((y + 180.8181818181818) / 181.8181818181818)
        print(x, y)
        print(self.govno[2 - x][y])
        print(self.field)
        f = open("sexy_olya.txt", "w")
        f.write(self.govno[2 - x][y]);
        
'''return Button(
        text = "olik",
        on_press=self.callback_press,
        on_release=self.callback_release
    )
    
def callback_press(self, instance):
    instance.text = "хи-хи ха-ха"
    
def  callback_release(self, instance):
    instance.text = "вот вам и хи-хи ха-ха девачки"
    instance.background_color = (randint(1, 100) / 100, randint(1, 100) / 100, randint(1, 100) / 100, randint(1, 100) / 100)'''

if __name__ == '__main__':
    MyApp().run()
