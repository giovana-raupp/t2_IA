import numpy as np

class MLP:
    """
    Rede Neural MLP de 2 camadas para aprender jogo da velha
    Entrada: estado do tabuleiro (9 posições)
    Saída: probabilidades para cada posição (9 saídas)
    """
    
    def __init__(self, input_size=9, hidden_size=18, output_size=9):
        """
        Inicializa a rede neural
        Args:
            input_size: tamanho da entrada (9 para tabuleiro 3x3)
            hidden_size: neurônios na camada oculta
            output_size: tamanho da saída (9 posições possíveis)
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Pesos serão definidos pelo AG, não inicializados aqui
        self.weights_input_hidden = None
        self.weights_hidden_output = None
        self.bias_hidden = None
        self.bias_output = None
        
    def set_weights(self, chromosome):
        """
        Define os pesos da rede a partir de um cromossomo do AG
        Args:
            chromosome: array com todos os pesos da rede
        """
        pass
    
    def forward_propagation(self, input_data):
        """
        Executa a propagação direta na rede
        Args:
            input_data: entrada da rede (estado do tabuleiro)
        Returns:
            output: saída da rede (probabilidades para cada posição)
        """
        if self.weights_input_hidden is None or self.weights_hidden_output is None:
            raise ValueError("Network weights not initialized")

        # Garante que a entrada esteja no formato correto
        x = np.asarray(input_data).reshape(-1)
        if x.size != self.input_size:
            raise ValueError("Invalid input size")

        # Camada oculta
        hidden_input = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)

        # Camada de saída
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_input)

        return output
    
    def sigmoid(self, x):
        """Função de ativação sigmoid"""
        return 1 / (1 + np.exp(-x))
    
    def get_best_move(self, board_state):
        """
        Retorna a melhor jogada baseada na saída da rede
        Args:
            board_state: estado atual do tabuleiro
        Returns:
            move: posição escolhida (0-8)
        """
        pass
    
    def get_total_weights_count(self):
        """
        Retorna o número total de pesos na rede
        Returns:
            count: número total de pesos e bias
        """
        pass 