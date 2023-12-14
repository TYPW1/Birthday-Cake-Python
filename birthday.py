import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Birthday Candle App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
cake_image = pygame.image.load('cake.png')
candle_image = pygame.image.load('candle.png')

# Function to draw text
def draw_text(surface, text, position, size=30):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, BLACK)
    surface.blit(text_surface, position)

# Function to draw candles
def draw_candles(surface, num_candles):
    candle_width = candle_image.get_width()
    cake_width = cake_image.get_width()
    spacing = (cake_width - candle_width * num_candles) // (num_candles + 1)
    candle_x = spacing
    for _ in range(num_candles):
        surface.blit(candle_image, (candle_x, 100))  # Adjust 100 to the y-position of the cake
        candle_x += candle_width + spacing

# Main application loop
running = True
age_input = ""
age = 0
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Process the input age
                try:
                    age = int(age_input)
                    print("Age entered:", age)
                except ValueError:
                    print("Invalid age entered")
                age_input = ""  # Reset age input
            elif event.key == pygame.K_BACKSPACE:
                age_input = age_input[:-1]
            else:
                age_input += event.unicode

    # Display instructions, input, cake, and candles
    draw_text(screen, "Enter your age and press Enter:", (50, 50))
    draw_text(screen, age_input, (50, 100))
    screen.blit(cake_image, (100, 200))  # Adjust (100, 200) as needed
    if age > 0:
        draw_candles(screen, age)

    pygame.display.flip()

pygame.quit()
