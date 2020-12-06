import pygame   #importiert die Pygamme Bibliothek in das Skript   
import os   
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN)  #importiert bestimmte Konstanten aus dem OS Modul in das Skript

class Settings(object):
    def __init__(self):
        self.width = 700    #gibt die Breite des Fensters an
        self.height = 400   #gibt die Höhe des Fensters an
        self.fps = 60       #gibt die Bilder pro Sekunde an
        self.title = "Game1.1"  #gibt den Programmnamen an
        self.file_path = os.path.dirname(os.path.abspath(__file__))    #Angabe woher er Dateien finden kann
        self.images_path = os.path.join(self.file_path, "images")   #Ordner festgelegt, wo Python zugreifen kann

    def get_dim(self):
        return (self.width, self.height)    #gibt die Breite x Höhe zurück



class Dog(pygame.sprite.Sprite):    #Objekt Dog
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self) #Da von den Pygame-Sprites geerbt wird, werden hier die Funktion initalisiert
        self.settings = settings
        self.pygame = pygame
        self.image = pygame.image.load(os.path.join(self.settings.images_path, "doggo.png")).convert_alpha() #das bmp für den Hund wird reinimportiert
        self.image = pygame.transform.scale(self.image, (110, 60))   #Größe des Bildes
        self.rect = self.image.get_rect()
        self.rect.left = (settings.width - self.rect.width) // 2    #Diese und die nächste Zeile sind dafür zuständig, dass das bmp mittig zentriert ist
        self.rect.top = settings.height - self.rect.height - 10
        self.direction = 0
        self.direction2 = 0
        self.speed = 5

    def update(self):
        newleft = self.rect.left + (self.direction * self.speed)
        newright = newleft + self.rect.width
        newtop = self.rect.top + (self.direction2 * self.speed)
        newbottom = newtop + self.rect.height
        
        if newleft > 0 and newright < settings.width:
            self.rect.left = newleft
        if newtop > 0 and newbottom < settings.height:
            self.rect.top = newtop
        
        

class Game(object):
    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.get_dim())   #die Breite und Höhe des Fensters wird festgelegt
        self.pygame.display.set_caption(self.settings.title)    #der sichtbare Programmname wird festgelegt
        self.background = self.pygame.image.load(os.path.join(self.settings.images_path, "background.jpg")).convert()   #der Hintergrund wird festgelegt
        self.background_rect = self.background.get_rect()
        self.clock = pygame.time.Clock()    #die Bilder pro Sekunde werden festgelegt
        self.done = False
        self.dog = Dog(settings)

        self.all_doggos = pygame.sprite.Group() #die Sprite Gruppe all_doggos wird erstellt
        self.all_doggos.add(self.dog)   #das Objekt self.dog wird der Gruppe all_doggos hinzugefügt

    def run(self):  #bringt das Spiel zum laufen
        while not self.done:             
            self.clock.tick(self.settings.fps)            
            for event in self.pygame.event.get():   
                if event.type == QUIT:   
                    self.done = True 
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.done = True
                    
                    elif event.key == K_LEFT:
                        self.dog.direction = -1
                    elif event.key == K_RIGHT:
                        self.dog.direction = 1
                   
                    elif event.key == K_UP:
                        self.dog.direction2 = -1
                    elif event.key == K_DOWN:
                        self.dog.direction2 = 1

                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.dog.direction = 0
                    elif event.key == K_UP or event.key == K_DOWN:
                        self.dog.direction2 = 0


            self.update()
            self.draw()

    def draw(self): #alle Objekte werden gezeichnet und der Bildschirm wird aktualisiert
        self.screen.blit(self.background, self.background_rect)
        self.all_doggos.draw(self.screen)
        self.pygame.display.flip()

    def update(self):
        self.all_doggos.update()

if __name__ == '__main__':  #main-Schleife   
                                    
    settings = Settings()
    pygame.init()               
    game = Game(pygame, settings)
    game.run()
  
    pygame.quit()               