#!/usr/bin/env python

import pygame
import time

pygame.init()

pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#screen.fill((0,0,255))
#pygame.display.update()
#time.sleep(1)
#
#screen.fill((0,255,0))
#pygame.display.update()
#time.sleep(1)
#
#screen.fill((255,0,0))
#pygame.display.update()
#time.sleep(1)
#
screen.fill((255,255,255))
pygame.display.update()
#time.sleep(1)

pygame.quit()
