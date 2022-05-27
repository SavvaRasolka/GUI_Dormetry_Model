import random


class Student:
    __name: str
    __noise_level: int
    __cleanliness: int
    __number_of_bans: int
    __responsability: int
    __study: int
    all_names = ['Павел', 'Матвей', 'Пётр', 'Григорий', 'Кирилл', 'Глеб', 'Антон', 'Аркадий', 'Геннадий',
                 'Сергей', 'Виктор', 'Андрей', 'Евгений', 'Алексей', 'Егор', 'Арсений', 'Владислав', 'Николай',
                 'Александр', 'Иван', 'Семён', 'Ростислав', 'Катерина', 'Константин', 'Владимир', 'Никита', 'Игорь',
                 'Вадим', 'Илья', 'Роман', 'Даниил', 'Михаил', 'Дмитрий', 'Савва', 'Валерий', 'Артем', 'Виталий',
                 'Василий',
                 'Тимофей', 'Кузьма', 'Максим', 'Станислав', 'Родион', 'Артур', 'Валерьян']
    all_surnames = ['Петров', 'Нестеров', 'Иванов', 'Синявский', 'Барановский', 'Бодров', 'Лисичкин', 'Кузнецов',
                    'Столер', 'Вершинин', 'Заневский', 'Загорский', 'Брилевский', 'Плетнёв', 'Горбачёв', 'Никифоров',
                    'Стручков', 'Янковский', 'Цветков', 'Рудницкий', 'Вашкевич', 'Федотов', 'Кисель', 'Таченко',
                    'Соколов',
                    'Звягинцев', 'Расолько', 'Ковальский', 'Халецкий', 'Неборский', 'Пупин', 'Овечко', 'Валюшок',
                    'Газда',
                    'Меркулов', 'Островский', 'Шлячин', 'Ярмошук', 'Смоляк', 'Батяй', 'Морозов', 'Швейко', 'Клименко',
                    'Максименко', 'Тарасов', 'Драпей', 'Кириллов', 'Подорожный', 'Карачун', 'Степанов', 'Рассафонов',
                    'Пищ',
                    'Щетько', 'Роговец', 'Сергеев', 'Скеля', 'Смирнов', 'Чугуйкий', 'Сыроежкин', 'Есенин', 'Кафка',
                    'Гусаров', 'Белый', 'Дегтярев', 'Чехов', 'Пушкин', 'Щукин', 'Миклуха', 'Воронин', 'Крылов',
                    'Шульга',
                    'Петренко', 'Киценко', 'Пличко', 'Иванцов', 'Гавриленко', 'Звягинцев', 'Новиков', 'Круглов',
                    'Озерский',
                    'Сахаров', 'Семенов', 'Сербин', 'Душман', 'Василенко', 'Суслов', 'Лебедев']


    def __init__(self):
        self.__name = random.choice(self.all_names) + " " + random.choice(self.all_surnames)
        self.__number_of_bans = 0
        self.__noise_level = random.randint(0, 4)
        self.__cleanliness = random.choice([-1, 0, 2])
        self.__responsability = random.randint(1, 5)
        self.__study = random.randint(1, 3)

    def get_name(self):
        return self.__name

    def get_study(self):
        return self.__study

    def get_noise_level(self):
        return self.__noise_level

    def get_cleanliness(self):
        return self.__cleanliness

    def get_number_of_bans(self):
        return self.__number_of_bans

    def get_responsability(self):
        return self.__responsability

    def give_ban(self, mode):
        self.__number_of_bans += 1
        if mode:
            print("Студент " + self.__name + " получил выговор")

    def check_kick(self) -> bool:
        if self.__number_of_bans >= 2:
            return True
        else:
            return False

    def exams(self, mode):
        results = -1
        if self.__study == 1:
            results = random.randint(0, 4)
        if self.__study == 2:
            results = random.randint(0, 9)
        if self.__study == 3:
            results = random.randint(0, 15)
        if results == 0:
            if mode:
                print("Студент " + self.__name + " завалил сессию и был отчислен")
            return False
        else:
            return True

    def print_info(self):
        print("Имя студента: " + self.__name + "\nКоличество выговоров: " + str(
            self.__number_of_bans) + "\nУровень шума: " +
              str(self.__noise_level) + "\nУровень чистоплотности: " + str(
            self.__cleanliness) + "\nУровень ответственности: " +
              str(self.__responsability) + "\nУспеваемость: " + str(self.__study))
