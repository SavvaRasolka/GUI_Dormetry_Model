class Controller:
    def __init__(self, model):
        self.model = model

    #def show_dorm(self):
     #   self.model.update()
      #  if self.model.our_dorm.get_month() == 4:
            #self.view.show_popup("Осторожно! В следующем месяце сессия")
       # self.view.show_dorm(self.model.our_dorm.get_room_list(), self.model.our_dorm.calculate_level_of_happiness(),
        #                    self.model.our_dorm.get_month(), self.model.our_dorm.define_is_kitchen_okey())

    def save(self):
        self.model.save_to_file()

    def kill_roach(self, room):
        self.model.kill_roach(room)
        #self.view.show_dorm(self.model.our_dorm.get_room_list(), self.model.our_dorm.calculate_level_of_happiness(),
         #                   self.model.our_dorm.get_month(), self.model.our_dorm.define_is_kitchen_okey())

    def add_student(self, room):
        if not self.model.add_student(room):
            #self.view.show_popup('В комнате нет места')
            return False
        else:
            return True
