# Angry Birds Space

Jogo estilo "Angry Birds no espaço" desenvolvido para o curso de Álgebra Linear. O jogo utiliza conceitos de vetores, física gravitacional e movimento para criar uma experiência interativa.

## Como Jogar

1. **Iniciar o jogo**: Execute o programa e pressione `ESPAÇO` no menu inicial
2. **Ajustar mira**: Mova o mouse para apontar o canhão na direção desejada
3. **Disparar**: Clique e arraste o mouse para ajustar a potência do disparo, depois solte para disparar
4. **Objetivo**: Acerte o alvo vermelho em cada nível
5. **Power-ups**: Colete as estrelas douradas para ganhar projéteis extras
6. **Física**: Os projéteis são afetados pela gravidade dos planetas e buracos negros

## Como Executar

### Execução Direta (Mais Simples)

1. Navegue até o diretório do projeto:
```bash
cd angry_birds_space
```

2. Instale as dependências (se ainda não instalou):
```bash
pip install -r requirements.txt
```

3. Execute o jogo:
```bash
python main.py
```

Ou, a partir da raiz do projeto:
```bash
python run_game.py
```

### Instalação via pip (Para Distribuição)

```bash
pip install git+https://github.com/seu-usuario/angry-birds-space.git
```

Depois de instalar, execute:

```bash
angry-birds-space
```

### Instalação Local como Pacote

1. Clone ou baixe o repositório:
```bash
git clone https://github.com/seu-usuario/angry-birds-space.git
cd angry-birds-space
```

2. Instale as dependências:
```bash
pip install -r angry_birds_space/requirements.txt
```

3. Instale o pacote:
```bash
pip install ./angry_birds_space
```

4. Execute o jogo:
```bash
angry-birds-space
```

Ou execute como módulo:
```bash
python -m angry_birds_space.main
```

## Requisitos

- Python 3.11 ou superior
- pygame >= 2.6.0
- numpy >= 1.24.0

## Características do Jogo

### Sistema de Níveis

O jogo possui 3 níveis com dificuldade crescente:

**Nível 1 - Fácil:**
- 1 planeta
- 1 power-up (estrela dourada)
- Alvo no canto superior direito

**Nível 2 - Médio:**
- 2 planetas
- 1 power-up em posição mais difícil
- Alvo em posição mais desafiadora

**Nível 3 - Difícil:**
- 3 planetas
- 2 buracos negros (atração muito forte)
- Alvo em posição muito difícil

### Física Implementada

1. **Movimento Uniforme Inicial**: Os projéteis começam com uma velocidade inicial definida pela direção e potência do disparo
2. **Atração Gravitacional**: Planetas e buracos negros exercem força gravitacional sobre os projéteis, desviando suas trajetórias
3. **Resistência do Ar**: Pequena resistência aplicada aos projéteis para simular atrito
4. **Colisões**: Projéteis são desativados ao colidir com corpos celestes, buracos negros ou ao sair da tela

### Elementos do Jogo

- **Planetas**: Corpos celestes que exercem atração gravitacional moderada
- **Buracos Negros**: Exercem atração gravitacional muito forte, com animação de anel de acréscimo
- **Power-ups**: Estrelas douradas que, ao serem coletadas, adicionam +1 projétil ao limite máximo
- **Alvo**: Objeto vermelho que deve ser acertado para completar o nível

### Elementos Visuais

- **Estrelas de fundo**: Ambiente espacial imersivo
- **Rastro dos projéteis**: Visualização da trajetória
- **Efeito de brilho nos planetas**: Destaque visual para os corpos celestes
- **Animações**: Power-ups pulsantes e buracos negros com anel rotativo
- **Menu inicial**: Interface amigável para começar o jogo
- **Transições entre níveis**: Tela de "Nível Completo" entre fases

### Controles

- **Mouse**: Apontar canhão e ajustar potência do disparo
- **ESPAÇO**: Iniciar jogo (no menu)
- **R**: Reiniciar (após vitória ou nível completo)
- **ESC**: Voltar ao menu (durante o jogo) ou pular transição de nível

## Matemática por Trás do Jogo

### Vetores

O jogo utiliza vetores do NumPy para representar:
- **Posição**: `s = [x, y]`
- **Velocidade**: `v = [vx, vy]`
- **Aceleração**: `a = [ax, ay]`

### Movimento Uniformemente Variado

A física do jogo segue as equações:

**Atualização de velocidade:**
```
v_n = v_{n-1} + a * dt
```

**Atualização de posição:**
```
s_n = s_{n-1} + v_{n-1} * dt + 0.5 * a * dt²
```

### Força Gravitacional

A aceleração gravitacional é calculada como:

```
a = (G * M / r²) * (r̂)
```

Onde:
- `G`: Constante gravitacional (ajustada para o jogo)
- `M`: Massa do corpo celeste
- `r`: Distância entre o projétil e o corpo celeste
- `r̂`: Vetor unitário na direção do corpo celeste

A aceleração total sobre um projétil é a soma vetorial de todas as forças gravitacionais:

```
a_total = Σ a_i
```

### Normalização de Vetores

Para calcular a direção unitária:
```
r̂ = r / |r|
```

Onde `|r|` é o módulo (norma) do vetor:
```
|r| = √(r_x² + r_y²)
```

## Estrutura do Projeto

```
angry_birds_space/
├── __init__.py          # Inicialização do pacote
├── main.py              # Ponto de entrada
├── game.py              # Classe principal do jogo
├── game_objects.py      # Objetos do jogo (Projétil, Canhão, Power-up, Buraco Negro, etc.)
├── physics.py           # Motor de física
├── setup.py             # Configuração para instalação
├── requirements.txt     # Dependências
└── README.md            # Este arquivo
```

## Objetivos Educacionais

Este projeto demonstra:
- Uso de vetores em programação (NumPy arrays)
- Operações vetoriais (soma, multiplicação por escalar, normalização)
- Cálculo de módulo e direção de vetores
- Aplicação de física em jogos digitais
- Integração de conceitos matemáticos em projetos práticos

## Solução de Problemas

**O jogo não inicia:**
- Verifique se todas as dependências estão instaladas: `pip install -r requirements.txt`
- Certifique-se de estar usando Python 3.11 ou superior

**Performance lenta:**
- Reduza o número de projéteis ativos simultaneamente
- Ajuste o FPS no código se necessário

**Projéteis não aparecem:**
- Verifique se você está clicando e arrastando o mouse corretamente
- Certifique-se de que não excedeu o limite de projéteis ativos

## Licença

Este projeto foi desenvolvido para fins educacionais no curso de Álgebra Linear.

## Autores

Grupo de Álgebra Linear - Insper

## Vídeo Explicativo

[Link para o vídeo explicativo será adicionado aqui]

O vídeo explica:
- A matemática por trás do jogo (vetores, física)
- Como funciona o modelo físico implementado
- Demonstração do gameplay
- Identidade visual do jogo
- Sistema de níveis e power-ups
