import pygame  # Impordib pygame teegi
import random  # Impordib random teegi juhuslike arvude genereerimiseks
import time  # Impordib time teegi ajastamiseks

# Initsialiseerib pygame.
pygame.init()

# Määrab ekraani mõõtmed
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Liikuv ruut ja takistused")

# Määrab värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Mängija algpositsioon ja suurus
player_size = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_color = BLUE  # Mängija algne värv

# Takistuste list
obstacles = []
num_obstacles = 5  # Mitu takistust tekib

# Genereerib suvalistes kohtades takistused
for _ in range(num_obstacles):
    obs_x = random.randint(0, WIDTH - player_size)
    obs_y = random.randint(0, HEIGHT - player_size)
    obstacles.append((obs_x, obs_y))  # Lisab takistuse listi

# Viimase takistuste uuendamise aeg
last_obstacle_update = time.time()
obstacle_update_interval = 5  # Takistuste uuendamise intervall sekundites.

# Mängu tsükkel.
running = True
while running:
    pygame.time.delay(30)  # Määrab mängu kiiruse.

    for event in pygame.event.get():  # Kontrollib sündmusi.
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb akna, lõpetab mängu.
            running = False

    # Kasutaja klahvivajutused.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed  # Liigub vasakule
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed  # Liigub paremale
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed  # Liigub üles
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed  # Liigub alla

    # Kontrollib, kas mängija puutub takistust.
    for obs in obstacles:
        obs_x, obs_y = obs
        if (player_x < obs_x + player_size and player_x + player_size > obs_x and
                player_y < obs_y + player_size and player_y + player_size > obs_y):
            player_color = RED  # Kui puutub takistust, muutub punaseks
            running = False  # Lõpetab mängu

    # Takistuste uuendamine iga 5 sekundi järel
    if time.time() - last_obstacle_update > obstacle_update_interval:
        if obstacles:
            obstacles.pop(0)  # Eemaldab kõige vanema takistuse

        new_obs_x = random.randint(0, WIDTH - player_size)
        new_obs_y = random.randint(0, HEIGHT - player_size)
        obstacles.append((new_obs_x, new_obs_y))  # Lisab uue takistuse

        last_obstacle_update = time.time()  # Uuendab viimase uuendamise aja

    # Värskendab ekraani
    screen.fill(WHITE)  # Täidab tausta valgega
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))  # Joonistab mängija

    for obs in obstacles:  # Joonistab kõik takistused
        pygame.draw.rect(screen, BLACK, (obs[0], obs[1], player_size, player_size))

    pygame.display.update()  # Uuendab ekraani

pygame.quit()  # Lõpetab pygame'ime'i  # Lõpetab pygame'i