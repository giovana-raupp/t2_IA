from enum import Enum
import numpy as np

class GameResult(Enum):
    """Possíveis resultados do jogo"""
    NEURAL_NETWORK_WIN = 1
    MINIMAX_WIN = -1
    DRAW = 0
    ONGOING = None

class GameState:
    """
    Representa o estado completo de uma partida
    Usado para análise e estatísticas
    """
    
    def __init__(self):
        """Inicializa o estado do jogo"""
        self.moves_history = []  # Histórico de jogadas
        self.board_states = []   # Estados do tabuleiro a cada jogada
        self.result = GameResult.ONGOING
        self.total_moves = 0
        self.invalid_moves_nn = 0  # Jogadas inválidas da rede neural
        self.game_duration = 0
        
    def add_move(self, player, position, board_state):
        """
        Adiciona uma jogada ao histórico
        Args:
            player: jogador que fez a jogada (1 ou -1)
            position: posição jogada (0-8)
            board_state: estado do tabuleiro após a jogada
        """
        pass
    
    def set_result(self, result):
        """
        Define o resultado final do jogo
        Args:
            result: GameResult
        """
        pass
    
    def increment_invalid_move(self):
        """Incrementa contador de jogadas inválidas da rede neural"""
        pass
    
    def get_game_statistics(self):
        """
        Retorna estatísticas da partida
        Returns:
            stats: dicionário com estatísticas
        """
        pass
    
    def reset(self):
        """Reseta o estado para uma nova partida"""
        pass 