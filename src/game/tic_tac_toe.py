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
        if not 0 <= position < 9:
            return False

        if self.board[position] != 0:
            return False

        self.board[position] = player
        self.current_player = -player
        return True
    
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
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
            (0, 4, 8), (2, 4, 6)              # diagonais
        ]

        for a, b, c in win_combinations:
            if self.board[a] == self.board[b] == self.board[c] != 0:
                self.winner = int(self.board[a])
                self.game_over = True
                return self.winner

        if 0 not in self.board:
            self.winner = 0
            self.game_over = True
            return 0

        return None
    
    def is_game_over(self):
        """
        Verifica se o jogo terminou
        Returns:
            game_over: boolean
        """
        if self.game_over:
            return True

        # Atualiza estado verificando vitória ou empate
        result = self.check_winner()
        return result is not None
    
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