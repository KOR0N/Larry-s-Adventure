import pygame as pg
from pygame import font
from cells import Cell  # Importe la classe Cell depuis le module cells.py
from settings import tile_size, screen_width, screen_height, level_music, level_map, level_access, level_type, title_font, ttp, game_over_sound, win_sound
from player import Player  # Importe la classe Player depuis le module player.py
from enemies import Enemy  # Importe la classe Enemy depuis le module enemies.py
from particles import Particle  # Importe la classe Particle depuis le module particles.py

class Level:
    def __init__(self, screen, level_data):
        # Initialise la classe Level avec l'écran et les données du niveau
        self.screen = screen
        self.number_level = level_data
        self.level_data = level_map[level_data]  # Récupère les données du niveau à partir de level_map
        self.level_type = level_type[level_data]
        self.setup_level(self.level_data)  # Configure le niveau en utilisant les données

        # Charge et joue la musique du niveau
        pg.mixer.music.load(level_music[level_data])
        pg.mixer.music.play(1)

        # Charge l'image de fond du niveau
        self.background = pg.image.load("graphics/terrain/" + self.level_type + "/background.png")

        # Initialise d'autres variables de contrôle du niveau
        self.world_mouvement = pg.math.Vector2(0, 0)
        self.background_mouv = 0
        self.total_move = [0, 0]
        self.current_x = 0
        self.player_fall = False
        self.death_transition = pg.image.load('graphics/game_display/character/death_transition.png').convert_alpha()
        self.death_transition_image_y = screen_height
        self.loose_state = False
        self.step1 = True
        self.step2 = False
        self.pos_finish_txt = [screen_width / 2, screen_height / 2]
        self.finish = False
        self.win = False
        self.delay_ttp = 0
        self.particles_effects = pg.sprite.GroupSingle()
        self.size_finish_txt = 0
        self.go_color = 0
        self.sound_played = False

    def setup_level(self, layout):
        # Configure le niveau en fonction des données fournies
        self.cells = pg.sprite.Group()  # Groupe de toutes les cellules du niveau
        self.player = pg.sprite.GroupSingle()  # Groupe pour le joueur
        self.enemies = pg.sprite.Group()  # Groupe pour les ennemis
        self.elements = pg.sprite.Group()  # Groupe pour d'autres éléments (non utilisé dans le code actuel)

        # Parcourt les données du niveau pour créer les différents éléments
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                # Crée des cellules, joueur, ennemis, etc., en fonction des caractères dans les données du niveau
                # Les cellules sont représentées par des 'X', le joueur par 'P', les ennemis par 'E', etc.
                # Les différents types de cellules sont configurés en fonction de la disposition dans le niveau
                # Les données spécifiques à chaque élément sont extraites des paramètres du niveau (level_map, level_type, etc.)

                if cell == 'X':
                    if row_index < len(layout)-1:
                        if layout[row_index-1][col_index] != "X":
                            if layout[row_index][col_index+1] != "X":
                                cell = Cell((x,y),'tr',True,self.level_type)
                            elif layout[row_index][col_index-1] != "X":
                                cell = Cell((x,y),'tl',True,self.level_type)
                            else:
                                cell = Cell((x,y),"t",True,self.level_type)

                            if layout[row_index+1][col_index] != "X":
                                if layout[row_index][col_index+1] != "X":
                                    cell = Cell((x,y),'wl',True,self.level_type)
                                    if layout[row_index][col_index-1] != "X":     
                                        cell = Cell((x,y),'o',True,self.level_type)
                            
                                elif layout[row_index][col_index-1] != "X":
                                    cell = Cell((x,y),'wr',True,self.level_type)
                                else:
                                    cell = Cell((x,y),'w',True,self.level_type)

                        elif layout[row_index+1][col_index] != "X":
                            if layout[row_index][col_index+1] != "X":
                                cell = Cell((x,y),'br',True,self.level_type)
                            elif layout[row_index][col_index-1] != "X":
                                cell = Cell((x,y),'bl',True,self.level_type)
                            else:
                                cell = Cell((x,y),'b',True,self.level_type)

                        else:
                            if layout[row_index][col_index+1] != "X":
                                cell = Cell((x,y),'r',True,self.level_type)
                            elif layout[row_index][col_index-1] != "X":
                                cell = Cell((x,y),'l',True,self.level_type)
                            else:
                                cell = Cell((x,y),"c",True,self.level_type)
                    else:
                        if layout[row_index][col_index+1] != "X":
                            cell = Cell((x,y),'r',True,self.level_type)
                        elif layout[row_index][col_index-1] != "X":
                            cell = Cell((x,y),'l',True,self.level_type)
                        else:
                            cell = Cell((x,y),"c",True,self.level_type)
                    self.cells.add(cell)

                if cell == 'C':
                    self.cells.add(Cell((x,y+22),'C',True,self.level_type))

                if cell == 'T':
                    self.cells.add(Cell((x,y),'T',False,self.level_type))
                    
                if cell == 'D':
                    self.cells.add(Cell((x,y),'D',False,self.level_type))

                if cell == 'P':
                    player_sprite = Player((x,y),self.screen,self.create_jump_particles)
                    self.player.add(player_sprite)

                if cell == 'E':
                    ennemie_sprite = Enemy((x,y),self.screen,True,self.level_type)
                    self.enemies.add(ennemie_sprite)

                if cell == 'F':
                    self.pos_end = [x,y]

    def menu_settings(self):
        # Méthode pour gérer les paramètres du menu (non utilisée dans le code actuel)
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE] and self.menu_activate == False:
            self.menu_activate = True
        elif keys[pg.K_ESCAPE] and self.menu_activate == True:
            self.menu_activate = False

    def create_jump_particles(self, pos):
        # Méthode pour créer des particules lors d'un saut du joueur
        jump_particle_sprite = Particle((pos[0], pos[1] - 15), 'jump', 0.5)
        self.particles_effects.add(jump_particle_sprite)

    def camera(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        #Récupère la cellule avec le plus petit x
        min_x = min(cell.rect.x for cell in self.cells.sprites())


        if player_x < screen_width/3 and direction_x < 0 and self.finish == False and min_x < 0:
            self.world_mouvement[0] = 4 * player.speed_mult
            player.speed = 0
        elif player_x > screen_width - (screen_width/3) and direction_x > 0 and self.finish == False:
            self.world_mouvement[0] = -4 * player.speed_mult
            player.speed = 0
        else:
            self.world_mouvement[0] = 0
            player.speed = 4    

        if player_x <= 0 and direction_x < 0 :
            player.speed = 0   


        player_y = player.rect.centery
        direction_y = player.direction.y
        if (player_y < screen_height/3 or player_y > 2*screen_height/3) and ((self.cells.sprites()[len(self.cells.sprites())-1-len(self.level_data[len(self.level_data)-2]) - len(self.level_data[len(self.level_data)-3])]).rect.y - 640)> 0:
            player.rect.y -= player.direction.y
            self.world_mouvement[1] = -direction_y
        else:
            self.world_mouvement[1] = 0

        if player_y > screen_height:
            self.player_fall = True
        
        if player.rect.x > self.pos_end[0] :
            self.finish = True

    def player_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed * player.speed_mult
        for cell in self.cells.sprites():
            if cell.rect.colliderect(player.rect) and cell.solidity:
                if player.direction.x < 0:
                    player.rect.left = cell.rect.right
                    player.on_l = True
                    self.current_x = player.rect.left                   
                elif player.direction.x > 0:
                    player.rect.right = cell.rect.left
                    player.on_r = True
                    self.current_x = player.rect.right

        player.apply_gravity()
        for cell in self.cells.sprites():
            if cell.rect.colliderect(player.rect) and cell.solidity:
                if player.direction.y > 0:
                    player.rect.bottom = cell.rect.top
                    player.direction.y = 0
                    player.on_g = True
                elif player.direction.y < 0:
                    player.rect.top = cell.rect.bottom
                    player.direction.y = 0
                    player.on_c = True

        if player.on_g and player.direction.y < 0 or player.direction.y > 0.1:
            player.on_g = False
        if player.on_c and player.direction.y > 0.1:
            player.on_c = False

        if player.on_l and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_l = False
        if player.on_r and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_r = False

    def projectiles_collisions(self):
        for projectiles in self.player.sprite.fire_ball_sprite:

            projectiles.rect.x += projectiles.direction.x
            for cell in self.cells.sprites():
                if projectiles.rect.colliderect(cell.rect) and cell.solidity:
                    if projectiles.direction.x > 0:
                        projectiles.speed *= -1
                        projectiles.rect.right = cell.rect.left
                    elif projectiles.direction.x < 0:
                        projectiles.speed *= -1
                        projectiles.rect.left = cell.rect.right
                    projectiles.bounce -=1

            projectiles.rect.y += projectiles.direction.y
            for cell in self.cells.sprites():
                if projectiles.rect.colliderect(cell.rect) and cell.solidity:
                    if projectiles.direction.y > 0:
                        projectiles.direction.y *= -1*2/3
                        projectiles.rect.bottom = cell.rect.top
                    elif projectiles.direction.y < 0:
                        projectiles.direction.y *= -1*2/3
                        projectiles.rect.top = cell.rect.bottom
                    projectiles.bounce -=1

    def enemies_player_collisions(self):
        player = self.player.sprite

        for enemy in self.enemies.sprites():
            player.lifes_sous = True
            if player.rect.colliderect(enemy.rect) and enemy.status != 'death':
                player_center = player.rect.center
                enemy_center = enemy.rect.center

                if player.direction.y > 0:
                    player.rect.bottom = enemy.rect.top
                    player.jump()
                    enemy.status = 'death'
                    enemy.animation_speed = 0.2

                else:
                    if player_center[0] < enemy_center[0]:
                        player.rect.right = enemy.rect.left
                    else:
                        player.rect.left = enemy.rect.right
                    player.direction.y = -8
                    player.damage = True
                    if player.delay_damage >= 10 :
                        player.lifes -= 1
                        player.delay_damage = 0
        player.delay_damage += 1

    def projectiles_enemies_collisions(self):
        for projectile in self.player.sprite.fire_ball_sprite:
            for enemy in self.enemies.sprites():
                if projectile.rect.colliderect(enemy.rect) and enemy.status != 'death' and projectile.bounce > 0:
                    enemy.status = 'death'
                    enemy.animation_speed = 0.2
                    projectile.bounce = 0
        
    def enemies_limits(self):
        for enemy in self.enemies.sprites():
            cell_pos_x = []
            cell_pos_y = []
            for cell in self.cells.sprites():
                if cell.rect.y//64 == enemy.rect.y//64+1:
                    cell_pos_x.append(cell.rect.x//64)
                if cell.rect.y//64 == enemy.rect.y//64:
                     cell_pos_y.append(cell.rect.x//64)
            if (enemy.rect.x//64 in cell_pos_x and enemy.rect.x//64+1 in cell_pos_x):
                if (enemy.rect.x//64 not in cell_pos_y and enemy.rect.x//64+1 not in cell_pos_y):
                    pass
                else:
                    enemy.sens = enemy.sens * -1
            else:
                enemy.sens = enemy.sens * -1


    def respawn(self):
            
        for row_index,row in enumerate(self.level_data):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    self.player.sprite.rect.x = x
                    self.player.sprite.rect.y = y

        for cell in self.cells.sprites():
            cell.rect.x -= self.total_move[0]
            cell.rect.y -= self.total_move[1]

        for projectile in self.player.sprite.fire_ball_sprite :
            projectile.kill()

        for enemie in self.enemies.sprites():
            enemie.rect.x -= self.total_move[0]
            enemie.rect.y -= self.total_move[1]

        self.background_mouv = 0
        self.pos_end[0] -= self.total_move[0]
        self.pos_end[1] -= self.total_move[1]

        self.total_move = [0,0]
        self.player.sprite.lifes -= 1


    def finished(self):        
        self.delay_ttp += 1
        
        if self.size_finish_txt == 200 :
            self.win = True
            level_access[self.number_level+1] = 1

        else:
            self.size_finish_txt += 10
            self.pos_finish_txt[0] -= 16
            self.pos_finish_txt[1] -= 7

        if self.delay_ttp > 100:
            self.screen.blit(ttp,(screen_width/2-60,550))

        finish_txt = font.Font('font/Playa.ttf',self.size_finish_txt)
        txt = finish_txt.render("YOU WIN",1,('Yellow'))
        self.screen.blit(txt,(self.pos_finish_txt))

    def game_over(self):
        # Méthode pour afficher l'écran de fin de jeu lorsque le joueur perd
        loose_txt = title_font.render("GAME OVER",1,(self.go_color, self.go_color, self.go_color))
        self.screen.blit(loose_txt,(screen_width/2 - 450,screen_height/2-50))
        if self.go_color < 255:
            self.go_color += 1
        else:
            self.screen.blit(ttp,(screen_width/2-60,550))
            self.loose_state = True

    def run(self):
        # Méthode principale pour exécuter le niveau
        if self.player.sprite.lifes <= 0 and self.player.sprite.status == "damage":
            self.player_fall = True
        self.screen.blit(self.background,(self.background_mouv,0))

        self.particles_effects.draw(self.screen)
        self.cells.draw(self.screen)
        self.enemies.draw(self.screen)
        self.player.draw(self.screen)

        if self.finish == True:
            # Si le joueur atteint la fin du niveau
            pg.mixer.music.play(0)
            if self.player.sprite.rect.x < screen_width:
                # Si le joueur est encore sur l'écran, continue l'animation du joueur
                self.player.sprite.speed_mult = 2
                self.player.sprite.speed = 4
                self.player_collision()
                self.player.sprite.player_status()
                self.player.sprite.player_animation()
                self.player.sprite.particles_run_animation()
            else:
                # Affiche l'écran de fin de niveau
                if not(self.sound_played):
                    win_sound.play(0)
                    self.sound_played = True
                self.finished()

        elif not(self.player_fall):

            # Si le joueur est en vie et n'est pas tombé
            self.total_move[0] += self.world_mouvement[0]
            self.total_move[1] += self.world_mouvement[1]
            self.background_mouv += self.world_mouvement[0]/4
            self.pos_end[0] += self.world_mouvement[0]
            self.pos_end[1] += self.world_mouvement[1]

            self.particles_effects.update(self.world_mouvement)
            self.cells.update(self.screen,self.world_mouvement)
            self.enemies.update(self.world_mouvement)
            self.enemies_limits()

            self.player.update(self.world_mouvement)
            self.player_collision()
            self.projectiles_collisions()
            self.projectiles_enemies_collisions()
            self.enemies_player_collisions()

            self.camera()

        else:
            # Si le joueur est tombé
            self.screen.blit(self.death_transition,(0,self.death_transition_image_y))
            if self.death_transition_image_y > -340 and self.step1 == True:
                self.death_transition_image_y -= 25
            else:
                self.step2 = True
                if self.player.sprite.lifes <= 0:
                    # Si le joueur n'a plus de vie
                    self.game_over()
                    pg.mixer.music.play(0)
                    if not(self.sound_played):
                        game_over_sound.play(0)
                        self.sound_played = True
                else:
                    # Si le joueur a encore de la vie, effectue la réapparition du joueur
                    if  self.step2 and self.step1:
                        self.respawn()
                        self.step1 = False
                    if self.death_transition_image_y < screen_height and self.step2 == True:
                        self.death_transition_image_y += 25
                    else:
                        self.step2 = False
                        self.step1 = True
                        self.player_fall = False
