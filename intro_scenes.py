from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, FadeTransition, \
    SlideTransition
from kivy.uix.textinput import TextInput


# Scene 1:
class SceneOne(Screen):
    def __init__(self, **kwargs):
        super(SceneOne, self).__init__(**kwargs)

        # Scene One heading
        self.text = TextInput(
            font_size=120,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[0.2, 0.5, 0.9, 1],
            text="Background Info (Part 1):",
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
            font_size=120,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[0.2, 0.5, 0.9, 11],
            text="Background Info (Part 2):",
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
        Clock.schedule_once(self.scene_3, 0.8)

    def scene_3(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'scene_three'


class SceneThree(Screen):
    def __init__(self, **kwargs):
        super(SceneThree, self).__init__(**kwargs)

        self.text = TextInput(
            font_size=120,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[0.2, 0.5, 0.9, 1],
            text="Game Rules (Part 1):",
            cursor_width=0
        )
        self.add_widget(self.text)

        self.text = TextInput(
            font_size=70,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[0.6, 0.8, 0.9, 1],
            text="Throughout this game, you have to make various decisions to survive. At the start of the game you have 3 hearts. Every round, you will have 3 choices: the worst choice (-1 heart), a harmful but okay choice (-0.5 hearts), and a good choice (-0 hearts).",
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
        Clock.schedule_once(self.scene_4, 0.8)

    def scene_4(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'scene_four'

class SceneFour(Screen):
    def __init__(self, **kwargs):
        super(SceneFour, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=120,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[0.2, 0.5, 0.9, 11],
            text="Game Rules (Part 2):",
            cursor_width=0
        )
        self.add_widget(self.text)

        self.text = TextInput(
            font_size=80,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[0.6, 0.8, 0.9, 1],
            text="The goal is to try to survive by not running out of hearts. When you lose all three hearts, the game is over.\nNow that you know how this works, are you ready to play?",
            cursor_width=0
        )
        self.add_widget(self.text)

        nextbutton = Button(
            text="I'm Ready",
            font_size=70,
            size_hint=(0.3, 0.2),
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