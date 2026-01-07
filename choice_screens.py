from kivy.app import App
from kivy.compat import clock
from kivy.properties import StringProperty
from kivy.uix import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image

class EscapeShipC(Screen):
    def __init__(self, **kwargs):
        super(EscapeShipC, self).__init__(**kwargs)

        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[1, 1, 1, 1],
            text="Your First Decision:",
            cursor_width=0
        )
        self.add_widget(self.text)

        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[1, 1, 1, 1],
            text="You need to escape the ship fast, and need to make a decision. How will you get off the ship?",
            cursor_width=0
        )
        self.add_widget(self.text)
