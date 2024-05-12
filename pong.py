import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game objects
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_RADIUS = 10

# Load sound effects
pygame.mixer.init()
paddle_sound = pygame.mixer.Sound("paddle_hit.wav")
wall_sound = pygame.mixer.Sound("wall_hit.wav")
score_sound = pygame.mixer.Sound("score.wav")

# Set up the game clock
clock = pygame.time.Clock()

# Define game functions
def draw_menu():
    window.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Press 'S' to Start", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.update()

def reset_game():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_speed_x, ball_speed_y, player1_score, player2_score
    paddle1_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    paddle2_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = WINDOW_WIDTH // 2
    ball_y = WINDOW_HEIGHT // 2
    ball_speed_x = random.choice([-5, 5])
    ball_speed_y = random.choice([-5, 5])
    player1_score = 0
    player2_score = 0

# Set initial game state
paddle1_x = 20
paddle2_x = WINDOW_WIDTH - 20 - PADDLE_WIDTH
paddle1_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5
player1_score = 0
player2_score = 0

# Game loop
running = True
in_menu = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                in_menu = False
                reset_game()

    if in_menu:
        draw_menu()
        continue

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 5
    if keys[pygame.K_s] and paddle1_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle1_y += 5
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 5
    if keys[pygame.K_DOWN] and paddle2_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle2_y += 5

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with walls
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - BALL_RADIUS:
        ball_speed_y = -ball_speed_y
        wall_sound.play()

    # Check for collisions with paddles
    if ball_x <= paddle1_x + PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_speed_x = -ball_speed_x
        paddle_sound.play()
    if ball_x >= paddle2_x - BALL_RADIUS and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_speed_x = -ball_speed_x
        paddle_sound.play()

    # Check for scoring
    if ball_x < 0:
        score_sound.play()
        player2_score += 1
        reset_game()
    if ball_x > WINDOW_WIDTH:
        score_sound.play()
        player1_score += 1
        reset_game()

    # Clear the window
    window.fill(BLACK)

    # Draw the paddles
    pygame.draw.rect(window, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Draw the scores
    font = pygame.font.Font(None, 36)
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    window.blit(player1_text, (WINDOW_WIDTH // 4, 10))
    window.blit(player2_text, (WINDOW_WIDTH // 4 * 3, 10))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
# This code creates a simple Pong game with two paddles controlled by the 'W' and 'S' keys for the left paddle,
# and the up and down arrow keys for the right paddle. The ball bounces off the paddles and the top and bottom walls. If the ball goes past the left or right edge of the window, the game will reset with the ball starting from the center.

# To control the ball speed, you can modify the initial values of ball_speed_x and ball_speed_y
# at the beginning of the script. Higher values will make the ball move faster, while lower values will make it move slower.