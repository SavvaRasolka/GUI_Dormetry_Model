import pickle
from kivy import Config
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from Model import Model
from View import View
from Controller import Controller


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
        self.controller = Controller(Model("saved_step.pickle", "saved_step_2.pickle"), View(screen))
        self.controller.show_dorm()
        return screen


if __name__ == '__main__':
    entry = input('Выберите режим работы (введите цифру): \n1.Консоль\n2.Графический интерфейс')
    if entry == '1':
        with open('saved_step.pickle', 'rb') as f:
            our_dorm = pickle.load(f)
        f.close()
        with open('saved_step_2.pickle', 'rb') as f:
            our_dorm.set_room_list(pickle.load(f))
        f.close()
        our_dorm.set_mode(True)
        our_dorm.find_all_students()
        our_dorm.next_month()
        our_dorm.define_is_kitchen_okey()
        our_dorm.roach()
        our_dorm.noise_in_dorm()
        our_dorm.visit_every_room()
        our_dorm.change_duty()
        our_dorm.print_field()
        while True:
            entry = input('Введите команду\n')
            split_entry = entry.split()
            if split_entry[0] == 'help':
                print('kill_roach \'номер\' - убить тараканов в комнате\n'
                      'print_info_room \'номер\' - вывод информации о комнате\n'
                      'print_info_dorm - вывод информации об общежитии\n'
                      'check_in - заселить студентов в общежитие\n'
                      'exit - выход')
            elif split_entry[0] == 'kill_roach':
                for x in range(1, len(split_entry)):
                    try:
                        number_of_room = int(split_entry[x])
                        room = our_dorm.get_room_by_number(number_of_room)
                        room.kill_roach(True)
                    except ValueError:
                        print('Ожидается номер комнаты для очистки')
            elif split_entry[0] == 'print_info_room':
                try:
                    number_of_room = int(split_entry[1])
                    room = our_dorm.get_room_by_number(number_of_room)
                    room.print_info()
                except ValueError:
                    print('Ожидается номер комнаты для вывода информации')
            elif split_entry[0] == 'print_info_dorm':
                our_dorm.print_info()
            elif split_entry[0] == 'check_in':
                for x in range(1, len(split_entry)):
                    try:
                        number_of_room = int(split_entry[x])
                        room = our_dorm.get_room_by_number(number_of_room)
                        our_dorm.check_in(room)
                    except ValueError:
                        print('Ожидается номер комнаты для заселения')
            elif split_entry[0] == 'exit':
                break
            else:
                print('Неверный ввод, введите \'help\' чтобы увидеть список команд')
        with open("saved_step.pickle", "wb") as write_file:
            pickle.dump(our_dorm, write_file)
        write_file.close()

        with open("saved_step_2.pickle", "wb") as write_file:
            pickle.dump(our_dorm.get_room_list(), write_file)
        write_file.close()
    else:
        DormApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
