import pygame
from game import Snake

class StartScreen:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Unfair Snake')
        self.win_x = 720
        self.win_y = 480
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.window = pygame.display.set_mode((self.win_x, self.win_y))
        self.font = pygame.font.SysFont('arial', 50)
        self.title = self.font.render('Unfair Snake', True, self.white)
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (self.win_x // 2, self.win_y // 2)
        self.start_text = self.font.render('Press SPACE to Start', True, self.white)
        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.center = (self.win_x // 2, self.win_y // 2 + 100)

    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                        game = Snake()
                        game.run()

            self.window.fill(self.black)
            self.window.blit(self.title, self.title_rect)
            self.window.blit(self.start_text, self.start_text_rect)
            pygame.display.update()

if __name__ == '__main__':
    start_screen = StartScreen()
    start_screen.show()
