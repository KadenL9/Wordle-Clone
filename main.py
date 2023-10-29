# import necessary modules
import pygame
import sys
import random

# initialize pygame modules
pygame.init()


# function that allows dynamics of size of courier new font size
# takes the variable size that represents the font size that is returned
def font(size):
    return pygame.font.SysFont("couriernew", size)


# initialize window
width = 600
height = 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wordle")

# define buttons as global variables
# play button on home page
p_rect = pygame.Rect(175, 250, 250, 50)
# how to play button on home page
htp_rect = pygame.Rect(175, 400, 250, 50)
# quit button on home page
q_rect = pygame.Rect(175, 550, 250, 50)
# back to home button on instructions page
b_rect = pygame.Rect(175, 725, 250, 50)
# play again button on play page
pa_rect = pygame.Rect(248, 135, 100, 25)


# function that draws home screen of game - contains 3 buttons: PLAY, HOW TO PlAY, QUIT
def home():
    # clear the screen
    window.fill((0, 0, 0))

    # wordle title
    wordle = font(50).render("WORDLE", True, (255, 255, 255))
    window.blit(wordle, (210, 100))

    # play button
    pygame.draw.rect(window, (0, 128, 0), p_rect, 2)
    play_button = font(45).render("Play", True, (255, 196, 37))
    window.blit(play_button, (245, 247))

    # how to play button
    pygame.draw.rect(window, (0, 128, 0), htp_rect, 2)
    how_to_play = font(35).render("How to Play", True, (255, 196, 37))
    window.blit(how_to_play, (185, 404))

    # quit button
    pygame.draw.rect(window, (0, 128, 0), q_rect, 2)
    q = font(45).render("Quit", True, (255, 196, 37))
    window.blit(q, (245, 550))

    pygame.display.update()


# function that displays instructions on how to play
def show_instructions():
    # clear the screen
    window.fill((0, 0, 0))

    # display the title "HOW TO PLAY"
    htp_title = font(45).render("HOW TO PLAY", True, (90, 102, 255))
    window.blit(htp_title, (150, 50))

    # display the how to play
    text1 = font(20).render("Guess the WORDLE in six tries", True, (255, 255, 255))
    window.blit(text1, (20, 150))

    text2 = font(20).render("Each guess must be a valid five-letter word.", True, (255, 255, 255))
    window.blit(text2, (20, 225))
    text3 = font(20).render("Hit the enter button to submit.", True, (255, 255, 255))
    window.blit(text3, (20, 250))

    text4 = font(20).render("After each guess, the color of the tiles will", True, (255, 255, 255))
    window.blit(text4, (20, 325))
    text5 = font(20).render("change to show how cloose your guess was to", True, (255, 255, 255))
    window.blit(text5, (20, 350))
    text6 = font(20).render("the text", True, (255, 255, 255))
    window.blit(text6, (20, 375))

    text7 = font(20).render("GREEN means that the letter is in the word and", True, (1, 154, 1))
    window.blit(text7, (20, 450))
    text8 = font(20).render("in the correct spot", True, (1, 154, 1))
    window.blit(text8, (20, 475))

    text9 = font(20).render("YELLOW means that the letter is in the word but", True, (255, 196, 37))
    window.blit(text9, (20, 550))
    text10 = font(20).render("in the wrong spot", True, (255, 196, 37))
    window.blit(text10, (20, 575))

    text11 = font(20).render("DARK GRAY means that the letter is not in the", True, (76, 76, 76))
    window.blit(text11, (20, 650))
    text12 = font(20).render("word in any spot", True, (76, 76, 76))
    window.blit(text12, (20, 675))

    # back button that allows user to go back to homepage
    b = font(30).render("Back to Home", True, (255, 196, 37))
    window.blit(b, (192, 732))
    pygame.draw.rect(window, (0, 128, 0), b_rect, 2)

    pygame.display.update()


# function that draws gray square given x and y coordinates
# x = x-coordinate, y = y-coordinate, w = width, h = height, b = border width, c = corner radius
def draw_rect(x, y, w, h, b, c):
    square = pygame.Rect(x, y, w, h)
    pygame.draw.rect(window, (100, 100, 100), square, b, c)


# lists that contain letters on screen keyboard
row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
row3 = ["Z", "X", "C", "V", "B", "N", "M"]


# functions that displays letters on screen keyboard
def draw_letters():
    # letters in first row (QWERTYUIOP)
    for letter in range(len(row1)):
        character = font(20).render(row1[letter], True, (255, 255, 255))
        window.blit(character, (91 + (45 * letter), 588))

    # letters in second row (ASDFGHJKL)
    for letter in range(len(row2)):
        character = font(20).render(row2[letter], True, (255, 255, 255))
        window.blit(character, (114 + (45 * letter), 643))

    # letters in third row (ZXCVBNM)
    for letter in range(len(row3)):
        character = font(20).render(row3[letter], True, (255, 255, 255))
        window.blit(character, (159 + (45 * letter), 698))

    # enter key and delete key (ENT, DEL)
    enter_key = font(20).render("ENT", True, (255, 255, 255))
    window.blit(enter_key, (91, 698))
    delete_key = font(20).render("DEL", True, (255, 255, 255))
    window.blit(delete_key, (473, 698))

    pygame.display.update()


# function that draws the wordle grid
def draw_grid():
    # draw black square to cover grid
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, 170, 600, 335))

    # loop that draw gray squares that surrounds the inputted letters
    startx, starty = (165, 175)
    for row in range(6):
        for letter in range(5):
            draw_rect(startx + (55 * letter), starty + (55 * row), 50, 50, 3, 0)


# function that displays the play screen
def play():
    # clear the screen
    window.fill((0, 0, 0))

    # wordle title
    wordle = font(60).render("WORDLE", True, (255, 255, 255))
    window.blit(wordle, (195, 60))

    draw_grid()

    # first row of screen keyboard that contains 10 letters (QWERTYUIOP)
    for letter in range(10):
        draw_rect(77 + (45 * letter), 575, 40, 50, 0, 7)

    # second row of screen keyboard that contains 9 letters (ASDFGHJKL)
    for letter in range(9):
        draw_rect(100 + (45 * letter), 630, 40, 50, 0, 7)

    # third row of screen keyboard that contains 2 non-letters (ENTER, DELETE) and 7 letters (ZXCVBNM)
    draw_rect(77, 685, 63, 50, 0, 7)
    for letter in range(7):
        draw_rect(145 + (45 * letter), 685, 40, 50, 0, 7)
    draw_rect(460, 685, 62, 50, 0, 7)

    # display letters on keyboard
    draw_letters()

    pygame.display.update()


# variable that is defined by the page that the user is on to determine when to check for events
# pages = "home", "instructions", "game"
page = "home"

# variable that allows or denies letter to be added
finished_word = False

# variable that defines chance user is on
chance = 0

# variable that defines whether the user has solved the word
solved = False

# generate random word that doesn't have 2 of the same letters
while True:
    rand_number = random.randint(0, 5756)
    with open("word-list.txt") as file:
        correct_word = file.readlines()[rand_number].rstrip()

    with open("possible-words.txt") as file2:
        possible_words = file2.readlines()
        new_list = [possible_word.rstrip() for possible_word in possible_words]

        if correct_word not in new_list:
            continue

    # remove 2 letter words
    counts = {}
    two_letter_word = False
    for letter in correct_word:
        if letter in counts.keys():
            two_letter_word = True
            break
        else:
            counts[letter] = 1

    if not two_letter_word:
        break

# function to check if any of the 3 home buttons are pressed + action
# takes a variable p that represents the position of the mouse pointer at the click
def check_button_pressed(p):
    global page

    if p_rect.collidepoint(p[0], p[1]):
        page = "game"
        play()
    elif htp_rect.collidepoint(p[0], p[1]):
        page = "instructions"
        show_instructions()
    elif q_rect.collidepoint(p[0], p[1]):
        sys.exit()
    else:
        return


# array that represents each box on the wordle grid
grid = []
for row in range(6):
    r = []
    for column in range(5):
        r.append("")
    grid.append(r)


# function that checks if a key pressed is valid; key = key that is pressed and checked
def check_key(key):
    # function that takes a list as input and returns the list in lowercase form; l represents lowercase
    def lowerlist(l):
        return list(map(lambda x: x.lower(), l))

    # check if key pressed is a valid key in the game
    if key in lowerlist(row1):
        return True
    elif key in lowerlist(row2):
        return True
    elif key in lowerlist(row3):
        return True
    else:
        return False


# function that displays letter on grid once pressed; letter = letter to be added to grid
def add_letter(letter):
    global grid, finished_word, chance

    if finished_word:
        return

    # loop that finds when next available letter there in given row
    for a in range(5):
        if grid[chance][a] == "":
            grid[chance][a] = letter

            # word becomes finished if letter is inputted in grid at 5 spot
            if a == 4:
                finished_word = True

            return


# function that colors keyboard based on correct letters
# key = the letter that is to be filled, color = 2 values ("green" and "yellow")
def fill_key(key, color):
    letter = key.upper()

    # determine which row the letter is in and then draw keys
    if letter in row1:
        pygame.draw.rect(window, color, pygame.Rect(77 + (45 * row1.index(letter)), 575, 40, 50), 0, 7)
    elif letter in row2:
        pygame.draw.rect(window, color, pygame.Rect(100 + (45 * row2.index(letter)), 630, 40, 50), 0, 7)
    else:
        pygame.draw.rect(window, color, pygame.Rect(145 + (45 * row3.index(letter)), 685, 40, 50), 0, 7)

    draw_letters()

    return


# list that contains dictionary containing information for "chance", "index", "color", and "letter"
colored_blocks = []


# function that displays colored blocks onto grid with letter to indicate correct letters
def display_colored_blocks():
    for info in colored_blocks:
        # draw square with green color at position
        square = pygame.Rect(165 + (55 * info["index"]), 175 + (55 * info["chance"]), 50, 50)
        pygame.draw.rect(window, info["color"], square)

        # blit letter onto that square
        letter = font(30).render(info["letter"].upper(), True, (255, 255, 255))
        window.blit(letter, (181 + (55 * info["index"]), 184 + (55 * info["chance"])))

    pygame.display.update()


# function that resets everything after game is over
def reset():
    global finished_word, chance, solved, grid, colored_blocks, correct_letters, correct_word

    # reset grid
    for a in range(6):
        for b in range(5):
            grid[a][b] = ""

    finished_word = False
    chance = 0
    solved = False

    # reset colored things
    colored_blocks = []
    correct_letters = []

    # reset correct word
    while True:
        rand_number = random.randint(0, 5756)
        with open("word-list.txt") as file:
            correct_word = file.readlines()[rand_number].rstrip()

        with open("possible-words.txt") as file2:
            possible_words = file2.readlines()
            new_list = [possible_word.rstrip() for possible_word in possible_words]

            if correct_word not in new_list:
                continue

        # remove 2 letter words
        counts = {}
        two_letter_word = False
        for letter in correct_word:
            if letter in counts.keys():
                two_letter_word = True
                break
            else:
                counts[letter] = 1

        if not two_letter_word:
            break

    # redraw screen
    play()
    display_letters()
    display_colored_blocks()

    print("GAME RESET")

    return

# function that displays play again button to reset
def play_again():
    # play again button that appears after game is finished and resets game
    restart_button = font(15).render("Play Again", True, (255, 196, 37))
    window.blit(restart_button, (253, 138))
    pygame.draw.rect(window, (0, 128, 0), pa_rect, 2)

    pygame.display.update()

# list variable that contains correct letters
correct_letters = []


# function that checks if user uses a chance and checks if word is correct
def check_word():
    global finished_word, chance, correct_letters, solved

    # the user's word that they inputted
    user_word = ""

    # first check if all letters are filled in row
    for l in range(5):
        if grid[chance][l] == "":
            print(False)
            return
        else:
            user_word += grid[chance][l]

    # check if word is valid
    valid = False
    with open("possible-words.txt") as file:
        words = file.readlines()

        for w in words:
            w = w.rstrip()

            # check if user_word in valid word list and display tkinter popup if not valid
            if user_word == w:
                valid = True

    # make sure word is valid using boolean value
    if not valid:
        # display text saying it is invalid
        text = font(15).render("Invalid Word", True, (173, 36, 31))
        window.blit(text, (245, 510))

        pygame.display.update()

        return

    # when user is incorrect, moves on to the next chance
    chance += 1
    finished_word = False

    # variable with new user word to find correct letters, but wrong location
    new_user_word = ""
    new_correct_word = ""

    # list that is an list of correct letters for this chance specifically
    specific_correct_letters = []

    # variables containing tuple of rgb values of colors green, yellow, and dark gray
    green = (108, 169, 101)
    yellow = (200, 182, 83)
    gray = (54, 54, 54)

    # fill all boxes with default gray
    for x in range(5):
        info = {"chance": chance - 1, "index": x, "color": gray, "letter": user_word[x]}
        colored_blocks.append(info)

    # check letters for correct letter and location
    for x in range(5):
        if user_word[x] == correct_word[x]:
            correct_letters.append(user_word[x])
            specific_correct_letters.append(user_word[x])
            new_user_word += " "
            new_correct_word += " "

            # fill key with green when user gets that letter right
            fill_key(user_word[x], green)

            # add to list containing blocks that should be colored
            info = {"chance": chance - 1, "index": x, "color": green, "letter": user_word[x]}
            colored_blocks.append(info)
        else:
            new_user_word += user_word[x]
            new_correct_word += correct_word[x]

    # list containing letters that are already yellow
    yellow_letters = []

    # check letters for correct letter, but wrong locations
    for x in range(5):
        w = new_user_word[x]
        if w != " " and w in new_correct_word and w not in specific_correct_letters:
            new_correct_word.replace(w, "")

            # fill keys with yellow when letter is correct, but not in the right position
            if w not in correct_letters:
                fill_key(w, yellow)

            if w not in yellow_letters:
                # add to list containing blocks that should be colored
                info = {"chance": chance - 1, "index": x, "color": yellow, "letter": w}
                colored_blocks.append(info)

            yellow_letters.append(w)

    # check for letters not in word
    for x in range(5):
        if user_word[x] not in correct_word:
            # fill keyboard with darker gray to denote letter not in word
            fill_key(user_word[x], gray)

    # check if word is correct else check for correct letters
    # if correct, displays correct message and next word button
    if user_word == correct_word:
        # display text saying "You Win! Congrats!"
        text = font(15).render("You Win! Congrats!", True, (173, 36, 31))
        window.blit(text, (236, 510))
        print("Solved!")

        solved = True

        play_again()
    else:
        # when user is incorrect, moves on to next chance unless out of chances and checks letters
        if chance == 6:
            # display text saying "You Lost Sucker!"
            text = font(15).render("You Lost Sucker!", True, (173, 36, 31))
            window.blit(text, (232, 510))

            # display correct word
            text = font(15).render("Correct Word: " + correct_word.upper(), True, (173, 36, 31))
            window.blit(text, (217, 530))
            solved = True

            play_again()

    return


# function that removes a letter from the word when backspace is pressed
def remove_letter():
    global grid, finished_word

    # conditional to make sure that word isn't empty, so nothing to backspace
    if grid[chance][0] != "":
        # loop over each letter to find furthest letter
        for x in range(5):
            if grid[chance][4 - x] != "":
                # remove "invalid word" text if deleting last letter
                if x == 0:
                    cover = pygame.Rect(245, 510, 200, 20)
                    pygame.draw.rect(window, (0, 0, 0), cover)
                grid[chance][4 - x] = ""

                finished_word = False

                return


# function that displays letter when it is added
def display_letters():
    global grid

    for a in range(6):
        for b in range(5):
            if grid[a][b] != "":
                letter = font(30).render(grid[a][b].upper(), True, (255, 255, 255))
                window.blit(letter, (181 + (55 * b), 184 + (a * 55)))
            else:
                return


# main game loop
def mainloop():
    # draw home screen
    home()

    global page, row

    while True:
        for event in pygame.event.get():
            # check to see if user wants to exit game
            if event.type == pygame.QUIT:
                sys.exit()

            # check for button clicks on home page
            if page == "home":
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    check_button_pressed(pos)

            # check for button click on instructions page
            if page == "instructions":
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if b_rect.collidepoint(pos[0], pos[1]):
                        page = "home"
                        home()

            # check for key presses on game page
            if page == "game" and not solved:
                if event.type == pygame.KEYDOWN:
                    # check if keys is alphabetical or the enter/backspace key
                    key = pygame.key.name(event.key)
                    valid = check_key(key)
                    if valid:
                        add_letter(key)
                    elif key == "return":
                        check_word()
                    elif key == "backspace":
                        remove_letter()

                    draw_grid()
                    display_letters()
                    display_colored_blocks()

                    pygame.display.update()

            # check for button click when game is over
            if solved and page == "game":
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pa_rect.collidepoint(pos[0], pos[1]):
                        reset()

# run game
if __name__ == '__main__':
    mainloop()
