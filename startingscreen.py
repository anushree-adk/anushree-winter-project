from kivy.app import App
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

# This is the starting screen that comes when run
class StartingScreen(Screen):
    def __init__(self, **kwargs):
        super(StartingScreen, self).__init__(**kwargs)

        # Title text
        self.text = TextInput(
            font_size=200,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            multiline=False,
            background_color=[0.9, 1, 0.9, 1],
            foreground_color=[0.1, 0.5, 0.2, 1],
            text="Expedition",
            cursor_width=0
        )
        self.add_widget(self.text)

        # Play button
        playbutton = Button(
            text="PLAY",
            font_size=70,
            size_hint=(0.2, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color=[0.1, 0.5, 0.2, 0.8],
            font_name="comic sans ms",
        )


        playbutton.bind(on_press=self.play_game)
        self.add_widget(playbutton)

    def play_game(self, instance):
        self.manager.current = 'scene_one'
        self.manager.transition.direction = 'left'


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
            background_color=[0.9, 1, 0.9, 1],
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
            background_color=[0.9, 1, 0.9, 1],
            text="You are on a cruise for a vacation, and people are running around in panic everywhere you look.",
            cursor_width=0
        )
        self.add_widget(self.text)


class ExpeditionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartingScreen(name='starting_screen'))
        sm.add_widget(SceneOne(name='scene_one'))
        return sm