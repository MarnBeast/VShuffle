import kivy
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('src/ui/tapeeditor/kv/tapeeditorwide.kv')
Builder.load_file('src/ui/tapeeditor/kv/te_videosources.kv')
Builder.load_file('src/ui/tapeeditor/kv/te_tapeinfo.kv')
Builder.load_file('src/ui/tapeeditor/kv/te_clips.kv')

class TapeEditorWide(Widget):
    pass

class TapeEditorWideApp(App):
    
    def build(self):
        return TapeEditorWide()

if __name__ == '__main__':
    from TEClipInfo import TEClipInfo
    TapeEditorWideApp().run()
else:
    from ui.tapeeditor.TEClipInfo import TEClipInfo