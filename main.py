from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.graphics import Ellipse

class MyWidget(Widget):
    def __init__(self):
        super().__init__()
        # self.bind(pos=self.update_canvas)
        # self.bind(size=self.update_canvas)       
        self.update_canvas()        
       
    def update_canvas(self, *args):
        self.canvas.clear() #tyhjää canvaksen
        with self.canvas: #mitä canvakselle piirretään
            #Ellipse(pos=self.pos, size=self.size)
            self.e =Ellipse()            

    def on_size(self,*args):#kutsutaan, kun ikkunan koko muuttuu
        self.e.pos = self.pos
        self.e.size = self.size

class MyApp(App): #pääohjelma, (jos)kv-file:myapp
    def build(self): # tätä kutsutaan, MyApp kutsutaan
        return MyWidget()

if __name__ =='__main__':
    MyApp().run() #run käynnistää ohjelman