import numpy as np

class TicTacToe:
    """
    Lógica do Jogo da Velha
    Tabuleiro representado como array 1D de 9 posições
    0 = vazio, 1 = X, -1 = O
    """
    
    def __init__(self):
        """Inicializa o jogo"""
        self.board = np.zeros(9, dtype=int)  # Tabuleiro 3x3 como array 1D
        self.current_player = 1  # 1 = X (rede neural), -1 = O (minimax)
        self.game_over = False
        self.winner = None
        
    def reset_game(self):
        """Reinicia o jogo"""
        pass
    
    def make_move(self, position, player):
        """
        Executa uma jogada
        Args:
            position: posição no tabuleiro (0-8)
            player: jogador (1 ou -1)
        Returns:
            success: se a jogada foi válida
        """
        pass
    
    def is_valid_move(self, position):
        """
        Verifica se uma jogada é válida
        Args:
            position: posição no tabuleiro (0-8)
        Returns:
            valid: boolean
        """
        pass
    
    def check_winner(self):
        """
        Verifica se há um vencedor
        Returns:
            winner: 1, -1, 0 (empate) ou None (jogo continua)
        """
        pass
    
    def is_game_over(self):
        """
        Verifica se o jogo terminou
        Returns:
            game_over: boolean
        """
        pass
    
    def get_available_moves(self):
        """
        Retorna lista de movimentos válidos
        Returns:
            moves: lista de posições disponíveis
        """
        pass
    
    def get_board_copy(self):
        """
        Retorna cópia do tabuleiro atual
        Returns:
            board_copy: cópia do tabuleiro
        """
        pass
    
    def print_board(self):
        """Imprime o tabuleiro de forma legível"""
        pass
    
    def board_to_string(self):
        """
        Converte tabuleiro para string
        Returns:
            board_str: representação string do tabuleiro
        """
        pass
    
    def get_board_state_for_nn(self):
        """
        Retorna estado do tabuleiro normalizado para a rede neural
        Returns:
            state: array normalizado para entrada da rede
        """
        pass 