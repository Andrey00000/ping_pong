from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

def b1_press(*args, **kwargs):
    print("Кнопка 1 нажата")

def b2_press(*args, **kwargs):
    print("Кнопка 2 нажата")

class BackButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(text=kwargs['text'])
        self.manager = kwargs['manager']
    def on_press(self, *args, **kwargs):
        self.manager.curreent = 'main'

class MyApp(App):
    def build(self):
        b1 = Button(text = "Играть")
        b1.on_press = b1_press

        b2 = Button(text = "Выйти")
        b2.bind(on_press = b2_press)

        layout = BoxLayout()
        layout.add_widget(b1)
        layout.add_widget(b2)

        self.manager = ScreeManager()
        s1 = Screen(name = 'main')
        s1.add_widget(layout)

        b3 = BackButton(text = "Назад", manager = self.manager)

        s2 = Screen(name = 'setting')
        s2.add_widget(b3)
        self.manager.add_widget(s1)
        self.manager.add_widget(s2)
        self.manager.current = "settings"
 
        return self.manager
app = MyApp()
app.run()
