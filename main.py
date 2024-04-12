from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.graphics import Ellipse

class MyWidget(Widget):
    def __init__(self):
        super().__init__()

class MyApp(App): #pääohjelma, (jos)kv-file:myapp
    def build(self): # tätä kutsutaan, MyApp kutsutaan
        return MyWidget()

if __name__ =='__main__':
    MyApp().run() #run käynnistää ohjelman