import pygame
import mido
import rtmidi

pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()
state = True
# ===========Cursor=======================
pygame.mouse.set_cursor(*pygame.cursors.diamond)
# ===========Font Renders=========================
pygame.font.init()
start_font = pygame.font.SysFont('arial', 30)
start_txt = start_font.render('Start Game', False, (255, 255,255))
configure_txt = start_font.render('Configure Settings', False, (255, 255,255))
song_txt = start_font.render('Edit Songs', False, (255, 255,255))


# blit Fonts
start_blit = screen.blit(start_txt, [(800 - start_txt.get_rect().width)//2, 300])
config_blit = screen.blit(configure_txt, [(800 - configure_txt.get_rect().width)//2, 400])
song_blit = screen.blit(song_txt, [(800 - song_txt.get_rect().width)//2, 500])

# Event Loop
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            state = False
        elif event.type == pygame.MOUSEBUTTONDOWN and start_blit.collidepoint(pygame.mouse.get_pos()):
            print('Start Detected')
        elif event.type == pygame.MOUSEBUTTONDOWN and config_blit.collidepoint(pygame.mouse.get_pos()):
            print('Config Detected')
        elif event.type == pygame.MOUSEBUTTONDOWN and song_blit.collidepoint(pygame.mouse.get_pos()):
            print('Song Detected')
    clock.tick(30)
    pygame.display.flip()


pygame.display.quit()
pygame.quit()