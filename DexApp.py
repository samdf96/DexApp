import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.properties import (BooleanProperty,
                             StringProperty,
                             VariableListProperty)
from colors import ColorPicker
from data_buffer import Row, data_loader

kivy.require('1.11.1')
ROOT_DIR = '/home/samuelfielder/PycharmProjects/Kivy/DexApp/'
PIC_DIR = ROOT_DIR + 'CustomSprites/'
SAVES_DIR = ROOT_DIR + 'saves/'
OUTPUT_BASE = 'PoGo_Main_'

DATA, db, EXPORT_FILENAME = data_loader(0,
                                        150,
                                        8,
                                        SAVES_DIR,
                                        OUTPUT_BASE)


class BorderBase(Widget):
    pass
class NameLabel(BorderBase, Label):
    pass
class DexLabel(BorderBase, Label):
    pass
class ButtonBase(BorderBase, ToggleButton):
    toggle = BooleanProperty()
    pass


class DexEntry(FloatLayout, Row):
    name = StringProperty('')
    name_lookup = StringProperty('')
    dex_number = StringProperty('')
    type1 = StringProperty('')
    entry = BooleanProperty()
    lucky = BooleanProperty()
    fc = BooleanProperty()
    pic_source = StringProperty('')
    color_regular = VariableListProperty(1)
    color_light = VariableListProperty(1)
    color_dark = VariableListProperty(1)

    def __init__(self, data_row, data_buffer, import_data, **kwargs):
        super(DexEntry, self).__init__(data_row=data_row, data_buffer=data_buffer,
                                       import_data=import_data, **kwargs)
        self.data_row = data_row
        self.name_lookup = str(data_row['Name'].lower())
        self.pic_source = PIC_DIR + str(self.dex_number).zfill(3) + '.png'
        self.color_regular = ColorPicker(self.type1, 'regular')
        self.color_light = ColorPicker(self.type1, 'light')
        self.color_dark = ColorPicker(self.type1, 'dark')

class DexWindow(GridLayout):
    def __init__(self, **kwargs):
        super(DexWindow, self).__init__(**kwargs)
        self.cols = 3
        self.size_hint_y = None
        for index, row in DATA.iterrows():
            dex_entry = DexEntry(row, db, DATA)
            print(dex_entry.lucky)
            print(dex_entry._lucky)
            self.add_widget(dex_entry)
            if index == 0:
                break


class DexScrollWindow(ScrollView):
    def __init__(self):
        super(DexScrollWindow, self).__init__()
        dex_window = DexWindow()
        dex_window.bind(minimum_height=dex_window.setter('height'))
        self.add_widget(dex_window)


class DexApp(App):
    def build(self):
        return DexScrollWindow()


if __name__ == '__main__':

    # Load Data Here
    DexApp().run()
