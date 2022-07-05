import pygame
import mido
import rtmidi

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

    for msg in inport.iter_pending():
        n = msg.note
# Determining where on screen note falls
# notes 12 -> 36; 25 notes * 20 = 500. Screenwidth = 800. center among 300.
# Notes - note.min %(num_keys) * 20(pixel seperation) + 150(center the 500px range in 800px screenwidth)
        x = ((n-12)%25) * 20 + 150 
        if msg.velocity > 0:
            notes.append([x, 0])
            print(x)
            print(n)
        else:
            msg = mido.Message('note_off', note=n)
            outport.send(msg)
            non_notes.append([x, 0])
            print(f'{x} release')

    for i in range(len(notes)):
        pygame.draw.circle(screen, [255,255,255], notes[i], 10)
        notes[i][1] += 1
    for i in range(len(non_notes)):
        pygame.draw.circle(screen, [0,0,0], non_notes[i], 10)
        non_notes[i][1] += 1
    pygame.display.flip()
    clock.tick(120)


pygame.quit()