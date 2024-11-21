import pygame
import sys

SQRT_3 = 1.732
SC_WIDTH, SC_HEIGHT = 640, 480
FPS = 30
running = True


class Triangle:
    def __init__(self, screen, radius, x, y) -> None:
        self.screen = screen
        self.radius = radius
        self.x = x
        self.y = y
        self.taken = False

    def update(self):
        if self.taken:
            self.x, self.y = pygame.mouse.get_pos()
        fp = (self.x, self.y - self.radius)
        sp = (self.x - self.radius * SQRT_3 / 2, self.y + self.radius / 2)
        tp = (self.x + self.radius * SQRT_3 / 2, self.y + self.radius / 2)
        pygame.draw.polygon(self.screen, "black", [fp, sp, tp], 5)

    def get_taken(self):
        self.taken = True
    
    def get_free(self):
        self.taken = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
    clock = pygame.time.Clock()
    triangle = Triangle(screen, 150, 200, 200)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_just_pressed()[pygame.K_q]:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    print(1)
                    triangle.get_taken()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT and triangle.taken:
                    print(2)
                    triangle.get_free()

        screen.fill("red")
        triangle.update()

        pygame.display.flip()
        clock.tick(60)


main()
