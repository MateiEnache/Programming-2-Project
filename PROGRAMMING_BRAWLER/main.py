import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.current_quest = ""

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont('comic sans ms', 100)
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        
        self.character_spritesheet = Spritesheet('Programming-2-Project\PROGRAMMING_BRAWLER\character.png')
        self.terrain_spritesheet = Spritesheet('Programming-2-Project/PROGRAMMING_BRAWLER/terrain.png')
        self.enemy_spritesheet = Spritesheet('Programming-2-Project\PROGRAMMING_BRAWLER\enemy.png')
        self.attack_spritesheet = Spritesheet('Programming-2-Project/PROGRAMMING_BRAWLER/attack.png')
        self.intro_background = pygame.image.load('Programming-2-Project\PROGRAMMING_BRAWLER\introbackground.png')
        self.go_background = pygame.image.load('Programming-2-Project\PROGRAMMING_BRAWLER\gameover.png')
    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == ',':
                    Ground2(self, j, i)
                if column == ';':
                    Ground4(self, j, i)
                if column == 'R':
                    Rock1(self, j, i)
                if column == '?':
                    Ground3(self, j, i)
                if column == 'X':
                    Block(self, j, i)
                if column == '.':
                    Ground(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'P':
                    self.player = Player(self, j, i)
                if column == ' ':
                    Empty(self, j, i)
                if column == 'B':
                    Bridge(self, j, i)
                if column == 'D':
                    Sand(self, j, i)
                if column == 'S':
                    Snow(self, j, i)
                if column == 'A':
                    Path(self, j, i)
                if column == '1':
                    fall1(self, j, i)
                if column == '2':
                    fall2(self, j, i)
                if column == '3':
                    fall3(self, j, i)
                if column == '4':
                    fall4(self, j, i)
                if column == '5':
                    fall5(self, j, i)
                if column == '6':
                    fall6(self, j, i)
                if column == '7':
                    fall7(self, j, i)
                if column == '8':
                    fall8(self, j, i)
                if column == '9':
                    fall9(self, j, i)
                if column == '0':
                    fall0(self, j, i)
                if column == '!':
                    fallten(self, j, i)
                if column == '$':
                    falleleven(self, j, i)
                if column == 'q':
                    falltwelve(self, j, i)
                if column == 'w':
                    fallthirteen(self, j, i)
                if column == 'e':
                    fallfourteen(self, j, i)
                if column == 'r':
                    Rock2(self, j, i)

        
    def new(self):
        pygame.mixer.music.load('Programming-2-Project\PROGRAMMING_BRAWLER\SLOWER-TEMPO2019-12-09_-_Retro_Forest_-_David_Fesliyan.mp3')
        pygame.mixer.music.play(loops=-1)
        self.createTilemap()
        self.playing = True
            
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.playing = False
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
        
    def update(self):
        self.all_sprites.update()
        
    def draw(self):
        self.screen.fill(BLUE) 
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

        if self.current_quest:
            text_surface = self.font.render(self.current_quest, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.screen.get_width() - text_surface.get_width() - 10, 10))

        
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        if self.playing == False:
            death = pygame.mixer.Sound('Programming-2-Project\PROGRAMMING_BRAWLER\gta-v-wasted-death-sound.mp3')
            death.play()
            time.sleep(2.3)
        
    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))
        
        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart')
        
        for sprite in self.all_sprites:
            sprite.kill()
            
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            
            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
        
    def intro_screen(self):
        intro = True
        
        title = self.font.render('IsleQuest', True, BLACK)
        title_rect = title.get_rect(x=100, y=100)
        
        play_button = Button(225, 240, 200, 50, WHITE, BLACK, 'Start  Quest')
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                    
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
            
        
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
