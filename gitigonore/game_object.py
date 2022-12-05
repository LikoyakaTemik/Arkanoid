import pygame
class Ball:
    def __init__(self, x, y, r, speed_x, speed_y):
        self.x = x
        self.y = y
        self.r = r
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.weight = 0
        if r < 20:
            self.weight = 10
        elif r > 20:
            self.weight = 20
    def process_movement(self, SIZE, x_p, y_p, w_p, h_p, score):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x - self.r <= 0 or self.x + self.r >= SIZE[0]:
            self.speed_x = -self.speed_x
        if self.y - self.r <= 0:
            self.speed_y = -self.speed_y
        if self.y + self.r >= SIZE[1]:
            score = score - 1
        if self.x >= x_p and self.x <= x_p + w_p and self.y < y_p and self.x + self.r >= x_p and self.x - self.r <= x_p + w_p and self.y + self.r >= y_p and self.y + self.r <= y_p + h_p / 2:
            self.speed_y = -self.speed_y
        if self.x >= x_p and self.x <= x_p + w_p and self.y > y_p and self.x + self.r >= x_p and self.x - self.r <= x_p + w_p and self.y + self.r <= y_p + h_p and self.y + self.r >= y_p + h_p / 2:
            self.speed_y = -self.speed_y
        return score
    def draw(self, sc, COLOR):
        pygame.draw.circle(sc, COLOR, (self.x, self.y), self.r)


class Platform:
    def __init__(self, x, y ,w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.left = False
        self.right = False

    def process_movement(self, SIZE):
        if self.left and self.x + self.w <= SIZE[0]:
            self.x += 5
        if self.right and self.x >= 0:
            self.x -= 5

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.left = True
            if event.key == pygame.K_a:
                self.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.left = False
            if event.key == pygame.K_a:
                self.right = False

    def draw(self, sc, COLOR):
        pygame.draw.rect(sc, COLOR, (self.x, self.y, self.w, self.h))

