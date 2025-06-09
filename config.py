"""
Arquivo de configuração para o projeto T2-IA
Centraliza todos os parâmetros configuráveis
"""

# Configurações da Rede Neural
NEURAL_NETWORK_CONFIG = {
    'input_size': 9,        # Tabuleiro 3x3
    'hidden_size': 18,      # Neurônios na camada oculta
    'output_size': 9,       # 9 posições possíveis
    'activation_function': 'sigmoid'
}

# Configurações do Algoritmo Genético
GENETIC_ALGORITHM_CONFIG = {
    'population_size': 50,
    'max_generations': 100,
    'mutation_rate': 0.1,
    'crossover_rate': 0.8,
    'elitism_rate': 0.1,
    'tournament_size': 3,
    'convergence_threshold': 0.001
}

# Configurações do Minimax
MINIMAX_CONFIG = {
    'difficulties': {
        'easy': 0.25,      # 25% das jogadas usam minimax
        'medium': 0.50,    # 50% das jogadas usam minimax
        'hard': 1.0        # 100% das jogadas usam minimax
    },
    'max_depth': 9  # Profundidade máxima da árvore
}

# Configurações de Treinamento
TRAINING_CONFIG = {
    'training_schedule': ['easy', 'medium', 'hard'],  # Ordem das dificuldades
    'generations_per_difficulty': [30, 30, 40],       # Gerações por dificuldade
    'games_per_evaluation': 10,                       # Jogos para avaliar cada cromossomo
    'neural_network_starts_first': True               # IA sempre inicia jogando
}

# Configurações da Função de Aptidão
FITNESS_CONFIG = {
    'win_reward': 10,           # Pontos por vitória
    'draw_reward': 1,           # Pontos por empate
    'loss_penalty': -5,         # Penalidade por derrota
    'invalid_move_penalty': -2,  # Penalidade por jogada inválida
    'game_length_bonus': 0.1    # Bonus por prolongar o jogo
}

# Configurações da Interface Gráfica
GUI_CONFIG = {
    'window_width': 800,
    'window_height': 600,
    'board_size': 300,
    'button_size': 80,
    'update_frequency': 100  # ms para atualizar progresso do treinamento
}

# Configurações de Salvamento/Carregamento
PERSISTENCE_CONFIG = {
    'save_training_progress': True,
    'save_best_networks': True,
    'results_directory': 'results/',
    'models_directory': 'models/',
    'plots_directory': 'plots/'
}

# Configurações de Debug/Logging
DEBUG_CONFIG = {
    'verbose_training': True,
    'save_generation_stats': True,
    'plot_training_progress': True,
    'log_level': 'INFO'
} 