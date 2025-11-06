"""
Ponto de entrada principal do jogo Angry Birds Space
"""
import sys
import os

# Permitir execução direta do script
if __name__ == "__main__":
    # Adicionar o diretório atual ao path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    
    # Importações locais quando executado diretamente
    from game import Game
    from game_objects import Projectile, Cannon, CelestialBody, Target
    from physics import PhysicsEngine
else:
    # Importações relativas quando usado como módulo
    from .game import Game


def main():
    """Função principal que inicia o jogo"""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

