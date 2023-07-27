from operator import truediv
from telnetlib import GA
import pygame
import time
import random

pygame.init()

# WORDLE
#
# Wordle in python
# Guess five letter words and try to get the chosen word
# Green means the letter is in the word and that position
# Yellow means the letter is in the word just not that position
# Gray means the letter is not in the word
# Get the chosen word in six guesses or you lose

# DO: 
    #Aline the letters better
    #Keyboard

WIDTH, HEIGTH = 900, 750
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (106, 170, 100) #6aaa64
YELLOW = (201, 180, 88) #c9b458
GRAY = (120, 124, 126) #787c7e

BASE_FONT = pygame.font.Font(None,64)
SEC_FONT = pygame.font.Font(None,32)

GAME = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Wordle")

def findColors(word, h):
    testAnswer = list(ANSWER)
    for i in range(5):
            length = 160+(120*i)
            height = 25 +(h*120)
            if word[i] == testAnswer[i]: #Check for Green letters 
                #If the letter is in that position
                pygame.draw.rect(GAME, GREEN, pygame.Rect(length, height, 100, 100))
                testAnswer[i] = "-"
            elif word[i] == testAnswer[0] or word[i] == testAnswer[1] or  word[i] == testAnswer[2] or  word[i] == testAnswer[3] or  word[i] == testAnswer[4]:
                #Check for Yellow letters
                #If the letter is in the word and not the position
                if word[i] == testAnswer[0] and word[0] != testAnswer[0]:
                    pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    testAnswer[0] = "-"
                elif word[i] == testAnswer[1] and word[1] != testAnswer[1]:
                    pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    testAnswer[1] = "-"
                elif word[i] == testAnswer[2] and word[2] != testAnswer[2]:
                    pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    testAnswer[2] = "-"
                elif word[i] == testAnswer[3] and word[3] != testAnswer[3]:
                    pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    testAnswer[3] = "-"
                elif word[i] == testAnswer[4] and word[4] != testAnswer[4]:
                    pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    testAnswer[4] = "-"
                else:
                    #If in the word but the position is already taken
                    pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                
            else:
                #If not Green or Yellow letter then Gray
                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))

            #Print letters
            letter = BASE_FONT.render(word[i],True,(BLACK))
            if i == 0:
                GAME.blit(letter,(length+35,height+30)) 
            elif i == 1:
                GAME.blit(letter,(length+35,height+30)) 
            elif i == 2:
                GAME.blit(letter,(length+35,height+30)) 
            elif i == 3:
                GAME.blit(letter,(length+35,height+30)) 
            elif i == 4:
                GAME.blit(letter,(length+35,height+30)) 

def getAnswer():
    wordList = open("/Users/joshfried/Downloads/Projects/Python_Games/Wordle/wordList.txt", "r")
    num = random.randint(0,5756)
    word = wordList.readlines()
    answer = word[num]
    print(str(num))
    print(word[num])
    wordList.close()
    return answer.upper()

ANSWER = getAnswer()

def loseGame():
    pygame.draw.rect(GAME, BLACK, pygame.Rect(300, 325, 300, 100))
    lose = BASE_FONT.render("YOU LOSE",True,(WHITE))
    GAME.blit(lose,(320,345)) # MAKE SQUARE
    word = SEC_FONT.render("Answer: " + ANSWER[0:5],True,(WHITE))
    GAME.blit(word,(320,390)) # MAKE SQUARE


def winGame():
    pygame.draw.rect(GAME, BLACK, pygame.Rect(300, 325, 300, 100))
    letter = BASE_FONT.render("YOU WIN",True,(WHITE))
    GAME.blit(letter,(320,345)) # MAKE SQUARE

def draw_guesses(one, two, three, four, five, six, guesses):
    g1 = False
    g2 = False
    g3 = False
    g4 = False
    g5 = False
    g6 = False

    if len(one) == 5:
        g1 = True
    if len(two) == 5:
        g2 = True
    if len(three) == 5:
        g3 = True
    if len(four) == 5:
        g4 = True
    if len(five) == 5:
        g5 = True
    if len(six) == 5:
        g6 = True

    if g1:
        findColors(one, 0)
    if g2:
        findColors(two, 1)
    if g3:
        findColors(three, 2)
    if g4:
        findColors(four, 3)
    if g5:
        findColors(five, 4)
    if g6:
        findColors(six, 5)
    

def invalidInput():
    pygame.draw.rect(GAME, BLACK, pygame.Rect(300, 100, 300, 100))
    letter = BASE_FONT.render("Invalid Input",True,(WHITE))
    GAME.blit(letter,(320,120)) # MAKE SQUARE
    pygame.display.update()
    time.sleep(1)

def checkGuess(input, guesses): # finish guesses 
    valid = False
    wordList = open("/Users/joshfried/Downloads/Projects/Python_Games/Wordle/wordList.txt", "r")
    words = wordList.readlines()

    for i in range(5756):
        if words[i].upper()[0:5] == input[0:5]:
            valid = True
    wordList.close()

    if valid:
        if(input[0:5] == ANSWER[0:5]):
            print("Correct " + input)
            return "win"
        else:
            print("Nope " + input)
            return "lose"
    else:
        return "invalid"

def printInput(input, guesses):
    # TRY: printInput(user_text, guesses)
    height = 55 + 120*(guesses)
    #GAME.blit(letter,(160,height))

    #text_surface = BASE_FONT.render(user_text[0:6],True,(255,255,255))
    #GAME.blit(text_surface,(10,10))
    for i in range(len(input)):
        letter = BASE_FONT.render(input[i],True,(BLACK))
        if i == 0:
            GAME.blit(letter,(195,height)) 
        elif i == 1:
            GAME.blit(letter,(315,height)) # how to do middle diffence for W and I ?????
        elif i == 2:
            GAME.blit(letter,(435,height))
        elif i == 3:
            GAME.blit(letter,(555,height))
        elif i == 4:
            GAME.blit(letter,(675,height))

    pygame.display.update()


def draw_window():
    GAME.fill(WHITE)
    for i in range(0, 481, 120):
        for j in range(0, 601, 120): # DO guesses*120 not 0
            pygame.draw.rect(GAME, BLACK, pygame.Rect(160+i, 25+j, 100, 100), 2)
    
    #pygame.draw.rect(GAME, BLACK, pygame.Rect(195, 55, 30, 40), 2)
    #pygame.display.update()

def main():
    #ADD guesses
    clock = pygame.time.Clock()
    run = True
    WIN = False
    user_text = ""
    guesses = 0
    guess_one = ""
    guess_two = ""
    guess_three = ""
    guess_four = ""
    guess_five = ""
    guess_six = ""
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_a and event.key != pygame.K_b and event.key != pygame.K_c and event.key != pygame.K_d and event.key != pygame.K_e and event.key != pygame.K_f and event.key != pygame.K_g and event.key != pygame.K_h and event.key != pygame.K_i and event.key != pygame.K_j and event.key != pygame.K_k and event.key != pygame.K_l and event.key != pygame.K_m and event.key != pygame.K_n and event.key != pygame.K_o and event.key != pygame.K_p and event.key != pygame.K_q and event.key != pygame.K_r and event.key != pygame.K_s and event.key != pygame.K_t and event.key != pygame.K_u and event.key != pygame.K_v and event.key != pygame.K_w and event.key != pygame.K_x and event.key != pygame.K_y and event.key != pygame.K_z and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN: 
                    invalidInput()
                    break
                if len(user_text) > 5:
                    user_text = user_text[:-1]
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN: 
                    if len(user_text) != 5:
                        invalidInput()
                        break
                    else:
                        guesses += 1
                        check = checkGuess(user_text.upper(), guesses)
                        if check == "win":
                            WIN = True
                        elif check == "invalid":
                            invalidInput()
                            guesses -= 1
                            break

                        if guesses == 1:
                            guess_one = user_text.upper()
                        elif guesses == 2:
                            guess_two = user_text.upper()
                        elif guesses == 3:
                            guess_three = user_text.upper()
                        elif guesses == 4:
                            guess_four = user_text.upper()
                        elif guesses == 5:
                            guess_five = user_text.upper()
                        elif guesses == 6:
                            guess_six = user_text.upper()
                        
                        user_text = ""
                else:
                    user_text += event.unicode
        if len(guess_six) > 0 and not WIN:
            loseGame()
        if WIN:
            winGame()
            
        printInput(user_text.upper(), guesses)
        draw_window()
        draw_guesses(guess_one, guess_two, guess_three, guess_four, guess_five, guess_six, guesses)

    pygame.quit()

if __name__ == "__main__":
    main()
  
 