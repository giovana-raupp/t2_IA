import random

class MinimaxPlayer:
    """
    Algoritmo Minimax adaptado com 3 modos de dificuldade
    - Fácil: usa minimax em 25% das jogadas
    - Médio: usa minimax em 50% das jogadas  
    - Difícil: usa minimax em 100% das jogadas
    """
    
    def __init__(self, difficulty='hard', symbol='O'):
        """
        Inicializa o jogador Minimax
        Args:
            difficulty: 'easy', 'medium', 'hard'
            symbol: símbolo do jogador ('X' ou 'O')
        """
        self.difficulty = difficulty
        self.symbol = symbol
        self.opponent_symbol = 'X' if symbol == 'O' else 'O'
        
        # Probabilidades de usar minimax por dificuldade
        self.minimax_probability = {
            'easy': 0.25,
            'medium': 0.50,
            'hard': 1.0
        }
    
    def get_move(self, board_state):
        """
        Retorna a próxima jogada baseada na dificuldade
        Args:
            board_state: estado atual do tabuleiro
        Returns:
            move: posição escolhida (0-8)
        """
        pass
    
    def minimax(self, board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
        """
        Algoritmo Minimax com poda alfa-beta
        Args:
            board: estado do tabuleiro
            depth: profundidade atual
            is_maximizing: se é turno do maximizador
            alpha: valor alfa para poda
            beta: valor beta para poda
        Returns:
            score: valor da posição
        """
        pass
    
    def evaluate_board(self, board):
        """
        Avalia o estado atual do tabuleiro
        Args:
            board: estado do tabuleiro
        Returns:
            score: pontuação da posição
        """
        pass
    
    def get_random_move(self, board_state):
        """
        Retorna uma jogada aleatória válida
        Args:
            board_state: estado do tabuleiro
        Returns:
            move: posição aleatória válida
        """
        pass
    
    def get_available_moves(self, board_state):
        """
        Retorna lista de movimentos válidos
        Args:
            board_state: estado do tabuleiro
        Returns:
            moves: lista de posições disponíveis
        """
        pass
    
    def set_difficulty(self, difficulty):
        """
        Altera a dificuldade do minimax
        Args:
            difficulty: 'easy', 'medium', 'hard'
        """
        pass 