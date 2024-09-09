class Gamer:
    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_number(self, num):
        self.__number = num

    def get_number(self):
        return self.__number

    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__number = 0
