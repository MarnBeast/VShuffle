import kivy
from ui.tapeeditor.TapeEditorWide import TapeEditorWide

print(kivy.__version__)
kivy.require('2.0.0')

from kivy.app import App

class VShuffle(App):
    
    def build(self):
        return TapeEditorWide()

if __name__ == '__main__':
    VShuffle().run()