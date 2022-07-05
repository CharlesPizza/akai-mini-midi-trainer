import pygame
import mido
import rtmidi
from LittleLamb import BAR, TEMPO
import time

pygame.init()
outport = mido.open_output()
inport = mido.open_input()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

notes = []
non_notes = []
state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    for b in BAR:
        for n in b:
            x = ((n-12)%25) * 20 + 150 
            notes.append([x, 0])

    for i in range(len(notes)):
        pygame.draw.circle(screen, [255,255,255], notes[i], 10)
        notes[i][1] += 1
    for i in range(len(non_notes)):
        pygame.draw.circle(screen, [0,0,0], non_notes[i], 10)
        non_notes[i][1] += 1

    pygame.display.flip()
    clock.tick(TEMPO)


pygame.quit()