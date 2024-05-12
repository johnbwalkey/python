#from ChatGTP
# write pong game in python for two players using keyboard and
# option to control ball speed with score tracking sound effects and menu system
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font_large = pygame.font.Font(None, 80)
font_medium = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 36)

# Define game variables
ball_speed = 5
paddle_speed = 7
player1_score = 0
player2_score = 0

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to display the main menu
def show_menu():
    screen.fill(BLACK)
    draw_text("PONG", font_large, WHITE, WIDTH//2, HEIGHT//4)
    draw_text("Press SPACE to Play", font_medium, WHITE, WIDTH//2, HEIGHT//2)
    draw_text("Press Q to Quit", font_small, WHITE, WIDTH//2, HEIGHT*3//4)
    pygame.display.update()

# Function to draw paddles
def draw_paddles(paddle1_y, paddle2_y):
    pygame.draw.rect(screen, WHITE, (50, paddle1_y, 20, 100))
    pygame.draw.rect(screen, WHITE, (WIDTH-70, paddle2_y, 20, 100))

# Function to draw the ball
def draw_ball(ball_x, ball_y):
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

# Function to move paddles
def move_paddle(paddle_y, direction):
    if direction == "up":
        paddle_y -= paddle_speed
    elif direction == "down":
        paddle_y += paddle_speed
    # Ensure paddles stay within the screen
    if paddle_y < 0:
        paddle_y = 0
    elif paddle_y > HEIGHT - 100:
        paddle_y = HEIGHT - 100
    return paddle_y

# Function to reset ball position
def reset_ball():
    return WIDTH//2, HEIGHT//2

# Function to handle collisions with paddles
def paddle_collision(ball_x, ball_y, paddle1_y, paddle2_y):
    if ball_x < 70 and paddle1_y <= ball_y <= paddle1_y + 100:
        return True
    elif ball_x > WIDTH - 70 and paddle2_y <= ball_y <= paddle2_y + 100:
        return True
    return False

# Function to play sound effects
def play_sound(sound):
    pygame.mixer.Sound.play(sound)

# Load sound effects
paddle_hit_sound = pygame.mixer.Sound("paddle_hit.wav")
wall_hit_sound = pygame.mixer.Sound("wall_hit.wav")
score_sound = pygame.mixer.Sound("score.wav")

# Main game loop
def main():
    global ball_speed, player1_score, player2_score

    clock = pygame.time.Clock()
    ball_x, ball_y = reset_ball()
    paddle1_y = paddle2_y = HEIGHT//2 - 50
    ball_dx = ball_dy = 1

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Player 1 controls
        if keys[pygame.K_w]:
            paddle1_y = move_paddle(paddle1_y, "up")
        if keys[pygame.K_s]:
            paddle1_y = move_paddle(paddle1_y, "down")

        # Player 2 controls
        if keys[pygame.K_UP]:
            paddle2_y = move_paddle(paddle2_y, "up")
        if keys[pygame.K_DOWN]:
            paddle2_y = move_paddle(paddle2_y, "down")

        # Move the ball
        ball_x += ball_speed * ball_dx
        ball_y += ball_speed * ball_dy

        # Ball collision with top and bottom walls
        if ball_y <= 0 or ball_y >= HEIGHT:
            ball_dy *= -1
            play_sound(wall_hit_sound)

        # Ball collision with paddles
        if paddle_collision(ball_x, ball_y, paddle1_y, paddle2_y):
            ball_dx *= -1
            play_sound(paddle_hit_sound)

        # Ball out of bounds - score
        if ball_x <= 0:
            player2_score += 1
            play_sound(score_sound)
            ball_x, ball_y = reset_ball()
            ball_dx *= -1
        elif ball_x >= WIDTH:
            player1_score += 1
            play_sound(score_sound)
            ball_x, ball_y = reset_ball()
            ball_dx *= -1

        # Clear the screen
        screen.fill(BLACK)

        # Draw paddles and ball
        draw_paddles(paddle1_y, paddle2_y)
        draw_ball(ball_x, ball_y)

        # Draw scores
        draw_text(str(player1_score), font_medium, WHITE, WIDTH//4, 50)
        draw_text(str(player2_score), font_medium, WHITE, WIDTH*3//4, 50)

        # Update the display
        pygame.display.update()
        clock.tick(60)

# Main menu loop
show_menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main()
                show_menu()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

# Make sure to have three sound files named paddle_hit.wav, wall_hit.wav, and score.wav in the same directory as your Python script for the sound effects to work.
# You can adjust the game parameters like paddle speed, ball speed, and screen dimensions according to your preferences.