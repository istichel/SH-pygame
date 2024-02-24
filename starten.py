# Importieren u. initialisieren der Pygame-Bibliothek
import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
Breite, Hoehe = 800, 800
FPS  = 60
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((Breite, Hoehe))
pygame.display.set_caption("Mein erstes Spiel")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while True:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()

    # Spiellogik

    # Spielfeld löschen
    fenster.fill(WEISS)

    # Spielfeld/figuren zeichnen

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)