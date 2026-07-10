# Pygame Learn - Jogo 2D Platformer

Um jogo 2D simples desenvolvido com a biblioteca **Pygame** como parte do aprendizado da biblioteca.

## 📝 Sobre

Este projeto foi desenvolvido com base no tutorial do YouTube [**"The Ultimate Introduction to Pygame"**](https://youtu.be/AY9MnQ4x3zk?si=RXiWUx8d1TgZGnyy) do canal **Clear Code**. O tutorial oferece uma introdução completa ao desenvolvimento de jogos com Pygame, cobrindo desde conceitos básicos até implementações mais avançadas.

## 🎮 Funcionalidades

- Controle do jogador com movimento e pulo
- Obstáculos dinâmicos (caracóis e moscas)
- Sistema de pontuação baseado no tempo
- Efeito parallax no fundo do cenário
- Música e efeitos sonoros
- Tela de início e game over com exibição da pontuação

## 🛠️ Tecnologias Utilizadas

- **Python** - Linguagem de programação
- **Pygame** - Biblioteca para desenvolvimento de jogos

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca Pygame:

   ```bash
   pip install pygame
   ```
3. Execute o jogo:

   ```bash
   python main.py
   ```

## 🎯 Como Jogar

- Pressione **ESPAÇO** para iniciar o jogo.
- Pressione **ESPAÇO** para fazer o jogador pular.
- Desvie dos obstáculos para continuar vivo.
- O jogo termina ao colidir com um obstáculo, exibindo sua pontuação final.

## 📦 Estrutura do Projeto

```
.
├── main.py                # Arquivo principal do jogo
├── audio/                 # Arquivos de áudio
│   ├── jump.mp3
│   └── music.wav
├── font/                  # Fonte personalizada
│   └── Pixeltype.ttf
└── graphics/              # Sprites e texturas
    ├── Fly/
    ├── Player/
    ├── snail/
    ├── ground.png
    ├── sky.png
    └── sky2.png
```

## 📚 Referência

- [The Ultimate Introduction to Pygame - Clear Code](https://youtu.be/AY9MnQ4x3zk?si=RXiWUx8d1TgZGnyy)
- [Documentação do Pygame](https://www.pygame.org/docs/)

---

Projeto criado para fins educacionais.
