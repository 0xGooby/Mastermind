import pygame, random, sys
from scripts.ball import Ball
from scripts.button import Button
from scripts.game_help import Help

pygame.init()
pygame.display.set_caption("Mastermind")
screen = pygame.display.set_mode((600, 900))
clock = pygame.time.Clock()
bg_surface = pygame.transform.scale(pygame.image.load('assets/bg/bg.png'), (600, 900))

BALL_RADIUS = 20
BOARD_WIDTH = 320
BOARD_HEIGHT = 720
BOX_WIDTH = 80
BOX_HEIGHT = 90
BLACK = (0, 0, 0)

list_of_colors = ["Grey", "Blue", "Orange", "Red", "Green", "Purple"]

guesses = []

pc_answer = []
for i in range(4):
    random_color = random.choice(list_of_colors)
    pc_answer.append(random_color)

pcball_1 = Ball((BOX_WIDTH + 20, 70), BALL_RADIUS, pc_answer[0])
pcball_2 = Ball(((BOX_WIDTH * 2) + 20, 70), BALL_RADIUS, pc_answer[1])
pcball_3 = Ball(((BOX_WIDTH * 3) + 20, 70), BALL_RADIUS, pc_answer[2])
pcball_4 = Ball(((BOX_WIDTH * 4) + 20, 70), BALL_RADIUS, pc_answer[3])

red_button = Button(50, "Red")
green_button = Button(100, "Green")
blue_button = Button(150, "Blue")
orange_button = Button(200, "Orange")
purple_button = Button(250, "Purple")
black_button = Button(300, "Grey")

# perfect_guess = Help(350, "Green")
# misplaced_guess = Help(380, "Red")

buttons = [red_button, green_button, blue_button, orange_button, purple_button, black_button]
pc_balls = [pcball_1, pcball_2, pcball_3, pcball_4]

ball_x = BOX_WIDTH + 20
ball_y = 715
perfect_count = 0
misplaced_count = 0
count = -1

def draw_grid():
    for i in range(4):
        for j in range(8):
            box = pygame.Rect(i*BOX_WIDTH + 60, j*BOX_HEIGHT + 40, BOX_WIDTH, BOX_HEIGHT)
            pygame.draw.rect(screen, BLACK, box, 1)

def find_answer(color, x, y):

    global perfect_count, misplaced_count

    pc_answer_copy = pc_answer[:]

    ball = Ball([x, y], BALL_RADIUS, color)
    x += 80
    guesses.append(ball)

    if len(guesses) % 4 == 0:

        guesses_copy = guesses[-4:]

        for i in range(4):
            if guesses_copy[i].color == pc_balls[i].color and guesses_copy[i].center[0] == pc_balls[i].center[0]:
                perfect_count += 1
                pc_answer_copy.remove(guesses_copy[i].color)

        for i in range(4):
            if guesses_copy[i].color in pc_answer_copy and guesses_copy[i].color != pc_answer[i]:
                misplaced_count += 1
                pc_answer_copy.remove(guesses_copy[i].color)    

while True:

    screen.blit(bg_surface, (0, 0))
    pygame.draw.rect(bg_surface, (255,255,255), (60, 40, BOARD_WIDTH, BOARD_HEIGHT))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and len(guesses) < 32:  
            if red_button.rect.collidepoint(event.pos):
                find_answer("Red", ball_x, ball_y)
                ball_x += 80
                if len(guesses) % 4 == 0:
                    ball_x = BOX_WIDTH + 20
                    ball_y -= 90
            if green_button.rect.collidepoint(event.pos):
                find_answer("Green", ball_x, ball_y)
                ball_x += 80
                if len(guesses) % 4 == 0:
                    ball_x = BOX_WIDTH + 20
                    ball_y -= 90
            if blue_button.rect.collidepoint(event.pos):
                find_answer("Blue", ball_x, ball_y)
                ball_x += 80
                if len(guesses) % 4 == 0:
                    ball_x = BOX_WIDTH + 20
                    ball_y -= 90
            if orange_button.rect.collidepoint(event.pos):
                find_answer("Orange", ball_x, ball_y)
                ball_x += 80
                if len(guesses) % 4 == 0:
                    ball_x = BOX_WIDTH + 20
                    ball_y -= 90
            if purple_button.rect.collidepoint(event.pos):
                find_answer("Purple", ball_x, ball_y)
                ball_x += 80
                if len(guesses) % 4 == 0:
                    ball_x = BOX_WIDTH + 20
                    ball_y -= 90
            if black_button.rect.collidepoint(event.pos):
                find_answer("Grey", ball_x, ball_y)
                ball_x += 80
                if len(guesses) % 4 == 0:
                    ball_x = BOX_WIDTH + 20
                    ball_y -= 90

            if len(guesses) % 4 == 0:
                print(f"Perfect guesses: {perfect_count}")
                print(f"Wrong spot guesses: {misplaced_count}")
                if perfect_count == 4:
                    print("You won!")
                else:
                    perfect_count = 0
                    misplaced_count = 0
        # if len(guesses) == 28 and perfect_count != 4:
        #     print("You lost")     

    for guess in guesses:
        guess.draw(screen)

    draw_grid()

    if perfect_count == 4 or len(guesses) >= 32:
        for ball in pc_balls:
            ball.draw(screen) 

    for button in buttons:
        button.draw(screen)

    pygame.display.update()
    clock.tick(60)