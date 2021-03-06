from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from functools import partial


class View:
    def __init__(self, screen, model, controller):
        self.screen = screen
        self.model = model
        self.controller = controller
        self.month = screen.ids.month
        self.kitchen = screen.ids.kitchen
        self.happiness = screen.ids.happiness
        self.students = []
        self.dirty = []
        self.roach = []
        self.noise = []
        self.source_noise = []
        self.duty = []
        self.field = 0
        for x in range(1, 16):
            self.students.append(screen.ids['student' + str(x)])
            self.dirty.append(screen.ids['dirty' + str(x)])
            self.roach.append(screen.ids['roach' + str(x)])
            self.noise.append(screen.ids['noise' + str(x)])
            self.duty.append(screen.ids['duty' + str(x)])
            self.source_noise.append(screen.ids['source_noise' + str(x)])

    def clear(self):
        for x in range(15):
            self.roach[x].clear_widgets(children=None)
            self.students[x].clear_widgets(children=None)
            self.noise[x].clear_widgets(children=None)
            self.duty[x].clear_widgets(children=None)
            self.source_noise[x].clear_widgets(children=None)

    def show_popup(self, msg):
        Popup(title='Предупреждение', size_hint=(0.5, 0.5),
              content=Label(text=msg)).open()

    def show_dorm(self):
        self.clear()
        self.happiness.text = "Уровень счастья: " + str(int(self.model.our_dorm.calculate_level_of_happiness())) + "/300"
        self.month.text = "Месяц: " + str(self.model.our_dorm.get_month())
        list_of_rooms = self.model.our_dorm.get_room_list()
        for x in range(15):
            room = list_of_rooms[x]
            self.dirty[x].text = str(room.get_dirty())
            if self.model.our_dorm.define_is_kitchen_okey():
                self.kitchen.source = 'img/kitchen.png'
            else:
                self.kitchen.source = 'img/kitchen_dirty.png'
            if room.get_is_duty():
                self.duty[x].add_widget(Image(source='img/duty.jpg'))
            if room.get_is_source_of_noise():
                self.source_noise[x].add_widget(Image(source='img/noise_source.jpg'))
            elif(room.get_is_noisy()):
                self.noise[x].add_widget(Image(source='img/noise.jpg'))
            if room.get_is_roach_in_room():
                self.roach[x].add_widget(Image(source='img/tarakan.jpg'))
            for student in room.get_students():
                layout = BoxLayout()
                layout.add_widget(Image(source='img/face.png'))
                layout.add_widget(Button(text='Инфо', on_press=partial(self.stud_info, student)))
                self.students[x].add_widget(layout)

    def stud_info(self, student, *args):
        Popup(title='Информация о студенте', size_hint=(0.5, 0.5),
              content=Label(text="Имя: " + student.get_name() + "\nШумность: " +
                            str(student.get_noise_level()) + "\nЧистоплотность: " +
                            str(student.get_cleanliness()) + "\nОтветственность: " +
                            str(student.get_responsability()) + "\nКоличество выговоров: " +
                            str(student.get_number_of_bans()) + "\nУспеваемость: " +
                            str(student.get_study()))).open()

    def kill_roach(self, room):
        self.controller.kill_roach(room)
        self.show_dorm()

    def add_student(self, room):
        if self.controller.add_student(room):
            self.show_dorm()
        else:
            self.show_popup('В комнате нет места')

    def next_step(self):
        self.model.update()
        if self.model.our_dorm.get_month() == 4:
            self.show_popup("Осторожно! В следующем месяце сессия")
        self.show_dorm()

