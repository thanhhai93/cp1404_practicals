from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.names = ["nameone", "nametwo", "namethree", "namefour"]
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()


DynamicWidgetsApp().run()