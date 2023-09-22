# PythonChess

<img src="src/images/logo.png" alt="Logo" width="400" height="570">

Este é um projeto de xadrez em Python que utiliza a biblioteca Tkinter para a interface gráfica e o motor de xadrez Stockfish para as jogadas.

## Recursos

- [x] Interface gráfica intuitiva.
- [ ]  Suporte para jogar contra um oponente humano ou contra o Stockfish.
- [x]  Análise de jogadas com a ajuda do Stockfish.
- [x]  Histórico de movimentos.
- [ ]  Contagem de movimentos, xeques, xeque-mate e empates.æ
- [x]  Personalização do nível de dificuldade do Stockfish. 

## Capturas de Tela

<div style="display: flex; flex-direction: row;">
  <img src="assets/images/tabuleiro-organizado.png" alt="Tabuleiro organizado" width="400" height="570">
  <img src="assets/images/tabuleiro-jogado.png" alt="Tabuleiro com jogada" width="400" height="570">
</div>


## Como Jogar

1. **Clone o repositório:**

```bash
git clone https://github.com/JoaoAndrade18/PythonChess.git
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. Compile o Stockfish:

```bash
Em desenvolvimento...
```

4. Execute o main.py

```bash
python main.py
```

## Como Jogar - Botões e Recursos

Quando você executar o PythonChess, terá acesso a vários botões e recursos na interface gráfica. Abaixo, explicamos o significado de cada um deles:

- **Reiniciar partida:** Inicia um novo jogo de xadrez.
  
- **Salvar jogo:** Permite salvar o estado do jogo. (*Em desenvolvimento...*)
  
- **Carregar Jogo:** Permite carregar um jogo salvo anteriormente. (*Em desenvolvimento...*)
  
- **Desfazer Jogada:** Desfaz o último movimento no jogo.
  
- **Sugerir jogada:** Ativa o motor de xadrez Stockfish para indicar a melhor jogada.
  
- **Histórico de Movimentos:** Exibe o histórico completo de todos os movimentos realizados durante a partida, destacando as jogadas das peças brancas.
  
- **Tamanho da Tela:** Permite redimensionar a janela para tamanhos predefinidos.
  
- **Sair do jogo:** Fecha o jogo PythonChess de forma adequada.
  
- **Jogar Sozinho:** O motor Stockfish fará todas as jogadas com base na melhor escolha possível, sem interações do usuário.
  
- **Diminuir e Aumentar tempo:** Modifica a profundidade de tempo que o Stockfish usará para escolher o melhor movimento.


## Contribuindo

Se você gostaria de contribuir para este projeto, por favor siga as diretrizes de contribuição descritas em [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.