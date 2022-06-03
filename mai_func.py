import pickle
import click
from click_shell import shell


@shell(prompt='общежитие-> ', intro='Запуск симуляции общежития...')
def main():
    with open('saved_step.pickle', 'rb') as f:
        global our_dorm
        our_dorm = pickle.load(f)
    f.close()
    with open('saved_step_2.pickle', 'rb') as f:
        our_dorm.set_room_list(pickle.load(f))
    f.close()
    our_dorm.find_all_students()
    our_dorm.next_month()
    our_dorm.define_is_kitchen_okey()
    our_dorm.roach()
    our_dorm.noise_in_dorm()
    our_dorm.visit_every_room()
    our_dorm.change_duty()
    our_dorm.print_field()
    save_to_file()


def save_to_file():
    with open("saved_step.pickle", "wb") as write_file:
        pickle.dump(our_dorm, write_file)
    write_file.close()

    with open("saved_step_2.pickle", "wb") as write_file:
        pickle.dump(our_dorm.get_room_list(), write_file)
    write_file.close()


@main.command(help='Убить тараканов в комнате(введите номер комнаты)')
@click.argument('num')
def kill_roach(num):
    try:
        room = our_dorm.get_room_by_number(int(num))
        room.kill_roach()
        save_to_file()
    except IndexError:
        print('В общежитии 15 комнат, введите число от 1 до 15')


@main.command(help='Вывод информации о комнате(введите номер комнаты)')
@click.argument('num')
def info_room(num):
    try:
        room = our_dorm.get_room_by_number(int(num))
        room.print_info()
    except IndexError:
        print('В общежитии 15 комнат, введите число от 1 до 15')


@main.command(help='Вывод информации об общежитии')
def info_dorm():
    our_dorm.print_info()


@main.command(help='Заселить студента в комнату(введите номер комнаты)')
@click.argument('num')
def check_in(num):
    try:
        room = our_dorm.get_room_by_number(int(num))
        our_dorm.check_in(room)
        save_to_file()
    except IndexError:
        print('В общежитии 15 комнат, введите число от 1 до 15')


@main.command(help='Вывод карты общежития')
def print_map():
    our_dorm.print_field()
