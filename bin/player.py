import pygame as pg
from settings import files_import
from projectiles import Fire_balls
from particles import Particle

class Player(pg.sprite.Sprite):
    def __init__(self, pos, screen, create_jump_particles):
        super().__init__()

        self.life_sous = True  # Booléen indiquant si le joueur a des vies restantes

        # Paramètres graphiques
        self.character_assets()
        self.screen = screen
        self.animation_speed = 0.20
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # Paramètres des particules
        self.run_particles = files_import(self.character_path + '/particles/run')
        self.particles_frame = 0
        self.particles_animation_speed = 0.15
        self.create_jump_particles = create_jump_particles

        # Paramètres de mouvement
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 4
        self.speed_mult = 1
        self.gravity = 0.8
        self.jump_speed = -18
        self.jump_limitation = 1

        # État du personnage
        self.status = 'idle'
        self.face_direction = True
        self.on_g = False  # Sur le sol
        self.on_c = False  # Sur le plafond
        self.on_r = False  # Sur le mur droit
        self.on_l = False  # Sur le mur gauche

        # Paramètres de vies
        self.lifes = 3
        self.lifes_started = self.lifes
        self.life_image = pg.image.load('graphics/game_display/character/lives2.png').convert_alpha()
        self.no_lifes_image = pg.image.load('graphics/game_display/character/lives_loosed2.png').convert_alpha()
        self.lifes_animation = files_import('graphics/game_display/character/animation')
        self.lifes_animation_speed = 0.20
        self.lifes_frame = 0
        self.damage = False
        self.delay_damage = 10

        # Paramètres des projectiles
        self.fire_ball_sprite = pg.sprite.Group()
        self.projectiles_time = 0
        self.explosion_particles = pg.sprite.GroupSingle()

    def character_assets(self):
        # Charger les animations du personnage
        self.character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': [], 'damage': []}

        for animation in self.animations.keys():
            full_path = self.character_path + animation
            self.animations[animation] = files_import(full_path)

    def particles_run_animation(self):
        # Mettre à jour et afficher les particules de course
        if self.status == 'run' and self.on_g:
            self.particles_frame += self.particles_animation_speed
            if self.particles_frame >= len(self.run_particles):
                self.particles_frame = 0

            run_particle = self.run_particles[int(self.particles_frame)]

            pos = self.rect.bottomleft
            player_sprite_size_x = self.image.get_size()[0]
            if self.face_direction:
                self.screen.blit(run_particle, (pos[0] - 10, pos[1] - 11))
            else:
                self.screen.blit(pg.transform.flip(run_particle, True, False), (pos[0] + player_sprite_size_x, pos[1] - 11))

    def player_status(self):
        # Déterminer le statut du joueur en fonction de la direction et du mouvement
        if self.direction.y < 0:
            self.status = 'jump'
            self.animation_speed = 0.40
        elif self.direction.y > 1:
            self.status = 'fall'
            self.animation_speed = 0.20
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
            self.animation_speed = 0.20

    def player_animation(self):
        # Mettre à jour l'animation du joueur
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.face_direction == True:
            self.image = image
        else:
            flipped_image = pg.transform.flip(image, True, False)
            self.image = flipped_image

        if self.on_g and self.on_r:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_g and self.on_l:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_g:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_c and self.on_r:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_c and self.on_l:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_c:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def apply_gravity(self):
        # Appliquer la gravité au joueur
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        # Faire sauter le joueur
        self.direction.y = self.jump_speed

    def keyboard_mouvement(self):
        # Gérer les mouvements au clavier
        keys = pg.key.get_pressed()

        # Mouvements de base (droite, gauche)
        if 1:
            if keys[pg.K_RIGHT]:
                self.direction.x = 1
                self.face_direction = True
            elif keys[pg.K_LEFT]:
                self.direction.x = -1
                self.face_direction = False
            else:
                self.direction.x = 0

        if keys[pg.K_LSHIFT]:
            self.speed_mult = 2
            self.animation_speed = 0.20
        else:
            self.speed_mult = 1
            self.animation_speed = 0.10

        # Mouvement de saut du personnage
        if (keys[pg.K_SPACE] or keys[pg.K_UP]) and self.jump_limitation == 1:
            self.jump()
            self.jump_limitation = 0
            self.on_g = False
            self.create_jump_particles(self.rect.midbottom)

        # Créer des boules de feu
        if keys[pg.K_x] and self.projectiles_time > 10:
            image_size = self.image.get_size()
            fire_ball = Fire_balls(self.screen, (self.rect.x + image_size[0] / 2, self.rect.y + image_size[1] / 2), self.face_direction, self.speed_mult)
            self.fire_ball_sprite.add(fire_ball)
            self.projectiles_time = 0

        if 1:
            # Limiter la possibilité de sauter si le joueur n'est pas sur le sol
            if self.on_g:
                self.jump_limitation = 1
            else:
                self.jump_limitation = 0

    def particle_explosion(self):
        # Gérer l'explosion des particules
        for fire_balls in self.fire_ball_sprite:
            if fire_balls.bounce == 0:
                explosion_particle = Particle((fire_balls.rect.x-5,fire_balls.rect.y-5),'explosion')
                self.explosion_particles.add(explosion_particle)
                
    def lifes_gestion(self):
        # Gérer les vies du joueur
        self.lifes_frame += self.lifes_animation_speed

        if self.lifes_frame >= len(self.lifes_animation):
            self.lifes_frame = 0
        
        lifes_flames_animation = self.lifes_animation[int(self.lifes_frame)]

        for i in range(self.lifes_started):
            if i+1 <= self.lifes:
                self.screen.blit(lifes_flames_animation,(90-8+i*100,90-54))
                self.screen.blit(self.life_image,(100+i*100,100))
            else:
                self.screen.blit(self.no_lifes_image,(100+i*100,100))

    def damage_taked(self):
        # Gérer les dégâts subis par le joueur
        self.status = 'damage'
        if self.face_direction == True:
            self.direction.x = -1
        else:
            self.direction.x = 1

        if self.on_g:
            self.damage = False
            
    def update(self,world_mouvement):
        # Mettre à jour l'état du joueur
        if not(self.damage):
            self.keyboard_mouvement()
            self.player_status() 
        else:
            self.damage_taked()
        self.player_animation()
        self.particles_run_animation()
        self.lifes_gestion()
        self.fire_ball_sprite.update(world_mouvement)
        self.fire_ball_sprite.draw(self.screen)
        self.projectiles_time += 0.2
