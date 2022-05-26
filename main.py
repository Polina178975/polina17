# Создание и запуск приложения, программирование интерфейса экранов и действий на них
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
# from instructions import txt_main, txt_two,txt_four
import ruffier
class MyApp(App):
     def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(TwoScr())
        sm.add_widget(TreeScr())
        sm.add_widget(FourScr())
        sm.add_widget(FiveScr())
        return sm
class ScrButton(Button):
    def __init__ (self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal



class MainScr(Screen):
    def __init__ (self, name="main"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.9,.1])
        layout3 = BoxLayout(size_hint=[0.9,.1])
        layout4 = BoxLayout(size_hint=[1,.7],padding=25)
        txt='''Данное приложение позволит вам с помощью текста Руфье провести\n пенвичную диагностику вашего здоровья.,\n
            'Проба Руфье предстовляет собой нагрузочный комплекс,\n преднозначенный для оценки работоспособности сердца при физической нагрузке.'''
        txt = Label(text=txt, markup=True)
        txt1= Label(text='Введите имя:    ')
        txt2= Label(text='Введите возраст:   ')
        btn = ScrButton(self, direction='left', goal="two", text='Начать')
        ti =TextInput(text="")
        ti2 = TextInput(text="")
        layout.add_widget(txt)
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(layout4)
        layout2.add_widget(txt1)
        layout3.add_widget(txt2)
        layout2.add_widget(ti)
        layout3.add_widget(ti2)
        layout4.add_widget(btn)
        self.add_widget(layout)
class TwoScr(Screen):
    global p
    def __init__ (self, name="two"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.009,.1])
        layout3= BoxLayout(size_hint=[0.9,.1])
        txt ='''Запишите пульс за 15 секунд.\n Результат запишите в соответствующее поле.'''
        txt=Label(text=txt, markup=True)
        txt1 = Label(text='Введите результат:  ')
        btn = ScrButton(self, direction='left', goal="tree", text='Продолжить')
        ti = TextInput(text='')
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(txt)
        layout3.add_widget(txt1)
        layout3.add_widget(ti)
        layout.add_widget(btn)
        
        # btn.on_press = p(ti.txt)
        self.add_widget(layout)
    # def p(b):
        # global p1
        # p1 = int(b)
        


class TreeScr(Screen):
    def __init__(self, name='tree'):
        super().__init__(name=name)
        layout = BoxLayout()
        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.09,.1])
        layout3= BoxLayout(size_hint=[0.9,.1])

        txt = Label(text='Выполни 30 пресиданий за 45 секунд',markup=True)
        btn = ScrButton(self, direction='left', goal="four", text='Продолжить')
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(txt)
        layout.add_widget(btn)
        self.add_widget(layout)
class FourScr(Screen):
    global p_1
    def __init__ (self, name='four'):
        super().__init__(name=name)
        layout = BoxLayout()
        self.add_widget(layout)
        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.9,.1])
        layout3 = BoxLayout(size_hint=[0.9,.1])
        layout4 = BoxLayout(size_hint=[1,.7],padding=25)
        txt='''В течении минуты замерьте пульс два раза:\n За первые 15 секунд минуты, затем за последние 15 секунд.\n Результаты запишите в соответствующие поля.'''
        txt = Label(text=txt, markup=True)
        txt1= Label(text='Результат:    ')
        txt2= Label(text='Результат после отдыха:   ')
        btn = ScrButton(self, direction='left', goal="five", text='Завершить')
        ti =TextInput(text="")
        ti2 = TextInput(text="")
        layout.add_widget(txt)
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(layout4)
        layout2.add_widget(txt1)
        layout3.add_widget(txt2)
        layout2.add_widget(ti)
        layout3.add_widget(ti2)
        layout4.add_widget(btn)
        # btn.on.press = p_1(ti,ti2)
        # btn.on_press= a(ti.txt)
        # btn.on_press= b(ti.txt)
        # btn.on_press = c(ti2.txt)
        self.add_widget(layout)
    # def p_1(a,c):
        # global p2, p3
        # p2 = int(a)
        # p3 = int(c)

class FiveScr(Screen):
    def __init__ (self, name='five'):
        super().__init__(name=name)
        layout = BoxLayout()
        txt =Label(text='')
        layout.add_widget(txt)
        self.add_widget(layout)
        
        
        
        


app = MyApp()
app.run()
