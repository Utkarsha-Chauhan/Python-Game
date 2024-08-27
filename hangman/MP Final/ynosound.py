# importing all libs + button class 
import random
import pygame
import sys
from button import Button

# Initialize the game
pygame.init()

# setup the menu - set size and surface 'SCREEN'
size = (1280, 720)
SCREEN = pygame.display.set_mode((size))
Back_ground = pygame.image.load("Background.png")

#set caption names the window
pygame.display.set_caption("Menu")

#gets the font file for the menu screen
def get_font(size):  
    return pygame.font.Font("font.ttf", size)

#making the buttons functional
def options():
    while True:
        GRAY = (182, 168, 168)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(GRAY)

        OPTIONS_TEXT = get_font(45).render("List of options here->", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(200, 640), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# main menu function
        
def main_menu():
    while True:
        SCREEN.blit(Back_ground, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(wins, losses)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update() 
               
# initialising wins and looses here->resets them to zero whenever exiting
wins = 0
losses = 0

#play function
def play(wins, losses):
    WIDTH, HEIGHT = 1280, 700
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    font_size = 36
    font = pygame.font.Font(None, font_size)
    
    pygame.display.set_caption("Hangman Game")


    # colors-->
    GRAY = (182, 168, 168)
    BLACK = (0, 0, 0)
    GREEN = (52,138,45)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    font_inkfree_size = 40
    inkfree_font = pygame.font.SysFont("Inkfree", font_inkfree_size)

    # word list-->
    words = {
        "Fruits": ["apple", "banana", "cherry", "grape", "kiwi", "orange", "pear", "strawberry", "watermelon"],
        "Animals": ["cat", "dog", "elephant", "giraffe", "lion", "monkey", "penguin", "tiger", "zebra"],
        "Vegetables":["carrot", "broccoli", "potato", "spicach", "cucumber"],
        "Planets":["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune","pluto"],
        "Occupations": ["doctor", "teacher", "firefighter", "chef", "astronaut", "mechanic", "Engineer", "electrician","carpenter","astrologist",],
        "Colors":["red", "yellow", "blue" , "green","orange","violet","purple", "indigo", "black", "white", "brown","grey","lavender"] 
    }

    # chooses random word and hint from the defined word lists
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    hint = f"Hint: It belongs to {category.capitalize()}!!"

    # render the hangman image
    original_hangman_imgs = [pygame.image.load(f"hangman ({step}).png") for step in range(8)]
    hangman_imgs = [pygame.transform.scale(img, (500, 500)) for img in original_hangman_imgs]

    # render the lives image
    lives_img = [pygame.image.load(f"mini ({step}).png") for step in range(8)]
    hangman_step = 0

    # display the number of letters in the word
    correct_guesses = ["_"] * len(word)
    
    # defining a list to store all the used letters
    used_letters = []

    # flags
    win_count=False
    loss_count=False

    # main game loop-->
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #running = False
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE: 
                    main_menu()
                elif event.key == pygame.K_RETURN:  
                    play(wins, losses)
                    
                elif event.key >= 97 and event.key <= 122:
                    letter = chr(event.key)

                    # checks if the letter has already been used
                    if letter in used_letters: 
                        #ignore letters used
                        continue
                    # Add the letter to the used letters list
                    used_letters.append(letter)  
                    
                    # checking if the letter is correct
                    if letter in word:
                        for i, char in enumerate(word):
                            if char == letter:
                                correct_guesses[i] = letter
                    # draw hangman if wrong
                    else:
                        hangman_step += 1
                        
        # message shown when the game is won:-
        if "".join(correct_guesses) == word:
            message = ("You Win! \n"
                       "Press Enter to REPLAY \n"
                        "or \n"
                        "ESC to go back to the menu.\n")
            # display_text(window, message, (20, 300), font, BLUE)
            if not win_count:
                win_count = True  # Set flag to indicate win counted
                wins += 1  # Increment wins only if not already counted
            

        # message shown when the game is lost:-
        elif hangman_step == 7:
            message = ("You Lose! \n"+
                       (f"The word was: {word}. \n\n")+
                       "Press ENTER to replay or \n"
                       "ESC to go back to the menu.\n")
            if not loss_count:
                losses += 1  # Increment losses only if not already counted
                loss_count = True  # Set flag to indicate loss counted
            # display_text(window, message, (20,300), font, RED)

        # no message during the other actions:- 
        else:
            message = ""
        
        # font for the letter in the game
        font = pygame.font.SysFont("Inkfree",50)

        # display text function; generates text for all the letters
        def display_text(surface, message, pos, font, color):
            collection = [word.split(' ') for word in message.splitlines()]
            space = font.size(' ')[0]
            x,y = pos
            for lines in collection:
                for words in lines:
                    word_surface = font.render(words, True, color)
                    word_width , word_height = word_surface.get_size()
                    if x + word_width >= 700:
                        x = pos[10]
                        y += word_height
                    surface.blit(word_surface, (x,y))
                    x += word_width + space
                x = pos[0]
                y += word_height

        # filling the screen background
        window.fill(GRAY)
        
        #render hint, word, lives and the hangman image 

        text = font.render(hint, True, BLACK)
        window.blit(text, (20, 80))

        word_text = font.render(" ".join(correct_guesses), True, BLACK)
        window.blit(word_text, (80, 160))

        window.blit(hangman_imgs[hangman_step], (WIDTH - 550, 80))
        window.blit(lives_img[hangman_step], (WIDTH - 500, 10))

        #reads, color codes and displays the letter guessed so far
        for i, letter in enumerate(used_letters):
            # Use different colors for correct and incorrect guesses
            text_color = GREEN if letter in word else RED

            letter_text = inkfree_font.render(letter, True, text_color)
            window.blit(letter_text, (20 + i * (font_size + 10), 240))

        # Display wins count
        wins_text = font.render(f"Wins: {wins}", True, BLACK)
        window.blit(wins_text, (20, 550))

        # Display losses count
        losses_text = font.render(f"Losses: {losses}", True, BLACK)
        window.blit(losses_text, (20, 600))

        if message == ("You Win! \n"
                       "Press Enter to REPLAY \n"
                        "or \n"
                        "ESC to go back to the menu.\n"):
            display_text(window, message, (20,300), font, BLUE)
        else:
           display_text(window, message, (20,300), font, RED)

        pygame.display.update()
    pygame.quit()
main_menu()