# Análise e Síntese de Algoritmos (ASA) - 2025/2026

Repositório contendo os projetos desenvolvidos para a unidade curricular de **Análise e Síntese de Algoritmos (ASA)** no Instituto Superior Técnico (IST), ano letivo 2025/2026.

---

## 📁 Estrutura do Repositório

```text
ASA/
├── Makefile                # Makefile principal para gerir todos os projetos
├── .gitignore              # Ficheiro para ignorar artefactos no Git
├── README.md               # Documentação geral do repositório
├── P1/                     # Projeto 1 - Enovelamento de Cadeia Proteica (DP)
│   ├── Makefile
│   ├── protein_chain.cpp
│   └── AL030 Relatório P1.pdf
├── P2/                     # Projeto 2 - Atribuição de Rotas de Entregas (Grafos / DAG)
│   ├── Makefile
│   ├── deliveriesCaracol.cpp
│   ├── graphic.py
│   └── AL030 Relatório P2.pdf
└── P3/                     # Projeto 3 - Análise de Campeonatos (Programação Linear)
    ├── Makefile
    ├── SnailSoft.py
    ├── plot_results.py
    └── AL030 Relatório P3.pdf
```

---

## 🚀 Como Compilar e Executar

Um `Makefile` na raiz do repositório permite compilar, testar ou limpar todos os projetos em simultâneo ou individualmente em cada pasta.

### Comandos Principais (na Raiz)

- **Compilar todos os projetos:**
  ```bash
  make
  ```
- **Recompilar do zero:**
  ```bash
  make rebuild
  ```
- **Executar testes:**
  ```bash
  make test
  ```
- **Limpar artefactos de compilação:**
  ```bash
  make clean
  ```
- **Limpar ficheiros temporários do editor:**
  ```bash
  make distclean
  ```

---

## 🧬 Projeto 1 (P1): Enovelamento de Cadeia Proteica

### Descrição
Cálculo da energia máxima de afinidade no enovelamento de uma cadeia proteica e reconstrução da sequência de dobragens lexicograficamente menor.

- **Abordagem:** Programação Dinâmica ($O(N^3)$) baseada no problema de multiplicação de matrizes em cadeia (parentetização) com reconstrução memoizada.
- **Linguagem:** C++17
- **Ficheiro principal:** [`P1/protein_chain.cpp`](file:///home/leonorguedes/Documentos/VS/ASA/P1/protein_chain.cpp)

### Execução Individual
```bash
cd P1
make
./protein_chain < input.txt
```

---

## 🚚 Projeto 2 (P2): Atribuição de Rotas de Entregas em Grafos (DAG)

### Descrição
Contagem eficiente do número de caminhos distintos entre interseções num Grafo Dirigido Acíclico (DAG) para determinar qual o camião atribuído a cada entrega da empresa *Entregas Caracol Lda.*

- **Atribuição:** $\text{Camiao}(A, B) = 1 + (\#\text{caminhos}(A, B) \pmod M)$
- **Abordagem:** Ordenação Topológica (Algoritmo de Kahn) e Programação Dinâmica em DAG.
- **Linguagem:** C++17
- **Ficheiro principal:** [`P2/deliveriesCaracol.cpp`](file:///home/leonorguedes/Documentos/VS/ASA/P2/deliveriesCaracol.cpp)

### Execução Individual
```bash
cd P2
make
./deliveriesCaracol < input.txt
```

---

## ⚽ Projeto 3 (P3): Análise de Campeonatos com Programação Linear

### Descrição
Determinação, para cada equipa num campeonato por pontos com duas voltas, do **menor número de vitórias que ainda precisa de obter** para ser possível vencer o campeonato (assumindo cenários favoráveis e critérios de desempate).

- **Abordagem:** Modelação através de problemas de Programação Linear (PL) resolvidos com o solver PuLP.
- **Linguagem:** Python 3 (requer biblioteca `pulp`)
- **Ficheiro principal:** [`P3/SnailSoft.py`](file:///home/leonorguedes/Documentos/VS/ASA/P3/SnailSoft.py)

### Requisitos e Execução Individual
```bash
# Instalação do PuLP
pip install pulp

cd P3
make
python3 SnailSoft.py < input.txt
```
