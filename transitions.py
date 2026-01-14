from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, FadeTransition

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