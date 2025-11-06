"""
Classe principal do jogo Angry Birds Space
"""
import numpy as np
import pygame
from pygame.locals import *
from typing import List, Optional

# Permitir importações relativas e absolutas
try:
    from .game_objects import Projectile, Cannon, CelestialBody, Target, PowerUp, BlackHole
    from .physics import PhysicsEngine
except ImportError:
    from game_objects import Projectile, Cannon, CelestialBody, Target, PowerUp, BlackHole
    from physics import PhysicsEngine


class Game:
    """Classe principal do jogo"""
    
    def __init__(self, width: int = 1200, height: int = 800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Angry Birds Space")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
        # Cores
        self.BLACK = (0, 0, 0)
        self.SPACE_COLOR = (10, 10, 30)
        self.WHITE = (255, 255, 255)
        
        # Física
        self.physics = PhysicsEngine(dt=1.0/self.FPS)
        
        # Objetos do jogo
        self.cannon = Cannon(np.array([50.0, float(height - 50)]))
        self.projectiles: List[Projectile] = []
        self.celestial_bodies: List[CelestialBody] = []
        self.black_holes: List[BlackHole] = []
        self.power_ups: List[PowerUp] = []
        self.target: Optional[Target] = None
        
        # Estado do jogo
        self.running = True
        self.game_state = "menu"  # "menu", "playing", "victory", "level_complete", "game_over"
        self.aiming = False
        self.aim_start_pos = None
        self.max_projectiles = 5
        self.current_level = 1
        self.total_levels = 3
        self.level_transition_timer = 0
        
        # Estrelas de fundo
        self.stars = self._generate_stars(100)
        
        # Inicializar nível
        self._setup_level(1)
    
    def _generate_stars(self, count: int) -> List[tuple]:
        """Gera estrelas aleatórias para o fundo"""
        import random
        stars = []
        for _ in range(count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            brightness = random.randint(100, 255)
            stars.append((x, y, brightness))
        return stars
    
    def _setup_level(self, level: int):
        # Limpar objetos
        self.projectiles.clear()
        self.celestial_bodies.clear()
        self.black_holes.clear()
        self.power_ups.clear()
        self.max_projectiles = 5
        self.current_level = level
        
        if level == 1:
            # NÍVEL 1: Fácil - Um planeta e um power-up
            self.celestial_bodies.append(
                CelestialBody(
                    position=np.array([600.0, 400.0]),
                    mass=40.0,
                    radius=35,
                    color=(100, 150, 255)
                )
            )
            
            # Power-up que dá projétil extra
            self.power_ups.append(
                PowerUp(
                    position=np.array([300.0, 200.0]),
                    radius=15
                )
            )
            
            # Alvo no canto superior direito
            self.target = Target(
                position=np.array([1100.0, 100.0]),
                radius=25
            )
            
        elif level == 2:
            # NÍVEL 2: Médio - Dois planetas e um power-up, mais complexo
            self.celestial_bodies.append(
                CelestialBody(
                    position=np.array([400.0, 300.0]),
                    mass=50.0,
                    radius=40,
                    color=(100, 150, 255)
                )
            )
            
            self.celestial_bodies.append(
                CelestialBody(
                    position=np.array([800.0, 500.0]),
                    mass=35.0,
                    radius=30,
                    color=(255, 150, 100)
                )
            )
            
            # Power-up em posição mais difícil
            self.power_ups.append(
                PowerUp(
                    position=np.array([600.0, 150.0]),
                    radius=15
                )
            )
            
            # Alvo em posição mais difícil
            self.target = Target(
                position=np.array([1050.0, 150.0]),
                radius=25
            )
            
        elif level == 3:
            # NÍVEL 3: Difícil - Múltiplos planetas e buracos negros
            # Planetas
            self.celestial_bodies.append(
                CelestialBody(
                    position=np.array([300.0, 250.0]),
                    mass=45.0,
                    radius=35,
                    color=(100, 150, 255)
                )
            )
            
            self.celestial_bodies.append(
                CelestialBody(
                    position=np.array([700.0, 400.0]),
                    mass=40.0,
                    radius=30,
                    color=(255, 150, 100)
                )
            )
            
            self.celestial_bodies.append(
                CelestialBody(
                    position=np.array([900.0, 200.0]),
                    mass=30.0,
                    radius=25,
                    color=(150, 255, 150)
                )
            )
            
            # Buracos negros (atração muito forte)
            self.black_holes.append(
                BlackHole(
                    position=np.array([500.0, 500.0]),
                    mass=100.0,  # Massa muito alta
                    radius=20
                )
            )
            
            self.black_holes.append(
                BlackHole(
                    position=np.array([950.0, 350.0]),
                    mass=80.0,
                    radius=18
                )
            )
            
            # Alvo em posição muito difícil
            self.target = Target(
                position=np.array([1100.0, 100.0]),
                radius=25
            )
    
    def _draw_stars(self):
        """Desenha as estrelas de fundo"""
        for x, y, brightness in self.stars:
            color = (brightness, brightness, brightness)
            pygame.draw.circle(self.screen, color, (x, y), 1)
    
    def _draw_menu(self):
        """Desenha o menu inicial"""
        self.screen.fill(self.SPACE_COLOR)
        self._draw_stars()
        
        # Título
        font_large = pygame.font.Font(None, 72)
        font_medium = pygame.font.Font(None, 36)
        
        title = font_large.render("ANGRY BIRDS SPACE", True, self.WHITE)
        title_rect = title.get_rect(center=(self.width // 2, self.height // 2 - 100))
        self.screen.blit(title, title_rect)
        
        # Instruções
        instructions = [
            "Use o mouse para apontar o canhão",
            "Clique e arraste para ajustar a potência",
            "Solte para disparar",
            "Acerte o alvo vermelho!",
            "",
            "Pressione ESPAÇO para começar"
        ]
        
        y_offset = self.height // 2
        for instruction in instructions:
            text = font_medium.render(instruction, True, self.WHITE)
            text_rect = text.get_rect(center=(self.width // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
    
    def _draw_aiming_line(self, start_pos: np.ndarray, end_pos: np.ndarray):
        """Desenha a linha de mira"""
        direction = end_pos - start_pos
        distance = np.linalg.norm(direction)
        
        # Calcular potência (comprimento da linha)
        power = min(distance / 10.0, 20.0)  # Limitar potência máxima
        
        # Cor baseada na potência
        intensity = int(min(255, power * 12))
        color = (255, intensity, 0)
        
        # Desenhar linha
        pygame.draw.line(self.screen, color, 
                        start_pos.astype(int), 
                        end_pos.astype(int), 3)
        
        # Desenhar círculo na ponta
        pygame.draw.circle(self.screen, color, 
                         end_pos.astype(int), 5)
    
    def _update_projectiles(self):
        """Atualiza a física de todos os projéteis"""
        dt = 1.0 / self.FPS
        
        for projectile in self.projectiles:
            if not projectile.active:
                continue
            
            # Calcular aceleração total (soma de todas as forças gravitacionais)
            total_acceleration = np.array([0.0, 0.0])
            
            # Força gravitacional dos planetas
            for celestial_body in self.celestial_bodies:
                grav_accel = self.physics.calculate_gravitational_force(
                    projectile.position,
                    celestial_body.position,
                    celestial_body.mass
                )
                total_acceleration += grav_accel
            
            # Força gravitacional dos buracos negros (muito mais forte)
            for black_hole in self.black_holes:
                grav_accel = self.physics.calculate_gravitational_force(
                    projectile.position,
                    black_hole.position,
                    black_hole.mass
                )
                total_acceleration += grav_accel
            
            # Aplicar resistência do ar
            projectile.velocity = self.physics.apply_air_resistance(
                projectile.velocity, 
                resistance_coefficient=0.999
            )
            
            # Atualizar velocidade
            projectile.velocity = self.physics.update_velocity(
                projectile.velocity,
                total_acceleration
            )
            
            # Atualizar posição
            projectile.position = self.physics.update_position(
                projectile.position,
                projectile.velocity,
                total_acceleration
            )
            
            # Atualizar rastro
            projectile.update_trail()
            
            # Verificar limites da tela
            if (projectile.position[0] < -50 or projectile.position[0] > self.width + 50 or
                projectile.position[1] < -50 or projectile.position[1] > self.height + 50):
                projectile.active = False
            
            # Verificar colisão com corpos celestes
            for celestial_body in self.celestial_bodies:
                distance = np.linalg.norm(projectile.position - celestial_body.position)
                if distance < celestial_body.radius + projectile.radius:
                    projectile.active = False
            
            # Verificar colisão com buracos negros
            for black_hole in self.black_holes:
                distance = np.linalg.norm(projectile.position - black_hole.position)
                if distance < black_hole.event_horizon_radius + projectile.radius:
                    projectile.active = False
            
            # Verificar colisão com power-ups
            for power_up in self.power_ups:
                if not power_up.collected and power_up.check_collision(projectile):
                    power_up.collected = True
                    self.max_projectiles += 1  # Adiciona um projétil extra
            
            # Verificar colisão com alvo
            if self.target and not self.target.hit:
                if self.target.check_collision(projectile):
                    self.target.hit = True
                    if self.current_level < self.total_levels:
                        self.game_state = "level_complete"
                        self.level_transition_timer = 180  # 3 segundos a 60 FPS
                    else:
                        self.game_state = "victory"
    
    def _draw_game(self):
        """Desenha o jogo"""
        # Fundo
        self.screen.fill(self.SPACE_COLOR)
        self._draw_stars()
        
        # Desenhar corpos celestes
        for celestial_body in self.celestial_bodies:
            celestial_body.draw(self.screen)
        
        # Desenhar buracos negros
        for black_hole in self.black_holes:
            black_hole.draw(self.screen)
        
        # Desenhar power-ups
        for power_up in self.power_ups:
            power_up.draw(self.screen)
        
        # Desenhar alvo
        if self.target:
            self.target.draw(self.screen)
        
        # Desenhar projéteis
        for projectile in self.projectiles:
            if projectile.active:
                projectile.draw(self.screen)
        
        # Desenhar canhão
        self.cannon.draw(self.screen)
        
        # Desenhar linha de mira
        if self.aiming and self.aim_start_pos is not None:
            mouse_pos = np.array(pygame.mouse.get_pos())
            self._draw_aiming_line(self.cannon.position, mouse_pos)
        
        # UI
        font = pygame.font.Font(None, 36)
        projectiles_text = font.render(
            f"Projéteis: {len([p for p in self.projectiles if p.active])}/{self.max_projectiles}",
            True, self.WHITE
        )
        self.screen.blit(projectiles_text, (10, 10))
        
        # Mostrar nível atual
        level_text = font.render(f"Nível: {self.current_level}/{self.total_levels}", True, self.WHITE)
        self.screen.blit(level_text, (10, 50))
    
    def _draw_level_complete(self):
        """Desenha tela de nível completo"""
        self._draw_game()
        
        # Overlay semi-transparente
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill(self.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Mensagem
        font = pygame.font.Font(None, 72)
        text = font.render(f"NÍVEL {self.current_level} COMPLETO!", True, (255, 215, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        
        font_small = pygame.font.Font(None, 36)
        if self.current_level < self.total_levels:
            next_text = font_small.render(f"Próximo nível: {self.current_level + 1}", True, self.WHITE)
            next_rect = next_text.get_rect(center=(self.width // 2, self.height // 2 + 60))
            self.screen.blit(next_text, next_rect)
    
    def _draw_victory(self):
        """Desenha tela de vitória final"""
        self._draw_game()
        
        # Overlay semi-transparente
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill(self.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Mensagem
        font = pygame.font.Font(None, 72)
        text = font.render("VITÓRIA TOTAL!", True, (255, 215, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        
        font_small = pygame.font.Font(None, 36)
        restart_text = font_small.render("Pressione R para reiniciar", True, self.WHITE)
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 60))
        self.screen.blit(restart_text, restart_rect)
    
    def handle_events(self):
        """Processa eventos do jogo"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game_state == "menu":
                    self.game_state = "playing"
                    self.current_level = 1
                    self._setup_level(1)
                elif event.key == pygame.K_r and (self.game_state == "victory" or self.game_state == "level_complete"):
                    self.game_state = "menu"
                    self.current_level = 1
                    self._setup_level(1)
                elif event.key == pygame.K_ESCAPE:
                    if self.game_state == "playing":
                        self.game_state = "menu"
                    elif self.game_state == "level_complete":
                        # Pular transição e ir direto para o próximo nível
                        self.current_level += 1
                        self._setup_level(self.current_level)
                        self.game_state = "playing"
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.game_state == "playing":  # Botão esquerdo
                    if len([p for p in self.projectiles if p.active]) < self.max_projectiles:
                        self.aiming = True
                        self.aim_start_pos = np.array(pygame.mouse.get_pos())
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.aiming and self.game_state == "playing":
                    mouse_pos = np.array(pygame.mouse.get_pos())
                    direction = mouse_pos - self.cannon.position
                    distance = np.linalg.norm(direction)
                    power = min(distance / 10.0, 20.0)
                    
                    projectile = self.cannon.fire(mouse_pos, power)
                    self.projectiles.append(projectile)
                    self.aiming = False
            
            elif event.type == pygame.MOUSEMOTION:
                if self.game_state == "playing":
                    mouse_pos = np.array(pygame.mouse.get_pos())
                    self.cannon.aim_at(mouse_pos)
    
    def update(self):
        """Atualiza o estado do jogo"""
        dt = 1.0 / self.FPS
        
        if self.game_state == "playing":
            self._update_projectiles()
            
            # Atualizar animações de power-ups
            for power_up in self.power_ups:
                power_up.update(dt)
            
            # Atualizar animações de buracos negros
            for black_hole in self.black_holes:
                black_hole.update(dt)
        
        elif self.game_state == "level_complete":
            # Contar timer de transição
            self.level_transition_timer -= 1
            if self.level_transition_timer <= 0:
                # Avançar para o próximo nível
                self.current_level += 1
                self._setup_level(self.current_level)
                self.game_state = "playing"
    
    def draw(self):
        """Desenha o jogo"""
        if self.game_state == "menu":
            self._draw_menu()
        elif self.game_state == "playing":
            self._draw_game()
        elif self.game_state == "level_complete":
            self._draw_level_complete()
        elif self.game_state == "victory":
            self._draw_victory()
        
        pygame.display.flip()
    
    def run(self):
        """Loop principal do jogo"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)
        
        pygame.quit()

