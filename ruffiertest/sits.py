# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
from seconds import *
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from runner import *
from kivy.clock import Clock
from instructions import *

class Sits(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_scr = False
        inst = Label(text=txt_sits, size_hint=(0.5, 1))
        self.amount_sits = Sits_lbl(30)
        self.run = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.finished)

        hl = BoxLayout()
        vl = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        vl.add_widget(self.amount_sits)
        hl.add_widget(vl)
        hl.add_widget(self.run)

        self.btn = Button(text='Начать', size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = '#a7986c'

        vl2 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vl2.add_widget(hl)
        vl2.add_widget(self.btn)

        self.add_widget(vl2)

    def finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text = 'Считать пульс'
        self.next_scr = True

    def next(self):
        if not self.next_scr:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.amount_sits.next)
        else:
            self.manager.current = 'third'

class Sits_lbl(Label):
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = '[color=#000000]' + "Осталось приседаний: " + str(self.total) + '[/color]'
        super().__init__(text=my_text, markup=True, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        my_text = '[color=#000000]' + "Осталось приседаний: " + str(remain)  + '[/color]'
        self.text=my_text
