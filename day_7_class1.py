class Animal():
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers Body"
    def get_colo(self):
        return self.color
    def make_noise(self):
        return self.noise


class Dog(Animal):
    name = "Jon"
    #color = "brown"
    #def get_color(self):
    #    return self.color
