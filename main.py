from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from starting_screen import StartingScreen
from intro_scenes import SceneOne, SceneTwo, SceneThree, SceneFour
from transitions import IntroChoiceT, StartingIntroT
from choice_screens import EscapeShipC


class ExpeditionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartingScreen(name='starting_screen'))
        sm.add_widget(SceneOne(name='scene_one'))
        sm.add_widget(SceneTwo(name='scene_two'))
        sm.add_widget(SceneThree(name='scene_three'))
        sm.add_widget(SceneFour(name='scene_four'))
        sm.add_widget(IntroChoiceT(name='intro_choice'))
        sm.add_widget(StartingIntroT(name='starting_intro'))
        sm.add_widget(EscapeShipC(name='escape_ship_c'))
        return sm

if __name__ == '__main__':
    ExpeditionApp().run()
