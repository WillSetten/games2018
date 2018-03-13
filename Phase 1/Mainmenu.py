
#Already in levels.py as it doesn't break anything
class Level_main_menu(Level):
    def __init__(self):
        super(Level_menu_main, self).__init__()

        self.create_gradient_background((0, 0, 0), (255, 255, 255))

        self.menu = Main_menu(self)
        self.list_draw.append(self.menu)
        self.list_update.append(self.menu)

#Main menu button
class Button_main_menu(Button):
    def __init__(self, level, scale, position, image_deselect, image_select):
        super(Button_main_menu, self).__init__(level, scale, position, image_deselect, image_select)

    def select(self):
        super(Button_main_menu, self).select()

    def clicked_action(self):
        super(Button_main_menu, self).clicked_action()

class Button_new_game(Button_main_menu):
    def __init__(self, level):
        scale = Vector(38*10, 7*10)
        position = Vector(50, 5*10)
        image_deselect = load_png("SET THE IMAGE")
        image_select = load_png("SET THE IMAGE")

class Menu_main(Menu):
    def __init__(self, level):
        super(Menu_main, self).__init__(level)

        self.button_new_game = Button_new_game(level)
        self.button_load_level = Button_load_level(level)
        self.button_info = Button_info(level)
        self.buttons = [self.button_new_game, self.button_load_level, self.button_info]

class Button_level_1(Button):
    def __init__(self, level):
        scale = Vector(48*10, 7*10)
        position = Vector(100, 10*10)
        image_deselect = load_png("SET THE IMAGE")
        image_select = load_png("SET THE IMAGE")

        super(Button_level_1, self).__init__(level, scale, position, image_deselect, image_select)

class Menu_level_loader(Menu):
    def __init__(self, level):
        super(Menu_level_loader, self).__init__()

        self.button_level_1 = Button_level_1(level)
        self.buttons = [self.button_level_1]


"""NOTE THAT THIS IS NOT FINISHED AND WILL REQUIRE IMPLEMENTATION WHEN THE REST IS FINISHED"""
