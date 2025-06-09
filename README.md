# T2 - Aprendizagem por Reforço: RN + AG + Minimax

**PUCRS - Inteligência Artificial**  
**Profa. Silvia Moraes**

## Objetivo

Construir uma solução de IA usando aprendizagem por reforço que faça uma rede neural aprender a jogar o jogo da Velha.

## Arquitetura

A solução combina três componentes principais:
- **Rede Neural MLP**: 2 camadas para tomada de decisão
- **Algoritmo Genético**: evolui os pesos da rede neural (sem backpropagation)
- **Minimax**: atua como "professor" com 3 níveis de dificuldade

## Estrutura do Projeto

```
├── main.py                     # Arquivo principal
├── requirements.txt            # Dependências
├── README.md                  # Este arquivo
├── src/
│   ├── neural_network/
│   │   └── mlp.py             # Rede Neural MLP
│   ├── genetic_algorithm/
│   │   └── genetic_algo.py    # Algoritmo Genético
│   ├── minimax/
│   │   └── minimax.py         # Minimax com 3 modos
│   ├── game/
│   │   ├── tic_tac_toe.py     # Lógica do jogo
│   │   └── game_state.py      # Estado do jogo
│   ├── training/
│   │   └── trainer.py         # Coordenador de treinamento
│   └── frontend/
│       └── gui.py             # Interface gráfica
└── tests/
    └── test_basic.py          # Testes básicos
```

## Instalação

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

### Interface Gráfica (padrão)
```bash
python main.py
```

### Interface Console
```bash
python main.py --mode console
```

## Modos de Funcionamento

### 1. Usuário vs Minimax
- Permite jogar contra o algoritmo Minimax
- Configurável entre 3 dificuldades (fácil, médio, difícil)

### 2. Treinamento: Rede Neural vs Minimax
- A rede neural aprende jogando contra o Minimax
- Evolução dos pesos via Algoritmo Genético
- Visualização do progresso em tempo real

### 3. Usuário vs Rede Neural
- Jogue contra a rede neural treinada
- Avaliação da performance da IA

## Componentes Técnicos

### Rede Neural MLP
- **Entrada**: Estado do tabuleiro (9 posições)
- **Camada Oculta**: 18 neurônios (configurável)
- **Saída**: 9 neurônios (probabilidade para cada posição)
- **Ativação**: Sigmoid

### Algoritmo Genético
- **Cromossomos**: Pesos da rede neural
- **População**: 50 indivíduos (configurável)
- **Seleção**: Elitismo + Torneio
- **Cruzamento**: BLX-α para valores reais
- **Mutação**: Gaussiana

### Minimax
- **Fácil**: 25% das jogadas usam minimax
- **Médio**: 50% das jogadas usam minimax
- **Difícil**: 100% das jogadas usam minimax

## Desenvolvimento

### TODO - Próximos Passos
1. [ ] Implementar propagação da rede neural
2. [ ] Implementar operadores do algoritmo genético
3. [ ] Implementar algoritmo minimax com modos
4. [ ] Implementar lógica completa do jogo da velha
5. [ ] Implementar função de aptidão
6. [ ] Implementar coordenador de treinamento
7. [ ] Implementar interfaces (GUI e console)
8. [ ] Implementar sistema de persistência
9. [ ] Adicionar visualizações e estatísticas
10. [ ] Testes e validação

### Executar Testes
```bash
python -m pytest tests/
# ou
python tests/test_basic.py
```

## Critérios de Avaliação

- **1,0 pt**: Adaptação do Minimax para os 3 modos
- **2,0 pts**: Rede neural MLP e propagação
- **2,0 pts**: Algoritmo genético completo
- **1,5 pts**: Frontend com 3 modos funcionais
- **2,5 pts**: Relatório de desenvolvimento
- **1,0 pt**: Vídeo demonstrativo (máx 10min)

## Autores

[SEUS NOMES AQUI]

## Data de Entrega

[VERIFICAR CRONOGRAMA DA DISCIPLINA] 