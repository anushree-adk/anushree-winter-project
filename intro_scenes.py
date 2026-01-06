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

# Scene 1:
class SceneOne(Screen):
    def __init__(self, **kwargs):
        super(SceneOne, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[0.2, 0.5, 0.9, 1],
            text="Scene One:",
            cursor_width=0
        )
        self.add_widget(self.text)

        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[0.6, 0.8, 0.9, 1],
            text="You are on a cruise for a vacation, and suddenly people are running around in panic everywhere you look.",
            cursor_width=0
        )
        self.add_widget(self.text)

        nextbutton = Button(
            text="Next",
            font_size=70,
            size_hint=(0.2, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[0.2, 0.5, 0.9, 0.8],
            font_name="comic sans ms",
        )

        nextbutton.bind(on_press=self.timeout)
        self.add_widget(nextbutton)

    def timeout(self, instance):
        Clock.schedule_once(self.scene_2, 0.8)

    def scene_2(self, instance):
        self.manager.current = 'scene_two'
        self.manager.transition.direction = 'left'

class SceneTwo(Screen):
    def __init__(self, **kwargs):
        super(SceneTwo, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[0.2, 0.5, 0.9, 11],
            text="Scene Two:",
            cursor_width=0
        )
        self.add_widget(self.text)