import pygame
from settings import Settings


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()