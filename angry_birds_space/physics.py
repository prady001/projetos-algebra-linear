"""
Módulo de física para o jogo Angry Birds Space
Implementa movimento uniforme, gravidade e outras forças físicas
"""
import numpy as np


class PhysicsEngine:
    """Motor de física para simulação de movimento e gravidade"""
    
    def __init__(self, dt=1/60.0):
        self.dt = dt
        self.gravitational_constant = 500.0  # Constante gravitacional ajustada para o jogo
    
    def calculate_gravitational_force(self, position, celestial_body_pos, celestial_body_mass):
        """Calcula a força gravitacional exercida por um corpo celeste"""
        # Vetor de posição relativa
        r = celestial_body_pos - position
        
        # Distância entre os corpos
        distance = np.linalg.norm(r)
        
        # Evitar divisão por zero e distâncias muito pequenas
        epsilon = 10.0
        if distance < epsilon:
            distance = epsilon
        
        # Módulo da aceleração gravitacional: a = G*M / r^2
        acceleration_magnitude = self.gravitational_constant * celestial_body_mass / (distance ** 2)
        
        # Vetor unitário na direção do corpo celeste
        if distance > 0:
            unit_vector = r / distance
        else:
            unit_vector = np.array([0.0, 0.0])
        
        # Vetor de aceleração
        acceleration = acceleration_magnitude * unit_vector * 1.4
        
        return acceleration
    
    def update_position(self, position, velocity, acceleration):
        """Atualiza a posição usando movimento uniformemente variado"""
        # Movimento uniformemente variado:
        # s_n = s_{n-1} + v_{n-1} * dt + 0.5 * a * dt^2
        new_position = position + velocity * self.dt + 0.5 * acceleration * self.dt ** 2
        return new_position
    
    def update_velocity(self, velocity, acceleration):
        """Atualiza a velocidade usando aceleração"""
        # v_n = v_{n-1} + a * dt
        new_velocity = velocity + acceleration * self.dt
        return new_velocity
    
    def apply_air_resistance(self, velocity, resistance_coefficient=0.98):
        """Aplica resistência do ar (força de arrasto)"""
        return velocity * resistance_coefficient

