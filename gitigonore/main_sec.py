import pygame
import random
import game_object
pygame.init()

class Game:
    def __init__(self, w=700, h=500, fps=60):
        self.SIZE = (w, h)
        self.FPS = fps
        self.colors = {
            "background": (255,255,255),
            "game_object": (0,0,0)
        }
        self.sc = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
        self.balls = []
        for i in range(100):
            x = random.randint(100, self.SIZE[0] - 100)
            y = random.randint(100, self.SIZE[1] - 100)
            r = random.randint(5, 40)
            speed_x = random.randint(-10, 10)
            if speed_x == 0:
                speed_x = 1
            speed_y = random.randint(-10, 10)
            if speed_y == 0:
                speed_y = 1
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
            self.colors[i] = (R,G,B)
           # print(str(i) + str(":") + str(R) + str(", ") + str(G) + str(", ") + str(B))
            self.ball = game_object.Ball(x, y, r, speed_x, speed_y)
            self.balls.append(self.ball)
        self.platform = game_object.Platform(200, 400, 100, 50)
        self.score = 100
        self.is_going = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_going = False
            self.platform.process_events(event)

    def process_movement(self):
        for ball in self.balls:
            self.score = ball.process_movement(self.SIZE, self.platform.x, self.platform.y, self.platform.w, self.platform.h, self.score)
            print(self.score)
        self.platform.process_movement(self.SIZE)

    def process_drawings(self):
        self.sc.fill(self.colors["background"])
        index_of_ball = 0
        for ball in self.balls:
            ball.draw(self.sc, self.colors[index_of_ball])
            index_of_ball = index_of_ball + 1
        self.platform.draw(self.sc, self.colors["game_object"])

    def main_loop(self):
        while self.is_going:
            self.process_events()
            self.process_movement()
            self.process_drawings()
            pygame.display.flip()
            self.clock.tick(self.FPS)

def main():
    game = Game()
    game.main_loop()

if __name__ == "__main__":
    main()