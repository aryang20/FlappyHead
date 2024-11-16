import main


class Pipe:
    def __init__(self, speed=5):
        self.speed = speed
        self.x = main.screenWidth
    def move(self):
        self.x -= self.speed
    def draw(self):
        pass