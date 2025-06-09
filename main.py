#!/usr/bin/env python3
"""
Trabalho T2 - Inteligência Artificial
PUCRS - Profa. Silvia Moraes

Aprendizagem por Reforço: RN + AG + Minimax
Jogo da Velha com Rede Neural treinada por Algoritmo Genético

Autores: [SEUS NOMES AQUI]
Data: [DATA]
"""

import sys
import argparse
from src.frontend.gui import TicTacToeGUI, ConsoleInterface

def main():
    """Função principal da aplicação"""
    parser = argparse.ArgumentParser(description='Jogo da Velha com IA')
    parser.add_argument('--mode', choices=['gui', 'console'], default='gui',
                        help='Modo de interface (gui ou console)')
    parser.add_argument('--config', type=str, help='Arquivo de configuração')
    
    args = parser.parse_args()
    
    try:
        if args.mode == 'gui':
            # Inicia interface gráfica
            app = TicTacToeGUI()
            app.run()
        else:
            # Inicia interface de console
            app = ConsoleInterface()
            app.run()
            
    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"Erro na aplicação: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 