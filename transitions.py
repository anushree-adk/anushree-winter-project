from kivy.app import App
from kivy.compat import clock
from kivy.properties import StringProperty
from kivy.uix import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from constants import transTime


class StartingIntroT(Screen):
    def __init__(self, **kwargs):
        super(StartingIntroT, self).__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.choice, transTime)

    def choice(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'scene_one'

class IntroChoiceT(Screen):
    def __init__(self, **kwargs):
        super(IntroChoiceT, self).__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.choice, transTime)

    def choice(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'escape_ship_c'

class ChoiceGameoverT(Screen):
    def __init__(self, **kwargs):
        super(ChoiceGameoverT, self).__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.choice, transTime)

    def choice(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'game_over'

class ChoiceSurviveT(Screen):
    def __init__(self, **kwargs):
        super(ChoiceSurviveT, self).__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.choice, transTime)

    def choice(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'you_survived'