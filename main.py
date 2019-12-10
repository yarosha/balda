from kivy.app import App
from kivy.uix.button import Button
from random import randint
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from subprocess import Popen, PIPE
from time import sleep

Config.set("graphics", "width", 600)
Config.set("graphics", "heigth", 600)
Config.set("graphics", "resizable", 0)

class MyApp(App):
    def build(self):
        self.done = set()
        self.vocabulary = self.vocabulary()
        bl = BoxLayout(orientation="vertical")
        self.visor = Label(text="               Хи-хи ха-ха\nВот вам и хи-хи ха-ха девачки")
        self.points = [0, 0]
        bl.add_widget(self.visor)
        gl = GridLayout(cols=7)
        start = "геометр"
        self.done.add(start)
        self.word = ""
        self.turn = 0
        self.prev = 1
        self.field = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.used = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.prevx = 0
        self.prevy = 0
        for i in range(49):
            if (int(i / 7) == 3):
                gl.add_widget(Button(on_press=self.callback_press, font_size=90, text=start[i % 7]))
                self.field[int(i / 7)][i % 7] = 1
            else:
                gl.add_widget(Button(on_press=self.callback_press, font_size=90))
        bl.add_widget(gl)
        return bl
    
    def vocabulary(self):
        string = ''
        voc = []
        correct_vocabulary = {}
        f = open('vocabulary.txt', 'r', encoding='utf-8')
        for line in f:
            for i in range(len(line)-1):
                string += line[i]
            voc.append(string)
            string = ''
        for elem in voc:
            correct_vocabulary[elem] = len(elem)
        print(correct_vocabulary)
        return correct_vocabulary
    
    def check_function(self, word):
        if word in self.vocabulary.keys():
            return self.vocabulary[word]
        else:
            return 0
    
    def callback_press(self, instance):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        y, x = instance.pos
        print(x, y)
        x = int((x + 84.7142857143) / 85.7142857143)
        y = int(y / 171.42857142857142)
        print(x, y)
        print(self.field)
        if (instance.text == ""):
            if (self.prev == 0):
                return "sexy_olya"
            print(self.word)
            if (self.check_function(self.word)) and (self.word not in self.done):
                self.used = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
                self.done.add(self.word)
                print(self.done)
                self.points[self.turn] += self.check_function(self.word)
                self.turn = (self.turn + 1) % 2
            else:
                if (len(self.word) != 0):
                    self.word = ""
                    return "sexy_olya"
                self.word = ""
            fl = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                print("check", nx, ny)
                if (nx >= 0 and nx < 7 and ny >= 0 and ny < 7):
                    if (self.field[nx][ny]):
                        fl = True
            if (not fl):
                return "sexy_olya"
            process = Popen(['python3', 'keyboard.py'], preexec_fn=None)
            sleep(5)
            f = open("sexy_olya.txt", "r")
            letter = f.read()
            self.field[x][y] = 1
            instance.text = letter
            self.visor.text = "У первого игрока {} очков\nУ второго игрока {} очков".format(self.points[0], self.points[1])
            self.word = ""
            self.prev = 0
        else:
            if (self.used[x][y] != 0):
                return "sexy_olya"
            
            fl = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                print("check", nx, ny)
                if (nx >= 0 and nx < 7 and ny >= 0 and ny < 7):
                    if (nx == self.prevx and ny == self.prevy):
                        fl = True
            if ((not fl) and (len(self.word)) != 0):
                return "sexy_olya"
            self.word += instance.text
            self.prev = 1
            self.prevx = x
            self.prevy = y
        return 'okich'

if __name__ == '__main__':
    MyApp().run()
