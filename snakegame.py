import pygame, sys, random
#Snake Game
# Initialize pygame
pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 500))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create a clock to control the game's framerate
clock = pygame.time.Clock()

# Define the snake's starting position and size
snake_x = 250
snake_y = 250
snake_size = 10

# Define the initial velocity of the snake
velocity_x = 0
velocity_y = 0

# Define the size of the food block
food_size = 10

# Generate the initial position of the food block
food_x = random.randint(0, 490)
food_y = random.randint(0, 490)

# Define a function to draw the snake
def draw_snake(x, y, size):
    pygame.draw.rect(screen, white, [x, y, size, size])

# Define a function to draw the food block
def draw_food(x, y, size):
    pygame.draw.rect(screen, red, [x, y, size, size])

# Start the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Check for arrow key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x = -10
        velocity_y = 0
    if keys[pygame.K_RIGHT]:
        velocity_x = 10
        velocity_y = 0
    if keys[pygame.K_UP]:
        velocity_y = -10
        velocity_x = 0
    if keys[pygame.K_DOWN]:
        velocity_y = 10
        velocity_x = 0

    # Update the snake's position based on its velocity
    snake_x += velocity_x
    snake_y += velocity_y

    # Fill the screen with black
    screen.fill(black)

    # Draw the snake
    draw_snake(snake_x, snake_y, snake_size)

    # Draw the food block
    draw_food(food_x, food_y, food_size)

    # Check if the snake has collided with the food block
    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        # Generate a new food block in a random location
        food_x = random.randint(0, 490)
        food_y = random.randint(0, 490)

    # Update the screen
    pygame.display.update()

    # Limit the game to 20 frames per second
    clock.tick(20)

# Quit pygame
pygame.quit()
