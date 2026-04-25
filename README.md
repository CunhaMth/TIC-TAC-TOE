# 🎮 Jogo da Velha com Flask

Jogo da Velha desenvolvido com Python (Flask) no backend e HTML, CSS e JavaScript no frontend. O jogador escolhe seu símbolo na página inicial e é redirecionado para o tabuleiro, onde enfrenta o computador.

## 📋 Funcionalidades

- Página inicial para escolha do símbolo (**X** ou **O**)
- Redirecionamento automático para a página do jogo após a escolha
- Computador joga automaticamente em uma casa aleatória
- Detecta **vitória** (horizontal, vertical e diagonal)
- Detecta **empate** quando todas as casas são preenchidas
- Pergunta se deseja **jogar novamente** ao fim de cada partida
- Computador começa automaticamente quando jogador escolhe **O**

## 🗂️ Estrutura do Projeto

```
jogo-da-velha/
├── app.py
├── requirements.txt
└── templates/
    ├── inicio.html
    └── jogo.html
```

## 🚀 Como Rodar

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/jogo-da-velha.git
cd jogo-da-velha
```

**2. Instale as dependências:**
```bash
pip install flask
```

**3. Rode o servidor:**
```bash
python app.py
```

**4. Acesse no navegador:**
```
http://127.0.0.1:5000
```

## 🕹️ Como Jogar

1. Acesse a página inicial e escolha seu símbolo: **X** ou **O**
2. Clique nas casas do tabuleiro para fazer sua jogada
3. O computador jogará automaticamente após sua jogada
4. Ao fim do jogo, confirme se deseja jogar novamente

## 🏆 Condições de Vitória

O jogo possui **8 combinações vencedoras**:

| Tipo | Combinações |
|------|-------------|
| Linhas | Superior, meio, inferior |
| Colunas | Esquerda, centro, direita |
| Diagonais | ↘ e ↙ |

## 🛠️ Tecnologias Utilizadas

- **Python 3** — backend
- **Flask** — servidor web
- **HTML5** — estrutura das páginas
- **CSS3** — estilização do tabuleiro
- **JavaScript** — lógica do jogo no frontend

## 👨‍💻 Autor

Feito por **Matheus Cunha**  
SENAI — Desenvolvimento de Sistemas
