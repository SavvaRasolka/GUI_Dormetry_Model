import pickle


class Model:
    def __init__(self, f1, f2):
        with open(f1, 'rb') as f:
            dorm = pickle.load(f)
        f.close()
        with open(f2, 'rb') as f:
            dorm.set_room_list(pickle.load(f))
        f.close()
        dorm.find_all_students()
        dorm.set_mode(False)
        self.our_dorm = dorm

    def update(self):
        self.our_dorm.next_month()
        self.our_dorm.define_is_kitchen_okey()
        self.our_dorm.roach()
        self.our_dorm.noise_in_dorm()
        self.our_dorm.visit_every_room()
        self.our_dorm.change_duty()

    def save_to_file(self):
        with open("saved_step.pickle", "wb") as write_file:
            pickle.dump(self.our_dorm, write_file)
        write_file.close()

        with open("saved_step_2.pickle", "wb") as write_file:
            pickle.dump(self.our_dorm.get_room_list(), write_file)
        write_file.close()

    def kill_roach(self, number):
        self.our_dorm.get_room_by_number(number).kill_roach(False)

    def add_student(self, number):
        room = self.our_dorm.get_room_by_number(number)
        if room.get_number_of_students() == 2:
            return -1
        else:
            self.our_dorm.check_in(room)
