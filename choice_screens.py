from kivy.app import App
from kivy.compat import clock
from kivy.properties import StringProperty
from kivy.uix import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image

# from constants import nextbutton


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
            text="You need to escape the ship fast and must make a decision. What will you use to get off the ship?",
            cursor_width=0
        )
        self.add_widget(self.text)

        tubebutton = Button(
            text="Float Tube",
            font_size=70,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.2, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        tubebutton.bind(on_press=self.tubescreen)
        self.add_widget(tubebutton)

        boatbutton = Button(
            text="Boat",
            font_size=70,
            size_hint=(0.2, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        boatbutton.bind(on_press=self.boatscreen)
        self.add_widget(boatbutton)

        jacketbutton = Button(
            text="Life Jacket",
            font_size=70,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.8, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        jacketbutton.bind(on_press=self.jacketscreen)
        self.add_widget(jacketbutton)


    def tubescreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[1, 1, 0.2, 1],
            text="This was a harmful but okay choice.\nYou escape with the float tube, but you have no supplies.\n\nYou're drifting off into the unknown waters, and eventually end up in a rainforest.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def boatscreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.4, 1, 0.2, 1],
            text="This was the best choice.\nYou escape with the boat, and you have some supplies to last you around a week.\n\nYou're drifting off into the unknown waters, and eventually end up in a rainforest.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def jacketscreen(self, instance):
        self.text = TextInput(
            font_size=70,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.8, 0.1, 0.1, 1],
            text="This was a bad choice.\nYou escape wearing a life jacket, but you have no supplies and are very cold. You haul yourself on a stray wooden board and go unconscious due to the cold.\n\nYou're drifting off into the unknown waters, and eventually end up in a rainforest.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def nextbutton(self):
        next = Button(
            text="Next",
            font_size=70,
            size_hint=(0.2, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        next.bind(on_press=self.timeout)
        self.add_widget(next)

    def timeout(self, instance):
        Clock.schedule_once(self.nextchoice, 0.8)

    def nextchoice(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'scene_two'

