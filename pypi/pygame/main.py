import pygame
import random

pygame.init()

# Tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tamanho dos blocos
TAMANHO = 20

# Cobra
cobra = [(100, 100), (80, 100), (60, 100)]
direcao = (TAMANHO, 0)

# Comida
comida = (
    random.randrange(0, LARGURA, TAMANHO),
    random.randrange(0, ALTURA, TAMANHO)
)

clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)

rodando = True

while rodando:

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_UP and direcao != (0, TAMANHO):
                direcao = (0, -TAMANHO)

            if evento.key == pygame.K_DOWN and direcao != (0, -TAMANHO):
                direcao = (0, TAMANHO)

            if evento.key == pygame.K_LEFT and direcao != (TAMANHO, 0):
                direcao = (-TAMANHO, 0)

            if evento.key == pygame.K_RIGHT and direcao != (-TAMANHO, 0):
                direcao = (TAMANHO, 0)

    # Nova posição da cabeça
    nova_cabeca = (
        cobra[0][0] + direcao[0],
        cobra[0][1] + direcao[1]
    )

    cobra.insert(0, nova_cabeca)

    # Comeu a comida
    if cobra[0] == comida:
        comida = (
            random.randrange(0, LARGURA, TAMANHO),
            random.randrange(0, ALTURA, TAMANHO)
        )
    else:
        cobra.pop()

    # Verificar colisão
    if (
        cobra[0][0] < 0 or
        cobra[0][0] >= LARGURA or
        cobra[0][1] < 0 or
        cobra[0][1] >= ALTURA or
        cobra[0] in cobra[1:]
    ):
        rodando = False

    # Desenhar
    tela.fill(PRETO)

    # Desenhar cobra
    for parte in cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            (parte[0], parte[1], TAMANHO, TAMANHO)
        )

    # Desenhar comida
    pygame.draw.rect(
        tela,
        VERMELHO,
        (comida[0], comida[1], TAMANHO, TAMANHO)
    )

    # Pontuação
    pontos = len(cobra) - 3
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))

    pygame.display.update()

    clock.tick(10)

pygame.quit()