# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.clock import Clock
# from kivy.core.window import Window
#
# class Expedition(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__()
#
# class ExpeditionApp(App):
#     def build(self):
#         return Expedition()
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from starting_screen import StartingScreen
from intro_scenes import SceneOne, SceneTwo


class ExpeditionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartingScreen(name='starting_screen'))
        sm.add_widget(SceneOne(name='scene_one'))
        sm.add_widget(SceneTwo(name='scene_two'))
        return sm

if __name__ == '__main__':
    ExpeditionApp().run()
