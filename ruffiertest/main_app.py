# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
from sits import *
from kivy.core.window import Window

Window.clearcolor = ('#fff2cc')
btn_color = ('#a7986c')

class ScrButton(Button):
    def  __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal




class InstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vl.add_widget(Label(text=txt_instruction, markup=True))        
        self.ti1 = TextInput(text='7', halign='right', focus=False, multiline=False, size_hint=(.7, 1))
        self.ti2 = TextInput(text='------', halign='right', focus=False, multiline=False, size_hint=(.7, 1))
        hl1 = BoxLayout(size_hint=(.9, .1))
        hl2 = BoxLayout(size_hint=(.9, .1))
        hl1.add_widget(Label(text='[color=#000000]' + 'Имя' + '[/color]', markup=True, size_hint=(.3, 1)))
        hl1.add_widget(self.ti2)
        hl2.add_widget(Label(text='[color=#000000]' + 'Возвраст' + '[/color]', markup=True, size_hint=(.3, 1)))
        hl2.add_widget(self.ti1)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        self.btn = Button(text='Начать', size_hint=(.8, None), pos_hint={'center_x':.5, 'center_y':0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        vl.add_widget(self.btn)
        self.add_widget(vl)
    def next(self):
        global age, name, level
        age = check_int(self.ti1.text)
        if age == False:
            self.ti1.text = 'Недопустимое значение'
        elif age < 7:
            self.ti1.text = 'Минимальный возвраст 7'
        else:
            self.manager.current = 'first'
        name = self.ti2.text
        print (name, age)
        level = neud_level(age)
        print(level)





class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False 

        inst = Label(text=txt_test1, markup=True)
        self.time = Seconds()
        self.time.bind(done=self.do)

        hl = BoxLayout(size_hint=(.9, None), height='30sp')
        res_txt = Label(text='[color=#000000]' + 'Введите результат:' + '[/color]', markup=True, halign='right')
        self.ti1 = TextInput(text='0', multiline=False)
        self.ti1.set_disabled(True)
        hl.add_widget(res_txt)
        hl.add_widget(self.ti1)

        self.btn = Button(text='Начать')
        self.btn.on_press = self.next
        self.btn.background_color = btn_color

        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vl.add_widget(inst)
        vl.add_widget(self.time)
        vl.add_widget(hl)
        self.hl2 = BoxLayout(size_hint=(.8, None), height='80sp', pos_hint={'center_x':.5})
        self.hl2.add_widget(self.btn)
        vl.add_widget(self.hl2)

        self.add_widget(vl)


    def do(self, *args):
        self.next_screen = True 
        self.ti1.set_disabled(False)
        self.btn.set_disabled(False) 
        self.btn.text = "Продолжить"
    def next(self):
        global P1
        if not self.next_screen: 
            self.btn.set_disabled(True) 
            self.time.restart(total=5) 
        else:
            P1 = check_int(self.ti1.text)
            if P1 == False or P1 <= 0:
                self.ti1.text = 'Недопустимое значение'
            else:
                self.manager.current = 'second'
    
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vl.add_widget(Label(text=txt_test2, markup=True))
        self.btn = Button(text='Далее', size_hint=(.8, .2), pos_hint={'center_x':.5, 'center_y':0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        vl.add_widget(self.btn)
        self.add_widget(vl)  
    def next(self):
        self.manager.current = 'sits'
class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        hl1 = BoxLayout(padding=8, spacing=8, size_hint=(1, .07), pos_hint={'center_x':.5, 'center_y':0.5})
        hl2 = BoxLayout(padding=8, spacing=8, size_hint=(1, .07), pos_hint={'center_x':.5, 'center_y':0.5})
        hl3 = BoxLayout(padding=8, spacing=8, size_hint=(1, .07))
        vl.add_widget(Label(text=txt_test3, markup=True, size_hint=(1, .5)))
        self.now_txt = Label(text='[color=#000000]' + 'Измерьте пульс' + '[/color]', markup=True, size_hint=(1, .1))
        self.time = Seconds()
        hl3.add_widget(self.time)
        self.time.bind(done = self.do)
        vl.add_widget(self.now_txt)
        vl.add_widget(hl3)
        self.ti1 = TextInput(text='Результат', halign='right', focus=False, multiline=False)
        self.ti2 = TextInput(text='Результат', halign='right', focus=False, multiline=False)
        hl1.add_widget(Label(text='[color=#000000]' + 'Первое измерение' + '[/color]', markup=True, size_hint=(.3, .2), pos_hint={'center_x':.5, 'center_y':0.5}))
        hl2.add_widget(Label(text='[color=#000000]' + 'Второе измерение' + '[/color]', markup=True, size_hint=(.3, .2), pos_hint={'center_x':.5, 'center_y':0.5}))
        hl1.add_widget(self.ti1)
        hl2.add_widget(self.ti2)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        self.btn = Button(text='Далее', size_hint=(.8, .2), pos_hint={'center_x':.5, 'center_y':0.5})
        self.on_enter = self.before
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        vl.add_widget(self.btn)
        self.add_widget(vl)  
    def next(self):
        global P1, P2, P3, res, reslabel
        P2 = check_int(self.ti1.text)
        P3 = check_int(self.ti2.text)
        if P2 == False or P2 <= 0:
            self.ti1.text = 'Недопустимое значение'
        elif P3 == 'False' or P3 <= 0:
            self.ti2.text = 'Недопустимое значение'
        else:
            r_index = ruffier_index(P1, P2, P3)
            self.manager.current = 'result'
            res = ruffier_result(r_index, level)
            reslabel = res_label(name, r_index, res)
    def do(self, *args):  
        if self.time.done == True:
            if self.stage == 0:
                self.stage += 1
                self.time.restart(total = 10)
                self.now_txt.text = '[color=#000000]' + 'Отдыхайте' + '[/color]'
                self.ti1.set_disabled(False)
                print('a')      
            elif self.stage == 1:
                self.stage += 1
                self.time.restart(total = 5)
                self.now_txt.text = '[color=#000000]' + 'Измерьте пульс' + '[/color]'
                print('b')       
            elif self.stage == 2:
                self.ti2.set_disabled(False)
                self.btn.disabled = False
                self.btn.text ='Завершить'
                print('c')
    def before(self, *args):        
        self.btn.disabled = True
        self.ti1.set_disabled(True)
        self.ti2.set_disabled(True)
        self.time.restart(total = 5)
        




class ResScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.inst = Label(text=' ', markup=True)
        vl.add_widget(self.inst)
        self.add_widget(vl)
        self.on_enter = self.before
    def before(self):
        global reslabel
        self.inst.text = reslabel

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScreen(name='InstScr'))
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(Sits(name='sits'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(ResScreen(name='result'))
        return sm

app = MyApp()
app.run()
