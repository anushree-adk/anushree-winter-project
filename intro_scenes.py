from kivy.app import App
from kivy.compat import clock
from kivy.properties import StringProperty
from kivy.uix import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition, FallOutTransition, FadeTransition, \
    SlideTransition
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

        # Scene One heading
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

        # Scene One story
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

        # Next button - button to Scene Two
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
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'scene_two'


class SceneTwo(Screen):
    def __init__(self, **kwargs):
        super(SceneTwo, self).__init__(**kwargs)

        # Scene Two heading
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

        # Scene Two story
        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[0.6, 0.8, 0.9, 1],
            text="Someone next to you screams, 'The cruise is sinking!' You spring into action, quickly running to the nearest exit.",
            cursor_width=0
        )
        self.add_widget(self.text)

        # Next button - button to Scene Three
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
        Clock.schedule_once(self.transition, 0)

    def transition(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'intro_choice'


# class SceneThree(Screen):
#     def __init__(self, **kwargs):
#         super(SceneThree, self).__init__(**kwargs)
