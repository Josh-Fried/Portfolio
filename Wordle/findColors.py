import pygame
from main import *

def findColors(word, h):
     for i in range(5):
            length = 160+(120*i)
            height = 25 +(h*120)
            if word[i] == ANSWER[i]:
                pygame.draw.rect(GAME, GREEN, pygame.Rect(length, height, 100, 100))
            elif word[i] == ANSWER[0] or word[i] == ANSWER[1] or  word[i] == ANSWER[2] or  word[i] == ANSWER[3] or  word[i] == ANSWER[4]:
                if i == 0:
                    if word[i] == ANSWER[1]:
                        if word[1] == ANSWER[1]:
                            if word[i] == ANSWER[2] and word[2] != ANSWER[2]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[2]:
                        if word[2] == ANSWER[2]:
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[3]:
                        if word[3] == ANSWER[3]:
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[4]:
                        if word[4] == ANSWER[4]:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
#llama
#lousy
                elif i == 1:
                    if word[i] == ANSWER[0]:
                        if word[0] == ANSWER[0]:
                            if word[i] == ANSWER[2] and word[2] != ANSWER[2]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[2]:
                        if word[2] == ANSWER[2]:
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[3]:
                        if word[3] == ANSWER[3]:
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[4]:
                        if word[4] == ANSWER[4]:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                elif i == 2:
                    if word[i] == ANSWER[0]:
                        if word[0] == ANSWER[0]:
                            if word[i] == ANSWER[1] and word[1] != ANSWER[1]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[1]:
                        if word[1] == ANSWER[1]:
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[3]:
                        if word[3] == ANSWER[3]:
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[4]:
                        if word[4] == ANSWER[4]:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                elif i == 3:
                    if word[i] == ANSWER[0]:
                        if word[0] == ANSWER[0]:
                            if word[i] == ANSWER[1] and word[1] != ANSWER[1]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[2] and word[2] != ANSWER[2]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[1]:
                        if word[1] == ANSWER[1]:
                            if word[i] == ANSWER[2] and word[2] != ANSWER[2]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[2]:
                        if word[2] == ANSWER[2]:
                            if word[i] == ANSWER[4] and word[4] != ANSWER[4]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[4]:
                        if word[4] == ANSWER[4]:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                elif i == 4:
                    if word[i] == ANSWER[0]:
                        if word[0] == ANSWER[0]:
                            if word[i] == ANSWER[1] and word[1] != ANSWER[1]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[2] and word[2] != ANSWER[2]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[1]:
                        if word[1] == ANSWER[1]:
                            if word[i] == ANSWER[2] and word[2] != ANSWER[2]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                    elif word[i] == ANSWER[2]:
                        if word[2] == ANSWER[2]:
                            if word[i] == ANSWER[3] and word[3] != ANSWER[3]:
                                pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
                            else:
                                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))
                        else:
                            pygame.draw.rect(GAME, YELLOW, pygame.Rect(length, height, 100, 100))
            else:
                pygame.draw.rect(GAME, GRAY, pygame.Rect(length, height, 100, 100))

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