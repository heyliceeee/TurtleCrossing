# 🐢 Turtle Crossing

Um mini‑jogo desenvolvido em **Python** com o módulo **Turtle Graphics**.  
O objetivo é simples: **ajudar a tartaruga a atravessar a estrada**, desviando‑se dos carros que passam a velocidades cada vez maiores.





---

## 🎯 Objetivo do Jogo  
Controlar a tartaruga até à linha de chegada, evitando colisões com os carros.  
A cada travessia bem‑sucedida:

- O **nível aumenta**
- A **velocidade dos carros cresce**
- A dificuldade torna‑se maior

---

## 🧠 Funcionalidades Principais  

- **Movimento do jogador** com a tecla **Up**  
- **Geração aleatória de carros** com cores e posições variadas  
- **Aumento progressivo da velocidade**  
- **Sistema de níveis** com atualização visual  
- **Deteção de colisões**  
- **Mensagem de Game Over**  
- Estrutura modular com classes separadas:
  - **CarManager**  
  - **Player**  
  - **Scoreboard**  

---

## 🧩 Descrição dos Componentes  

### 🚗 CarManager
Responsável por:
- Criar carros aleatórios  
- Controlar o movimento horizontal  
- Aumentar a velocidade a cada nível  

---

### 🐢 Player
A tartaruga controlada pelo utilizador:
- Começa sempre na posição inicial  
- Move‑se para cima com a tecla **Up**  
- Verifica se atingiu a linha de chegada  
- Regressa ao início após cada nível  

---

### 🧮 Scoreboard
Mostra:
- O nível atual  
- A mensagem de **Game Over**  
- Atualiza o texto sempre que o nível muda  

---


## 📚 Conceitos Praticados  

- Programação orientada a objetos (OOP)  
- Animação com `screen.tracer()`  
- Deteção de colisões  
- Geração aleatória  
- Modularização do código  
- Eventos de teclado com `onkey()`