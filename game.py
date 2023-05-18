import pygame
import random
import time

class Snake:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Unfair Snake')
        self.font = pygame.font.Font('font2.ttf', 20)
        self.win_x = 720
        self.win_y = 480
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.window = pygame.display.set_mode((self.win_x, self.win_y))
        self.fps = pygame.time.Clock()
        self.init_pos = [100, 50]
        self.body = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
        ]
        self.fruit_position = [random.randrange(1, (self.win_x // 10)) * 10,
                                random.randrange(1, (self.win_y // 10)) * 10]
        self.fruit_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.lives = 3

    def score_display(self, choice, color, font, size):
        self.font = pygame.font.Font('font2.ttf', 20)
        score_surface = self.font.render(f'Score: {str(self.score)}    Lives: {str(self.lives)}', True, color)
        score_rect = score_surface.get_rect()
        score_rect.bottomleft = (10, self.win_y - 10)
        self.window.blit(score_surface, score_rect)

    def game_end(self):
        self.lives -= 1
        if self.lives == 0:
            self.font = pygame.font.Font('font2.ttf', 40)
            game_over_surface = self.font.render(f'score total: {str(self.score)}', True, self.white)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (self.win_x / 2, self.win_y / 4)
            self.window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()

            time.sleep(2)
            pygame.quit()
            quit()
        else:
            self.init_pos = [100, 50]
            self.body = [
                [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
            self.direction = 'RIGHT'
            self.change_to = self.direction
            self.fruit_position = [random.randrange(1, (self.win_x // 10)) * 10,
                                    random.randrange(1, (self.win_y // 10)) * 10]
            self.fruit_spawn = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        self.change_to = 'RIGHT'

            if self.change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'

            if self.direction == 'UP':
                self.init_pos[1] -= 10
            if self.direction == 'DOWN':
                self.init_pos[1] += 10
            if self.direction == 'LEFT':
                self.init_pos[0] -= 10
            if self.direction == 'RIGHT':
                self.init_pos[0] += 10

            self.body.insert(0, list(self.init_pos))
            if self.init_pos[0] == self.fruit_position[0] and self.init_pos[1] == self.fruit_position[1]:
                self.score += 10
                self.fruit_spawn = False
            else:
                self.body.pop()
            if not self.fruit_spawn:
                self.fruit_position = [random.randrange(1, (self.win_x // 10)) * 10,
                                        random.randrange(1, (self.win_y // 10)) * 10]

            self.fruit_spawn = True
            self.window.fill(self.black)

            for pos in self.body:
                pygame.draw.rect(self.window, self.white, pygame.Rect(
                    pos[0], pos[1], 10, 10))

            pygame.draw.rect(self.window, self.white, pygame.Rect(
                self.fruit_position[0], self.fruit_position[1], 10, 10))

            if self.init_pos[0] < 0 or self.init_pos[0] > self.win_x - 10:
                self.game_end()
            if self.init_pos[1] < 0 or self.init_pos[1] > self.win_y - 10:
                self.game_end()

            for block in self.body[1:]:
                if self.init_pos[0] == block[0] and self.init_pos[1] == block[1]:
                    self.game_end()

            self.score_display(1, self.white, 'arial', 20)
            pygame.display.update()
            self.fps.tick(60)