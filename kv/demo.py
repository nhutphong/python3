from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class ButtonApp(App):
    def build(self):
        return Button(text='Hello Button')

class LabelApp():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = Label(text="hello label")

class MyApp(App):
    def build(self):
        return LabelApp()

if __name__ == "__main__":
   MyApp().run()
