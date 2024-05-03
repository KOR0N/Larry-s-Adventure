import pygame as pg
from pygame import font
from cells import Cell
from settings import tile_size, screen_width, screen_height, level_music, level_map, loose_txt, pos_finish_txt
from player import Player
from enemies import Enemy
from particles import Particle

class Level:
    def __init__(self,screen,level_data):
        self.screen = screen
        self.level_data = level_map[level_data]
        self.setup_level(self.level_data)

        pg.mixer.music.load(level_music[level_data])
        pg.mixer.music.play(1)

        self.background = pg.image.load("graphics\\terrain\\background_test.png")

        self.world_mouvement = pg.math.Vector2(0,0)
        self.background_mouv = 0
        self.total_move = [0,0]
        self.current_x = 0

        self.player_fall = False
        self.death_transition = pg.image.load('graphics/game_display/character/death_transition.png').convert_alpha()
        self.death_transition_image_y = screen_height
        self.loose_state = False
        self.step1 = True
        self.step2 = False
        self.finish = False

        self.particles_effects = pg.sprite.GroupSingle()
        
        self.size_finish_txt = 0

    def setup_level(self,layout):
        self.cells = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        self.enemies = pg.sprite.Group()
        self.elements = pg.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    if layout[row_index-1][col_index] != "X":
                        if layout[row_index][col_index+1] != "X":
                            cell = Cell((x,y),'tr',True)
                        elif layout[row_index][col_index-1] != "X":
                            cell = Cell((x,y),'tl',True)
                        else:
                            cell = Cell((x,y),"t",True)

                    else:
                        if layout[row_index][col_index+1] != "X":
                            cell = Cell((x,y),'r',True)
                        elif layout[row_index][col_index-1] != "X":
                            cell = Cell((x,y),'l',True)
                        else:
                            cell = Cell((x,y),"b",True)
                    self.cells.add(cell)
                    # self.elements.add(cell)

                if cell == 'C':
                    self.cells.add(Cell((x,y+22),'c',True))
                    # self.elements.add(Cell((x,y+22),'c',True))

                if cell == 'T':
                    self.cells.add(Cell((x,y),'T',False))
                    # self.elements.add(Cell((x,y),'T',False))
                    
                if cell == 'D':
                    self.cells.add(Cell((x,y),'D',False))

                if cell == 'P':
                    player_sprite = Player((x,y),self.screen,self.create_jump_particles)
                    self.player.add(player_sprite)

                if cell == 'E':
                    ennemie_sprite = Enemy((x,y),self.screen,True)
                    self.enemies.add(ennemie_sprite)
                    # self.elements.add(ennemie_sprite)

                if cell == 'F':
                    self.pos_end = [x,y]

    def menu_settings(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE] and self.menu_activate == False:
            self.menu_activate = True
        elif keys[pg.K_ESCAPE] and self.menu_activate == True:
            self.menu_activate = False

    def create_jump_particles(self,pos):
        jump_particle_sprite = Particle((pos[0],pos[1]-15),'jump',0.5)
        self.particles_effects.add(jump_particle_sprite)

    def camera(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/3 and direction_x < 0:
            self.world_mouvement[0] = 4 * player.speed_mult
            player.speed = 0
        elif player_x > screen_width - (screen_width/3) and direction_x > 0:
            self.world_mouvement[0] = -4 * player.speed_mult
            player.speed = 0
        else:
            self.world_mouvement[0] = 0
            player.speed = 4       


        player_y = player.rect.centery
        direction_y = player.direction.y

        if (player_y < screen_height/3 or player_y > 2*screen_height/3) and ((self.cells.sprites()[len(self.cells.sprites())-1-len(self.level_data[len(self.level_data)-2]) - len(self.level_data[len(self.level_data)-3])]).rect.y - 640) > 0:
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
                        projectiles.direction.y *= -1
                        projectiles.rect.bottom = cell.rect.top
                    elif projectiles.direction.y < 0:
                        projectiles.direction.y *= -1
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
                    player.lifes -= 1
                    # player.define_lifes()
                    player.damage = True
                    player.direction.y = -8
                    print(player.direction.y)
                    if player.life_sous == True:
                        # player.lifes -= 1
                        # print(player.lifes)
                        # player.lifes -= 1
                        # print(str(player.lifes) + "\n")
                        player.life_sous = False

    # def enemies_player_collisions(self):
    #     player = self.player.sprite

    #     for enemie in self.enemies.sprites():
    #         if enemie.rect.colliderect(player.rect):
    #             if player.direction.x < 0:
    #                 player.rect.left = enemie.rect.right
    #                 player.direction.x -= 10
    #                 player.direction.y -= 2
    #                 player.lives -= 1
    #                 self.current_x = player.rect.left                   
    #             elif player.direction.x > 0:
    #                 player.rect.right = enemie.rect.left
    #                 player.direction.x = 2
    #                 player.direction.y -= 10
    #                 player.lives -= 1
    #                 self.current_x = player.rect.right
                

    #     for enemie in self.enemies.sprites():
    #         if enemie.rect.colliderect(player.rect):
    #             if player.direction.y > 0:
    #                 player.rect.bottom = enemie.rect.top
    #                 player.jump()
    #                 enemie.kill()
    #             elif player.direction.y < 0:
    #                 player.rect.top = enemie.rect.bottom
    #                 player.direction.y = 0
    #                 player.lives -= 1

    def projectiles_enemies_collisions(self):
        for projectile in self.player.sprite.fire_ball_sprite:
            for enemy in self.enemies.sprites():
                if projectile.rect.colliderect(enemy.rect) and enemy.status != 'death' and projectile.bounce > 0:
                    enemy.status = 'death'
                    enemy.animation_speed = 0.2
                    projectile.bounce = 0
        
    def enemies_limits(self):
        for enemy in self.enemies.sprites():
            cell_pos = []
            for cell in self.cells.sprites():
                if cell.rect.y//64 == enemy.rect.y//64+1:
                    cell_pos.append(cell.rect.x//64)
            if enemy.rect.x//64 in cell_pos and enemy.rect.x//64+1 in cell_pos:
                pass
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
            projectile.rect.x -= self.total_move[0]
            projectile.rect.y -= self.total_move[1]

        for enemie in self.enemies.sprites():
            enemie.rect.x -= self.total_move[0]
            enemie.rect.y -= self.total_move[1]

        self.background_mouv = 0
        self.pos_end[0] -= self.total_move[0]
        self.pos_end[1] -= self.total_move[1]

        self.total_move = [0,0]
        self.player.sprite.lifes -= 1

    def end(self):
        if self.size_finish_txt == 200 :
            pass
        else:
            self.size_finish_txt += 10
            pos_finish_txt[0] -= 16
            pos_finish_txt[1] -= 7
        finish_txt = font.Font(None,self.size_finish_txt)
        txt = finish_txt.render("YOU WIN",1,('white'))
        self.screen.blit(txt,(pos_finish_txt))

    def run(self):
        self.screen.blit(self.background,(self.background_mouv,0))

        self.particles_effects.draw(self.screen)
        self.cells.draw(self.screen)
        self.enemies.draw(self.screen)
        self.player.draw(self.screen)


        if self.finish == True:
            if self.player.sprite.rect.x < screen_width:
                self.player.sprite.rect.x += 8
                self.player.sprite.player_animation()
            else:
                self.end()

        elif not(self.player_fall):

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
            x_loose = screen_width
            if self.death_transition_image_y > -340 and self.step1 == True:
                self.death_transition_image_y -= 25
            else:
                self.step2 = True
                if self.player.sprite.lifes == 0:
                    x_loose = screen_width/2 - 200
                    self.loose_state = True

                else:
                    if  self.step2 and self.step1:
                        self.respawn()
                        self.step1 = False
                    if self.death_transition_image_y < screen_height and self.step2 == True:
                        self.death_transition_image_y += 25
                    else:
                        self.step2 = False
                        self.step1 = True
                        self.player_fall = False

            self.screen.blit(self.death_transition,(0,self.death_transition_image_y))
            self.screen.blit(loose_txt,(x_loose,screen_height/2-10))
        
        