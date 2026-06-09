# GlobalS_Python — OrbitWatch 🛰️

## Integrantes do Grupo

| Nome | RM |
|---|---|
| João Victor Pereira Gimenes | 571662 |
| Juan Duarte | 570331 |
| Julio Cesar da Silva Cocco | 569463 |
| Rafael Boletini de Oliveira | 570219 |
| Victor Rossi Sales Zanandre | 573844 |

---

## Sobre o Projeto

Hoje existem mais de 30 mil pedaços de lixo orbital catalogados girando ao redor da Terra a 28 mil km/h. Parafusos, restos de foguete, satélites mortos, fragmentos de colisões antigas. Cada nova colisão gera milhares de fragmentos novos — é o efeito Kessler, conceito real e citável: se a órbita baixa entrar em cascata, a humanidade perde GPS, internet por satélite, comunicação e previsão do tempo.

O **OrbitWatch** é uma plataforma de monitoramento que rastreia esses detritos, cruza com a órbita de satélites ativos (Starlink, ISS, satélites brasileiros como o Amazônia-1) e alerta operadoras quando o risco de colisão passa de um limite. O operador recebe o alerta antes do impacto e pode comandar manobra evasiva.

**ODS:** 9 (infraestrutura e inovação) como principal, 13 (sustentabilidade orbital) como complemento.

**Público-alvo:** Operadoras de satélite, agências espaciais (NASA, ESA, AEB brasileira), e indiretamente toda infraestrutura global que depende de órbita baixa.

---

## Como Funciona

```
1. Sistema recebe dados de detritos (Space-Track.org ou cadastro manual)
2. Calcula posição orbital de cada objeto usando propagação orbital
3. Compara distância entre detritos e satélites ativos
4. Quando distância < limiar configurado → dispara alerta de risco
5. Usuário visualiza gráfico e relatório gerado automaticamente
```

---

## Requisitos

- Python 3.12+
- Conta gratuita no [Space-Track.org](https://www.space-track.org) (para importar dados reais)

---

## Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/GlobalS_Python.git
cd GlobalS_Python
```

**2. Crie e ative um ambiente virtual:**
```bash
# Criar
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Mac/Linux)
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

---

## Como Usar

**Execute o programa pelo terminal:**
```bash
python main.py
```

O menu principal será exibido:

```
===== ORBITWATCH =====
1 -- Descrição do projeto
2 -- Cadastrar satélite/detrito
3 -- Listar objetos cadastrados
4 -- Calcular distância entre corpos
5 -- Simulação de trajetória
6 -- Deletar objeto
7 -- Importar dados reais (Space-Track)
0 -- Sair
```

### Opção 2 — Cadastrar objeto manualmente
Informe nome, tipo (satélite ou detrito), posição (X, Y, Z em km) e velocidade (X, Y, Z em km/s). O sistema valida automaticamente se a velocidade ultrapassa 11,2 km/s (velocidade de escape terrestre).

### Opção 3 — Listar objetos
Exibe todos os objetos cadastrados com paginação de 10 por vez. Use `s` para ver mais e `n` para voltar ao menu.

### Opção 4 — Calcular distância
Selecione dois objetos pelo número da lista. O sistema calcula a distância euclidiana 3D entre eles em km.

### Opção 5 — Simulação de trajetória
Selecione dois objetos, defina o tempo de simulação (em horas), o intervalo de verificação (em minutos) e o limiar de alerta (em km). O sistema propaga as órbitas e exibe alertas quando os objetos se aproximam. Ao final, é gerado um gráfico PNG salvo na pasta `relatorios/`.

### Opção 6 — Deletar objeto
Selecione o objeto pelo número e confirme a exclusão.

### Opção 7 — Importar dados reais
Faça login com suas credenciais do Space-Track.org e busque objetos pelo nome (ex: `ISS`, `HUBBLE`, `NOAA 19`). Use `~~` como coringa para buscas parciais (ex: `~~STARLINK`). O objeto encontrado pode ser salvo diretamente no sistema.

---

## Estrutura do Projeto

```
GlobalS_Python/
├── main.py                  # Ponto de entrada — menu principal
├── requirements.txt         # Dependências do projeto
│
├── modulos/
│   ├── __init__.py
│   ├── cadastro.py          # Cadastro manual de objetos
│   ├── listagem.py          # Listagem paginada
│   ├── distancia.py         # Cálculo de distância
│   ├── simulacao.py         # Simulação orbital e alertas
│   ├── deletar.py           # Exclusão de objetos
│   └── tle.py               # Integração com Space-Track
│
├── dados/
│   └── objetos.json         # Banco de dados local
│
└── relatorios/              # Gráficos PNG gerados
```

---

## Dependências

| Biblioteca | Uso |
|---|---|
| poliastro | Propagação orbital |
| astropy | Unidades físicas e tempo astronômico |
| numpy | Cálculos vetoriais |
| matplotlib | Geração de gráficos |
| requests | Integração com API Space-Track |
| sgp4 | Conversão de TLE em posição/velocidade |

---

## Observações

- A pasta `relatorios/` e o arquivo `dados/objetos.json` são gerados localmente e não são versionados
- Nunca compartilhe suas credenciais do Space-Track — não as coloque no código
- Objetos com velocidade acima de 11,2 km/s não estão em órbita terrestre e podem causar erros na simulação