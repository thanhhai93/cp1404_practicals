from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934


class DistanceConversionApp(App):
    """ DistanceConversionApp is a Kivy App for converting Miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


DistanceConversionApp().run()