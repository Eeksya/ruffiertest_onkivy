# напиши модуль для реализации секундомера
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, **kwargs):
        self.done = False
        self.current = 0
        my_text = '[color=#000000]' + 'Прошло секунд: ' + str(self.current) + '[/color]'
        super().__init__(text=my_text, markup=True)


    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = '[color=#000000]' + 'Прошло секунд: ' + str(self.current) + '[/color]'
        self.start()
            

    def start(self):
        Clock.schedule_interval(self.change, 1)


    def change(self, dt):
        self.current += 1
        self.text = '[color=#000000]' + 'Прошло секунд: ' + str(self.current) + '[/color]'
        if self.current >= self.total:
            self.current = 0
            self.done = True
            return False
            