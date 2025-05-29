import pygame

# Initialize pygame
pygame.init()

# Screen
width = 800
height = 600

screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Mountain Shooter")

running = True

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close the window
            quit()  # Close the program
            running = False  # Stop the loop
