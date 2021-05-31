import kivy
from kivy.uix.label import Label

print(kivy.__version__)
kivy.require('2.0.0')

from kivy.app import App

class VShuffle(App):
    
    def build(self):
        return Label(text="Hello VShuffle")

if __name__ == '__main__':
    VShuffle().run()