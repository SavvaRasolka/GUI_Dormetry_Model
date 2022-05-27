from Student import Student

class Room:
    __number_of_room: int
    __number_of_students: int
    __students: list[Student]
    __room_neighbours: list['Room']
    __is_noisy: bool
    __is_source_of_noise: bool
    __is_duty: bool
    __is_roach: bool
    __dirty: int

    def __init__(self, number: int):
        self.__number_of_students = 0
        self.__students = []
        self.__room_neighbours = []
        self.__dirty = 0
        self.__is_roach = False
        self.__is_duty = False
        self.__is_source_of_noise = False
        self.__is_noisy = False
        self.__number_of_room = number
        self.__level_of_happiness = 0

    def get_students(self):
        return self.__students

    def get_is_source_of_noise(self):
        return self.__is_source_of_noise

    def get_is_duty(self):
        return self.__is_duty

    def get_is_roach_in_room(self):
        return self.__is_roach

    def get_is_noisy(self):
        return self.__is_noisy

    def get_room_neighbours(self):
        return self.__room_neighbours

    def get_dirty(self):
        return self.__dirty

    def get_number_of_students(self):
        return self.__number_of_students

    def get_number_of_room(self):
        return self.__number_of_room

    def add_neighbour_room(self, roomy: 'Room'):
        self.__room_neighbours.append(roomy)

    def add_student(self, student: Student):
        self.__number_of_students += 1
        self.__students.append(student)

    def noise_in_room(self):
        noise = 0
        for each_student in self.__students:
            noise += each_student.get_noise_level()
        if noise > 5:
            self.__is_noisy = False
            self.__is_source_of_noise = True
        else:
            self.__is_source_of_noise = False


    def move_out(self, stud: Student):
        self.__students.remove(stud)
        self.__number_of_students -= 1

    def set_duty(self, val: bool):
        self.__is_duty = val

    def set_roach(self, true_or_false: bool):
        self.__is_roach = true_or_false

    def set_is_noisy(self, true_or_false: bool):
        self.__is_noisy = true_or_false

    def movement_of_roach(self):
        if not self.__is_roach:
            if self.__dirty > 5:
                return self
        else:
            dirty_ratio = 0
            for each_room in self.__room_neighbours:
                if each_room.__is_roach:
                    continue
                else:
                    if each_room.__dirty >= dirty_ratio:
                        dirty_ratio = each_room.__dirty
                        dirtiest_room = each_room
                    return dirtiest_room
        return 0


    def kill_roach(self, mode):
        self.__is_roach = False
        self.__dirty = 0
        if mode:
            print('Тараканы уничтожены')


    def dirty_up(self):
        for each_student in self.__students:
            self.__dirty += each_student.get_cleanliness()
        if self.__dirty < 0:
            self.__dirty = 0

    def print_info(self):
        print("Номер комнаты: " + str(self.__number_of_room) + "\nКоличество студентов: " + str(
            self.__number_of_students))
        print("Источник шума:", end=" ")
        if self.__is_source_of_noise:
            print("является")
        else:
            print("не является")
        if self.__is_noisy:
            print("В комнате шумно")
        if self.__is_duty:
            print("Комната дежурит")
        if self.__is_roach:
            print("В комнате водятся тараканы")
        print("Уровень загрязнения комнаты: " + str(self.__dirty))
        print("___Информация о проживающих студентах___")
        for each_student in self.__students:
            each_student.print_info()
            print()