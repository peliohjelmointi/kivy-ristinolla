from kivy.app import App
from kivy.uix.widget import Widget 

class MyWidget(Widget):  
    pass

class MyApp(App): #pääohjelma, (jos)kv-file:myapp
    def build(self): # tätä kutsutaan, MyApp kutsutaan
        return MyWidget()

if __name__ =='__main__':
    MyApp().run() 