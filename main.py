import pickle
from kivy import Config
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from Model import Model
from View import View
from Controller import Controller
from mai_func import main


Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'width', 900)
Config.write()


class MainWindow(Widget):
    pass


class DormApp(MDApp):
    def build(self):
        self.title = "Dormetry"
        screen = MainWindow()
        model = Model("saved_step.pickle", "saved_step_2.pickle")
        controller = Controller(model)
        self.view = View(screen, model, controller)
        self.controller = Controller(model)
        self.view.show_dorm()
        return screen


if __name__ == '__main__':
    entry = input('Выберите режим работы (введите цифру): \n1.Консоль\n2.Графический интерфейс')
    if entry == '1':
        main()
    else:
        DormApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
