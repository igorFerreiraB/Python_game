import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Beba e coma')
player_image = pygame.image.load('img/Original3.png')
original_player_rect = player_image.get_rect()

# Defina a escala desejada para o jogador
escala_jogador = 2
player_image = pygame.transform.scale(player_image, (int(original_player_rect.width * escala_jogador), int(original_player_rect.height * escala_jogador)))
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# Carregar a imagem dos pontos (substitua 'ponto.png' pelo caminho correto)
point_image = pygame.image.load('img/Original3.png')
original_point_rect = point_image.get_rect()

# Defina a escala desejada para os pontos
escala_ponto = 0.5
point_image = pygame.transform.scale(point_image, (int(original_point_rect.width * escala_ponto), int(original_point_rect.height * escala_ponto)))

# Propriedades dos pontos
num_points = 20
point_width, point_height = point_image.get_width(), point_image.get_height()
points = [pygame.Rect(random.randint(0, width - point_width), random.randint(0, height - point_height), point_width, point_height) for _ in range(num_points)]

score = 0

# Fonte para o contador
font = pygame.font.Font(None, 36)

# Função para gerar um novo ponto
def spawn_point():
    return random.randint(0, width), random.randint(0, height)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left - player_rect.width > 0:
        player_rect.x -= 10
    if keys[pygame.K_RIGHT] and player_rect.right + player_rect.width < width:
        player_rect.x += 10
    if keys[pygame.K_UP] and player_rect.top - player_rect.height > 0:
        player_rect.y -= 10
    if keys[pygame.K_DOWN] and player_rect.bottom + player_rect.height < height:
        player_rect.y += 10

    # Verificar colisão com os pontos menores
    for point_rect in points[:]:
        if player_rect.colliderect(point_rect):
            points.remove(point_rect)
            score += 1
            print(f'Pontos coletados: {score}')
            # Spawnar um novo ponto
            points.append(spawn_point())

    # Limpar a tela
    screen.fill((255, 255, 255))

    for point in points:
        screen.blit(point_image, point)

    # Desenhar o jogador (imagem)
    screen.blit(player_image, player_rect.topleft)

    # Exibir o contador na tela
    text = font.render(f'score: {score}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização
    pygame.time.Clock().tick(30)

