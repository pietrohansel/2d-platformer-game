import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = pygame.image.load(
            'graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load(
            'graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            'graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type):
        super().__init__()

        if obstacle_type == 'fly':
            fly_1 = pygame.image.load('graphics/Fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load(
                'graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load(
                'graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()


def display_score(font, surface, start):
    current_time = int(pygame.time.get_ticks() / 1000) - start
    score_surf = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    surface.blit(score_surf, score_rect)
    return current_time


def collision_sprite(player, obstacles):
    if pygame.sprite.spritecollide(player, obstacles, False):
        return False
    return True


# --- Initialization ---
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Titulo do jogo')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

bg_music = pygame.mixer.Sound('audio/music.wav')

# Groups
player = pygame.sprite.GroupSingle()
player_sprite = Player()
player.add(player_sprite)

obstacle_group = pygame.sprite.Group()

# Background surfaces
sky_surface = pygame.image.load('graphics/sky.png').convert()
sky_surface2 = pygame.image.load('graphics/sky2.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Sky scrolling
sky_x = 0
sky2_x = 0
sky_scroll_speed = 0.5
sky2_scroll_speed = 0.25

# Intro screen surfaces
player_stand = pygame.image.load(
    'graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = font.render('Nome do Jogo', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = font.render('Aperte space para comecar', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# --- Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(
                    Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                bg_music.play(loops=-1)

    if game_active:
        # Draw background with parallax scrolling
        sky_x -= sky_scroll_speed
        sky2_x -= sky2_scroll_speed

        # Draw sky surfaces (loop them for seamless scrolling)
        screen.blit(sky_surface, (sky_x, 0))
        screen.blit(sky_surface, (sky_x + sky_surface.get_width(), 0))
        if sky_x <= -sky_surface.get_width():
            sky_x = 0

        screen.blit(sky_surface2, (sky2_x, 0))
        screen.blit(sky_surface2, (sky2_x + sky_surface2.get_width(), 0))
        if sky2_x <= -sky_surface2.get_width():
            sky2_x = 0

        screen.blit(ground_surface, (0, 300))

        # Score
        score = display_score(font, screen, start_time)

        # Player
        player.draw(screen)
        player.update()

        # Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collision
        if not collision_sprite(player_sprite, obstacle_group):
            game_active = False
            bg_music.stop()
    else:
        # Intro / Game Over screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        # Reset player and obstacles
        player_sprite.rect.midbottom = (80, 300)
        player_sprite.gravity = 0
        obstacle_group.empty()

        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            score_message = font.render(
                f'Your Score: {score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 330))
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
