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
import hearts

life = 3

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
            text=f"Your Hearts: {life}",
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
        global life
        life -= 0.5

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
        global life
        life -= 1

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
        self.manager.current = 'first_choice'

class FirstChoice(Screen):
    def on_enter(self, *args):
        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[1, 1, 1, 1],
            text=f"Your hearts: {life}",
            cursor_width=0
        )
        self.add_widget(self.text)
    def __init__(self, **kwargs):
        super(FirstChoice, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[1, 1, 1, 1],
            text="You have survived but are tired, hungry, and alone. What do you do first?",
            cursor_width=0
        )
        self.add_widget(self.text)

        shelterbutton = Button(
            text="Look for Shelter",
            font_size=60,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.2, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        shelterbutton.bind(on_press=self.shelterscreen)
        self.add_widget(shelterbutton)

        foodbutton = Button(
            text="Search for Food",
            font_size=60,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        foodbutton.bind(on_press=self.foodscreen)
        self.add_widget(foodbutton)

        explorebutton = Button(
            text="Explore the Forest",
            font_size=55,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.8, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        explorebutton.bind(on_press=self.explorescreen)
        self.add_widget(explorebutton)

    def shelterscreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.4, 1, 0.2, 1],
            text="This was the best choice.\nYou stay dry and protected, preserving your energy. You make it safely through the day.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def foodscreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[1, 1, 0.2, 1],
            text="This was a harmful but okay choice.\nYou find some food, but it’s risky. You gain a little energy but still feel weak.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()
        global life
        life -= 0.5

    def explorescreen(self, instance):
        self.text = TextInput(
            font_size=70,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.8, 0.1, 0.1, 1],
            text="This was a bad choice.\nYou waste energy and get lost. Night comes faster than expected.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()
        global life
        life -= 1

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
        self.manager.current = 'night_choice'

class NightChoice(Screen):
    def on_enter(self, *args):
        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[1, 1, 1, 1],
            text=f"Your hearts: {life}",
            cursor_width=0
        )
        self.add_widget(self.text)
    def __init__(self, **kwargs):
        super(NightChoice, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[1, 1, 1, 1],
            text="It is now nighttime and you need to stay safe. How do you survive the night?",
            cursor_width=0
        )
        self.add_widget(self.text)

        firebutton = Button(
            text="Make a Fire",
            font_size=60,
            size_hint=(0.25, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        firebutton.bind(on_press=self.firescreen)
        self.add_widget(firebutton)

        leavesbutton = Button(
            text="Hide Under Leaves",
            font_size=60,
            size_hint=(0.35, 0.2),
            pos_hint={"center_x": 0.2, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        leavesbutton.bind(on_press=self.leavesscreen)
        self.add_widget(leavesbutton)

        walkbutton = Button(
            text="Walk at Night",
            font_size=55,
            size_hint=(0.25, 0.2),
            pos_hint={"center_x": 0.8, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        walkbutton.bind(on_press=self.walkscreen)
        self.add_widget(walkbutton)

    def firescreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.4, 1, 0.2, 1],
            text="This was the best choice.\nThe fire keeps you warm and scares away animals.You feel safer and wake up stronger.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def leavesscreen(self, instance):
        global life
        life -= 0.5
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[1, 1, 0.2, 1],
            text="This was a harmful but okay choice. -0.5 heart\nYou stay dry and get rest, but you are cold, making you feel unwell.",
            cursor_width=0
            )
        self.add_widget(self.text)
        self.nextbutton()
        # global life
        # life -= 0.5

    def walkscreen(self, instance):
        global life
        life -= 1
        if life > 0:
            self.text = TextInput(
                font_size=70,
                font_name='comic sans ms',
                readonly=True,
                halign="center",
                background_color=[0.8, 0.1, 0.1, 1],
                text="This was a bad choice. -1 heart\nYou trip and hurt yourself, losing a lot of energy.",
                cursor_width=0
            )
            self.add_widget(self.text)
            self.nextbutton()
        else:
            self.transition()

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
        self.manager.current = 'water_choice'

    def transition(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'choice_gameover'

class WaterChoice(Screen):
    def on_enter(self, *args):
        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[1, 1, 1, 1],
            text=f"Your hearts: {life}",
            cursor_width=0
        )
        self.add_widget(self.text)
    def __init__(self, **kwargs):
        super(WaterChoice, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[1, 1, 1, 1],
            text="You have gone hours without drinking water and are ow thirsty. How do you get water?",
            cursor_width=0
        )
        self.add_widget(self.text)

        riverbutton = Button(
            text="Follow a River",
            font_size=60,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.2, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        riverbutton.bind(on_press=self.riverscreen)
        self.add_widget(riverbutton)

        rainbutton = Button(
            text="Collect Rain",
            font_size=60,
            size_hint=(0.25, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        rainbutton.bind(on_press=self.rainscreen)
        self.add_widget(rainbutton)

        puddlebutton = Button(
            text="Drink From Puddles",
            font_size=55,
            size_hint=(0.35, 0.2),
            pos_hint={"center_x": 0.8, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        puddlebutton.bind(on_press=self.puddlescreen)
        self.add_widget(puddlebutton)

    def riverscreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.35, 1, 0.2, 1],
            text="This was the best choice.\nYou find clean water and fish, regaining strength.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def rainscreen(self, instance):
        global life
        life -= 0.5
        if life > 0:
            self.text = TextInput(
                font_size=85,
                font_name='comic sans ms',
                readonly=True,
                halign="center",
                background_color=[1, 1, 0.2, 1],
                text="This was a harmful but okay choice. -0.5 heart\nYou get some water, but not much. You end up staying thirsty.",
                cursor_width=0
            )
            self.add_widget(self.text)
            self.nextbutton()
        else:
            self.transition()

    def puddlescreen(self, instance):
        global life
        life -= 1
        if life > 0:
            self.text = TextInput(
                font_size=90,
                font_name='comic sans ms',
                readonly=True,
                halign="center",
                background_color=[0.8, 0.1, 0.1, 1],
                text="This was a bad choice. -1 heart\nThe water is dirty and full of harmful bacteria, which makes you get sick.",
                cursor_width=0
            )
            self.add_widget(self.text)
            self.nextbutton()
        else:
            self.transition()

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
        self.manager.current = 'plan_choice'

    def transition(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'choice_gameover'

class PlanChoice(Screen):
    def on_enter(self, *args):
        self.text = TextInput(
            font_size=150,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            size_hint_y=0.2,
            background_color=[1, 1, 1, 1],
            text=f"Your hearts: {life}",
            cursor_width=0
        )
        self.add_widget(self.text)
    def __init__(self, **kwargs):
        super(PlanChoice, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=100,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            background_color=[1, 1, 1, 1],
            text="You need to think of a way to survive and get noticed by rescuers. What’s your long-term plan?",
            cursor_width=0
        )
        self.add_widget(self.text)

        signalbutton = Button(
            text="Signal for Help",
            font_size=60,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.8, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        signalbutton.bind(on_press=self.signalscreen)
        self.add_widget(signalbutton)

        adaptbutton = Button(
            text="Stay and Adapt",
            font_size=60,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        adaptbutton.bind(on_press=self.adaptscreen)
        self.add_widget(adaptbutton)

        giveupbutton = Button(
            text="Give Up Hope",
            font_size=55,
            size_hint=(0.3, 0.2),
            pos_hint={"center_x": 0.2, "center_y": 0.17},
            background_color=[1, 1, 1, 1],
            font_name="comic sans ms",
        )
        giveupbutton.bind(on_press=self.giveupscreen)
        self.add_widget(giveupbutton)

    def signalscreen(self, instance):
        self.text = TextInput(
            font_size=85,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.4, 1, 0.2, 1],
            text="This was the best choice.\nSmoke and signals are visible, so rescuers eventually notice you.",
            cursor_width=0
        )
        self.add_widget(self.text)
        self.nextbutton()

    def adaptscreen(self, instance):
        global life
        life -= 0.5
        if life > 0:
            self.text = TextInput(
                font_size=85,
                font_name='comic sans ms',
                readonly=True,
                halign="center",
                background_color=[1, 1, 0.2, 1],
                text="This was a harmful but okay choice. -0.5 heart\nYou survive, but rescue is slow. Life is hard but possible.",
                cursor_width=0
            )
            self.add_widget(self.text)
            self.nextbutton()
        else:
            self.transition()

    def giveupscreen(self, instance):
        global life
        life -= 1
        if life > 0:
            self.text = TextInput(
                font_size=90,
                font_name='comic sans ms',
                readonly=True,
                halign="center",
                background_color=[0.8, 0.1, 0.1, 1],
                text="This was a bad choice. -1 heart\nYou stop trying and survival becomes very difficult.",
                cursor_width=0
            )
            self.add_widget(self.text)
            self.nextbutton()
        else:
            self.transition()

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
        Clock.schedule_once(self.ending, 0.8)

    def ending(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = 'choice_survive'

    def transition(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'choice_gameover'

class YouSurvived(Screen):
    def __init__(self, **kwargs):
        super(YouSurvived, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=120,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.4, 1, 0.2, 1],
            text="YOU WON!\n\n You didn't run out of hearts.\nYou survived the rainforest.",
            cursor_width=0
        )
        self.add_widget(self.text)

class GameOver(Screen):
    def __init__(self, **kwargs):
        super(GameOver, self).__init__(**kwargs)
        self.text = TextInput(
            font_size=120,
            font_name='comic sans ms',
            readonly=True,
            halign="center",
            background_color=[0.8, 0.1, 0.1, 1],
            text="GAME OVER\n\nYou lost all your hearts.\nYou failed to survive the rainforest.",
            cursor_width=0
        )
        self.add_widget(self.text)
