from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, FadeTransition
from kivy.uix.textinput import TextInput


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
        playbutton.bind(on_press=self.timeout)
        self.add_widget(playbutton)

    def timeout(self, instance):
        Clock.schedule_once(self.transition, 0)

    def transition(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'starting_intro'
