import tkinter as tk
from tkinter import ttk, messagebox
import threading
from ..game.tic_tac_toe import TicTacToe
from ..minimax.minimax import MinimaxPlayer
from ..neural_network.mlp import MLP
from ..training.trainer import Trainer

class TicTacToeGUI:
    """
    Interface gráfica para o jogo da velha com 3 modos:
    1. Usuário vs Minimax
    2. Treinamento: Rede Neural vs Minimax
    3. Usuário vs Rede Neural treinada
    """
    
    def __init__(self):
        """Inicializa a interface gráfica"""
        self.root = tk.Tk()
        self.root.title("Jogo da Velha - IA com AG + RN + Minimax")
        self.root.geometry("800x600")
        
        # Componentes do jogo
        self.game = None
        self.minimax_player = None
        self.neural_network = None
        self.trainer = None
        
        # Estado da interface
        self.current_mode = None
        self.training_in_progress = False
        
        # Elementos da GUI
        self.buttons = []
        self.status_label = None
        self.progress_bar = None
        
        self.setup_gui()
        
    def setup_gui(self):
        """Configura a interface gráfica"""
        pass
    
    def create_menu(self):
        """Cria menu superior com opções de modo"""
        pass
    
    def create_game_board(self):
        """Cria o tabuleiro do jogo"""
        pass
    
    def create_control_panel(self):
        """Cria painel de controles"""
        pass
    
    def create_training_panel(self):
        """Cria painel para acompanhar treinamento"""
        pass
    
    # Modo 1: Usuário vs Minimax
    def start_user_vs_minimax(self):
        """Inicia modo usuário contra minimax"""
        pass
    
    def user_move(self, position):
        """
        Processa jogada do usuário
        Args:
            position: posição clicada (0-8)
        """
        pass
    
    def minimax_move(self):
        """Executa jogada do minimax"""
        pass
    
    # Modo 2: Treinamento Rede Neural vs Minimax
    def start_training_mode(self):
        """Inicia modo de treinamento"""
        pass
    
    def run_training(self):
        """Executa treinamento em thread separada"""
        pass
    
    def update_training_progress(self, generation, stats):
        """
        Atualiza progresso do treinamento na interface
        Args:
            generation: geração atual
            stats: estatísticas da geração
        """
        pass
    
    def training_completed(self):
        """Callback quando treinamento termina"""
        pass
    
    # Modo 3: Usuário vs Rede Neural
    def start_user_vs_neural_network(self):
        """Inicia modo usuário contra rede neural"""
        pass
    
    def neural_network_move(self):
        """Executa jogada da rede neural"""
        pass
    
    # Métodos auxiliares
    def update_board_display(self):
        """Atualiza visualização do tabuleiro"""
        pass
    
    def update_status(self, message):
        """
        Atualiza mensagem de status
        Args:
            message: mensagem a ser exibida
        """
        pass
    
    def reset_game(self):
        """Reinicia o jogo atual"""
        pass
    
    def show_game_result(self, result):
        """
        Mostra resultado do jogo
        Args:
            result: resultado da partida
        """
        pass
    
    def configure_minimax_difficulty(self):
        """Abre dialog para configurar dificuldade do minimax"""
        pass
    
    def show_training_statistics(self):
        """Mostra estatísticas detalhadas do treinamento"""
        pass
    
    def load_trained_network(self):
        """Carrega rede neural já treinada"""
        pass
    
    def save_trained_network(self):
        """Salva rede neural treinada"""
        pass
    
    def run(self):
        """Inicia a aplicação"""
        pass

class ConsoleInterface:
    """
    Interface de console alternativa (mais simples)
    """
    
    def __init__(self):
        """Inicializa interface de console"""
        pass
    
    def show_menu(self):
        """Mostra menu principal"""
        pass
    
    def run_user_vs_minimax(self):
        """Executa modo usuário vs minimax"""
        pass
    
    def run_training(self):
        """Executa treinamento via console"""
        pass
    
    def run_user_vs_neural_network(self):
        """Executa modo usuário vs rede neural"""
        pass
    
    def print_board(self, board):
        """
        Imprime tabuleiro no console
        Args:
            board: estado do tabuleiro
        """
        pass
    
    def get_user_move(self):
        """
        Obtém jogada do usuário via input
        Returns:
            position: posição escolhida
        """
        pass
    
    def run(self):
        """Inicia interface de console"""
        pass 