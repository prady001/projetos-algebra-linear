"""
Objetos do jogo: Projétil, Canhão, Corpo Celeste
"""
import numpy as np
import pygame
from typing import List, Optional


class Projectile:
    """Projétil disparado pelo canhão"""
    
    def __init__(self, position: np.ndarray, velocity: np.ndarray, radius: int = 5):
        self.position = position.copy()
        self.velocity = velocity.copy()
        self.radius = radius
        self.active = True
        self.trail = []  # Rastro do projétil
        self.max_trail_length = 20
    
    def update_trail(self):
        """Atualiza o rastro do projétil"""
        self.trail.append(self.position.copy())
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)
    
    def draw(self, screen: pygame.Surface):
        """Desenha o projétil e seu rastro"""
        # Desenhar rastro
        if len(self.trail) > 1:
            for i in range(len(self.trail) - 1):
                alpha = int(255 * (i / len(self.trail)))
                color = (255, 200, 100, alpha)
                pygame.draw.line(screen, (255, 200, 100), 
                               self.trail[i].astype(int), 
                               self.trail[i+1].astype(int), 2)
        
        # Desenhar projétil
        if self.active:
            pygame.draw.circle(screen, (255, 200, 0), 
                             self.position.astype(int), self.radius)
            pygame.draw.circle(screen, (255, 150, 0), 
                             self.position.astype(int), self.radius - 2)


class Cannon:
    """Canhão que dispara projéteis"""
    
    def __init__(self, position: np.ndarray, angle: float = 0.0):
        self.position = position.copy()
        self.angle = angle
        self.length = 30
        self.width = 10
    
    def aim_at(self, target_position: np.ndarray):
        """Aponta o canhão para uma posição alvo"""
        direction = target_position - self.position
        self.angle = np.arctan2(direction[1], direction[0])
    
    def fire(self, mouse_position: np.ndarray, power: float = 10.0) -> Projectile:
        """Dispara um projétil na direção do mouse"""
        # Calcular direção do disparo
        direction = mouse_position - self.position
        distance = np.linalg.norm(direction)
        
        if distance > 0:
            # Normalizar direção
            unit_direction = direction / distance
        else:
            unit_direction = np.array([1.0, 0.0])
        
        # Velocidade inicial
        initial_velocity = unit_direction * power
        
        # Posição inicial (na ponta do canhão)
        cannon_tip = self.position + unit_direction * self.length
        
        return Projectile(cannon_tip, initial_velocity)
    
    def draw(self, screen: pygame.Surface):
        """Desenha o canhão"""
        # Corpo do canhão
        cannon_end = self.position + np.array([
            np.cos(self.angle) * self.length,
            np.sin(self.angle) * self.length
        ])
        
        # Desenhar canhão
        pygame.draw.line(screen, (100, 100, 100), 
                        self.position.astype(int), 
                        cannon_end.astype(int), self.width)
        
        # Base do canhão
        pygame.draw.circle(screen, (80, 80, 80), 
                         self.position.astype(int), 15)


class CelestialBody:
    """Corpo celeste que exerce atração gravitacional"""
    
    def __init__(self, position: np.ndarray, mass: float, radius: int, color: tuple):
        self.position = position.copy()
        self.mass = mass
        self.radius = radius
        self.color = color
        self.glow_radius = radius + 5
    
    def draw(self, screen: pygame.Surface):
        """Desenha o corpo celeste com efeito de brilho"""
        # Brilho externo
        for i in range(3):
            alpha = 50 - i * 15
            glow_radius = self.glow_radius + i * 3
            glow_surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, (*self.color, alpha), 
                             (glow_radius, glow_radius), glow_radius)
            screen.blit(glow_surface, 
                       (self.position[0] - glow_radius, self.position[1] - glow_radius))
        
        # Corpo principal
        pygame.draw.circle(screen, self.color, 
                         self.position.astype(int), self.radius)
        
        # Destaque interno
        highlight_pos = self.position + np.array([-self.radius * 0.3, -self.radius * 0.3])
        highlight_color = tuple(min(255, c + 50) for c in self.color)
        pygame.draw.circle(screen, highlight_color, 
                         highlight_pos.astype(int), self.radius // 3)


class Target:
    """Alvo que o jogador deve acertar"""
    
    def __init__(self, position: np.ndarray, radius: int = 20):
        self.position = position.copy()
        self.radius = radius
        self.hit = False
    
    def check_collision(self, projectile: Projectile) -> bool:
        """Verifica se um projétil colidiu com o alvo"""
        if not projectile.active:
            return False
        
        distance = np.linalg.norm(projectile.position - self.position)
        return distance < (self.radius + projectile.radius)
    
    def draw(self, screen: pygame.Surface):
        """Desenha o alvo"""
        if not self.hit:
            # Círculos concêntricos
            pygame.draw.circle(screen, (255, 0, 0), 
                             self.position.astype(int), self.radius)
            pygame.draw.circle(screen, (255, 255, 255), 
                             self.position.astype(int), self.radius - 5)
            pygame.draw.circle(screen, (255, 0, 0), 
                             self.position.astype(int), self.radius - 10)
            
            # Cruz central
            cross_size = 5
            pygame.draw.line(screen, (255, 255, 255),
                           (self.position[0] - cross_size, self.position[1]),
                           (self.position[0] + cross_size, self.position[1]), 2)
            pygame.draw.line(screen, (255, 255, 255),
                           (self.position[0], self.position[1] - cross_size),
                           (self.position[0], self.position[1] + cross_size), 2)


class PowerUp:
    """Power-up que dá projéteis extras ao jogador"""
    
    def __init__(self, position: np.ndarray, radius: int = 15):
        self.position = position.copy()
        self.radius = radius
        self.collected = False
        self.animation_time = 0.0
        self.pulse_radius = radius
    
    def check_collision(self, projectile: Projectile) -> bool:
        """Verifica se um projétil colidiu com o power-up"""
        if self.collected or not projectile.active:
            return False
        
        distance = np.linalg.norm(projectile.position - self.position)
        return distance < (self.radius + projectile.radius)
    
    def update(self, dt: float):
        """Atualiza a animação do power-up"""
        if not self.collected:
            self.animation_time += dt
            self.pulse_radius = self.radius + int(3 * np.sin(self.animation_time * 5))
    
    def draw(self, screen: pygame.Surface):
        """Desenha o power-up com animação pulsante"""
        if not self.collected:
            # Brilho pulsante
            for i in range(3):
                alpha = 100 - i * 30
                glow_radius = self.pulse_radius + i * 2
                glow_surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, (255, 215, 0, alpha), 
                                 (glow_radius, glow_radius), glow_radius)
                screen.blit(glow_surface, 
                           (self.position[0] - glow_radius, self.position[1] - glow_radius))
            
            # Corpo principal (estrela)
            points = []
            for i in range(10):
                angle = (i * np.pi / 5) - np.pi / 2
                if i % 2 == 0:
                    r = self.radius
                else:
                    r = self.radius * 0.5
                x = self.position[0] + r * np.cos(angle)
                y = self.position[1] + r * np.sin(angle)
                points.append((x, y))
            
            pygame.draw.polygon(screen, (255, 215, 0), points)
            pygame.draw.polygon(screen, (255, 255, 0), points, 2)


class BlackHole(CelestialBody):
    """Buraco negro com atração gravitacional muito forte"""
    
    def __init__(self, position: np.ndarray, mass: float, radius: int):
        super().__init__(position, mass, radius, (0, 0, 0))
        self.event_horizon_radius = radius + 10
        self.animation_time = 0.0
    
    def update(self, dt: float):
        """Atualiza a animação do buraco negro"""
        self.animation_time += dt
    
    def draw(self, screen: pygame.Surface):
        """Desenha o buraco negro com efeito de distorção"""
        # Anel de acréscimo (disco de matéria)
        for i in range(5):
            angle = self.animation_time * 2 + i * (2 * np.pi / 5)
            ring_radius = self.radius + 15 + i * 3
            x = self.position[0] + ring_radius * np.cos(angle)
            y = self.position[1] + ring_radius * np.sin(angle)
            pygame.draw.circle(screen, (100, 50, 200), (int(x), int(y)), 3)
        
        # Horizonte de eventos (círculo preto)
        pygame.draw.circle(screen, (0, 0, 0), 
                         self.position.astype(int), self.event_horizon_radius)
        
        # Brilho ao redor (efeito de lente gravitacional)
        for i in range(4):
            alpha = 80 - i * 20
            glow_radius = self.event_horizon_radius + i * 5
            glow_surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, (50, 0, 100, alpha), 
                             (glow_radius, glow_radius), glow_radius)
            screen.blit(glow_surface, 
                       (self.position[0] - glow_radius, self.position[1] - glow_radius))
        
        # Centro (singularidade)
        pygame.draw.circle(screen, (20, 0, 40), 
                         self.position.astype(int), self.radius // 2)

