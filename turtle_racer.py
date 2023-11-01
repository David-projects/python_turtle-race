import random


class TurtleRacer:
    import random
    def __init__(self, racer, colour):
        self.racer = racer
        self.colour = colour
        self.racer.color(colour)
        self.place = -250

    def penup(self):
        self.racer.penup()

    def goto_start(self, x, y):
        self.racer.goto(x, y)

    def start_race(self):
        self.racer.speed(random.choice([1,2,3,4,5,6,7,8,9,10]))
        f = random.randint(1,10)
        self.place += f
        self.racer.forward(f)
        if self.place >= 200:
            return True
        return False

    def get_colour(self):
        return self.colour

