import pygame
import sys

SQRT_3 = 1.732
SQRT_2 = 1.414
SC_WIDTH, SC_HEIGHT = 1280, 720
FPS = 30
BG_COLOR = "red"
running = True

def check_colision(obj):
    if obj.collRect.collidepoint(pygame.mouse.get_pos()):
        return True
    else:
        return False

class Triangle:
    def __init__(self, screen, radius, x, y) -> None:
        self.screen = screen
        self.radius = radius
        self.x = x
        self.y = y
        self.taken = False
        self.sideRect = 2 * radius / SQRT_2

    def update(self):
        if self.taken:
            self.x, self.y = pygame.mouse.get_pos()

        self.collRect = pygame.Rect(
            self.x - self.sideRect / 2,
            self.y - self.sideRect / 2,
            self.sideRect,
            self.sideRect,
        )
        #pygame.draw.rect(self.screen, 'black', self.collRect)

    def draw(self):
        fp = (self.x, self.y - self.radius)
        sp = (self.x - self.radius * SQRT_3 / 2, self.y + self.radius / 2)
        tp = (self.x + self.radius * SQRT_3 / 2, self.y + self.radius / 2)
        pygame.draw.polygon(self.screen, "black", [fp, sp, tp], 5)

    def get_taken(self):
        self.taken = True

    def get_free(self):
        self.taken = False
class Circle(Triangle):
    def draw(self):
        pygame.draw.circle(self.screen, 'black', (self.x, self.y), self.radius, 5)
class Square(Triangle):
    def draw(self):
        pygame.draw.rect(self.screen, 'black', self.collRect, 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    triangle = Triangle(screen, 100, 200, 200)
    circle = Circle(screen, 100, 500, 500)
    square = Square(screen, 100, 800, 600)

    shapes_list = [triangle, circle, square]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_just_pressed()[pygame.K_q]:
                pygame.quit()
                sys.exit()

            for obj in shapes_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and check_colision(obj):
                        print(1)
                        obj.get_taken()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == pygame.BUTTON_LEFT and obj.taken:
                        print(2)
                        obj.get_free()

        screen.fill("red")
        for obj in shapes_list:
            obj.update()
            obj.draw()

        pygame.display.flip()
        clock.tick(60)


main()
