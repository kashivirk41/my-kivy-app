from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return Button(text='Hello, Click Me!')

if __name__ == '__main__':
    MainApp().run()
