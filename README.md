# IFutHeads
iFutHead é um jogo arcade de futebol inspirado no Soccer Heads, com partidas rápidas e diretas. O jogador controla personagens cabeçudos em duelos 1x1, focando em movimentação e chutes precisos para marcar gols. Simples, competitivo e ideal para diversão rápida

# Integrantes 
* Anthony Rafael Ferreira da Silva
* Rafael Araújo Brito

# ⚽ IFutHeads

*Um jogo arcade de futebol de cabeça inspirado em Soccer Heads*

## 1. 🎮 Descrição Geral

O **IFutHeads** é um jogo do tipo **arcade esportivo**, inspirado em jogos como Soccer Heads.

* **Tipo de jogo:** Arcade / Esporte
* **Ambiente:** Campo de futebol 2D
* **Ideia principal:** Um jogador enfrenta uma IA em partidas de futebol com personagens de cabeça grande, focando em marcar gols usando movimentação, pulos e chutes.

## 2. 🥅 Objetivo do Jogo

O objetivo do jogador é:

* Marcar mais gols que a IA dentro do tempo da partida
* Defender seu próprio gol
* Utilizar movimentação, pulos e chutes para controlar a bola

**Meta principal:** vencer a partida com mais gols.

## 3. 🧍 Personagem Principal

* Um jogador controlado pelo usuário
* Movimentação:

  * Andar para esquerda e direita
  * Pular
  * Chutar a bola

**Atributos:**

* Velocidade
* Força do pulo
* Força do chute
* Pontuação (gols marcados)

## 4. 👾 Inimigos e Obstáculos

* Oponente controlado por IA
* Obstáculos opcionais no mapa (versões futuras)

**Comportamento:**

* IA se movimenta automaticamente
* IA segue a bola e tenta marcar gols

**Colisão:**

* Ao colidir com a bola → ela é impulsionada
* Ao colidir com o adversário → ocorre bloqueio de movimento

## 5. 🗺️ Cenário (Mapa)

* Campo de futebol 2D simples
* Elementos:

  * Chão (limite inferior)
  * Gols (lado esquerdo e direito)
  * Limites laterais

**Posicionamento:**

* Jogador e IA começam em lados opostos
* Bola inicia no centro

## 6. ⭐ Sistema de Pontuação

* Gol marcado = **1 ponto**
* Placar exibido na tela

## 7. ❤️ Sistema de Vida

* Não há sistema de vidas tradicional
* O jogo funciona por **tempo ou número de gols**

(Ex: partida termina após 3 gols ou 60 segundos)

## 8. 🎮 Controles

**Jogador:**

* A → mover para esquerda
* D → mover para direita
* W → pular
* Espaço → chutar

**Outros:**

* ESC → sair do jogo

## 9. 🔄 Fluxo do Jogo

1. Tela inicial
2. Início da partida
3. Jogador enfrenta a IA
4. Disputa pela bola usando movimento, pulo e chute
5. Gol → reinicia posições
6. Jogo continua até atingir condição de vitória

**Vitória:** mais gols
**Derrota:** menos gols

## 10. 📜 Regras do Jogo

* Jogador não pode atravessar o chão
* Bola deve respeitar a física básica (gravidade e colisão)
* Gol só conta quando a bola entra completamente na área
* Não atravessar limites do mapa

## 11. 🗂️ Estrutura do Projeto

IF-Heads-Cup/

│

├── main.py

├── player.py

├── ball.py

├── enemy.py

├── game.py

├── settings.py

├── assets/

│   ├── imagens/

│   └── sons/

└── README.md

## 12. ⚙️ Funcionalidades Mínimas

Para a primeira versão, o jogo deve ter:

* Movimento do jogador
* Sistema de pulo
* Sistema de chute
* IA básica funcional
* Bola com física básica
* Sistema de gols
* Placar funcionando
* Tela de jogo rodando sem erros

## 13. 🚀 Melhorias Futuras

* Modo jogador vs jogador (multiplayer local)
* Inteligência artificial mais avançada
* Modos de jogo (campeonato)
* Personagens personalizados
* Efeitos visuais e sons
* Power-ups (velocidade, pulo alto, chute forte)
* Sistema de menu completo

## 14. 🖼️ Storyboard

* As imagens do Storyboard estão anexadas denro do repositório

## 15. Cronograma das próximas seis semanas

A ideia é ir evoluindo o jogo gradualmente, adicionando funcionalidades novas e corrigindo bugs conforme o projeto for andando.

# Semana 1 — Física do jogo

Nessa primeira semana o foco vai ser fazer a base do jogo funcionar direito. Melhorar:

* Movimento do player
* Pulo
* Gravidade
* Limites da tela
* Bola com física
* Colisão da bola com parede/chão/teto
* IA simples seguindo a bola
  
# Semana 2 — Colisões

Agora o foco vai ser melhorar a gameplay. Planejamos melhorar:

* Colisão do player com a bola
* Bola reagindo ao impacto
* IA batendo na bola
* Melhorar o quique da bola
* Corrigir bugs de colisão

# Semana 3 — Sistema de gol

Essa semana vai ser mais focada nas mecanicas principais do futebol. Devemos aprimorar/adcionar:

* Criar as traves
* Detectar quando for gol
* Reiniciar bola
* Reiniciar jogadores
* Fazer o placar

# Semana 4 — Interface

Aqui a ideia é deixar o jogo mais organizado visualmente. Fazer:

* Menu inicial
* Botão de jogar
* Mostrar tempo da partida
* Melhorar visual do placar

# Semana 5 — Melhorias visuais

Semana mais focada em aparência e detalhes.

* Melhorar sprites
* Melhorar o campo
* Adicionar sons simples
* Pequenas animações

# Semana 6 — Ajustes finais e organização

Na ultima semana a ideia vai ser mais corrigir e melhorar coisas que ainda estiverem incompletas ou com bug.

* Corrigir bugs restantes
* Melhorar algumas partes da gameplay
* Organizar melhor os arquivos
* Melhorar partes do código
* Atualizar GitHub
