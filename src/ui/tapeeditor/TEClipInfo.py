import kivy
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('src/ui/tapeeditor/kv/te_clipinfo.kv')

class TEClipInfo(BoxLayout):
    pass

class TEClipInfoApp(App):
    
    def build(self):
        return TEClipInfo()

if __name__ == '__main__':
    TEClipInfoApp().run()