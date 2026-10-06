#!/usr/bin/env python3
import subprocess
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def generate_dag(n, edge_ratio=0.3):
    """Gera um DAG (Directed Acyclic Graph) com n nós"""
    edges = []
    seen = set()
    
    # Gerar arestas garantindo que é um DAG (só conecta i -> j onde i < j)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if random.random() < edge_ratio:
                edge = (i, j)
                if edge not in seen:
                    edges.append(edge)
                    seen.add(edge)
    
    return edges

def create_test_instance(n, m, m1, m2):
    """Cria uma instância de teste"""
    edges = generate_dag(n)
    k = len(edges)
    
    lines = [f"{n} {m} {m1} {m2} {k}"]
    for a, b in edges:
        lines.append(f"{a} {b}")
    
    return "\n".join(lines) + "\n", k

def run_program(input_data):
    """Executa o programa compilado e mede o tempo"""
    try:
        start = time.time()
        result = subprocess.run(
            ["./a.out"],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=30
        )
        end = time.time()
        
        if result.returncode == 0:
            return end - start
        else:
            return None
    except subprocess.TimeoutExpired:
        return None
    except FileNotFoundError:
        print("Erro: ficheiro a.out não encontrado. Compile o programa primeiro com: g++ deliveriesCaracol.cpp")
        return None

def main():
    # Verificar se o programa está compilado
    if not Path("a.out").exists():
        print("Compilando o programa...")
        subprocess.run(["g++", "-O2", "deliveriesCaracol.cpp"])
    
    # Configuração das instâncias de teste
    test_sizes = [
        100, 200, 400, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000
    ]
    
    results = []
    
    print("=" * 70)
    print("AVALIAÇÃO EXPERIMENTAL DA SOLUÇÃO")
    print("=" * 70)
    print(f"{'N (nós)':<10} {'K (arestas)':<12} {'f(N,K)':<15} {'Tempo (s)':<12}")
    print("-" * 70)
    
    for n in test_sizes:
        # Gerar instância
        M = 1000000007  # Número primo grande
        m1 = 1
        m2 = min(10, n)
        
        input_data, k = create_test_instance(n, M, m1, m2)
        
        # Executar múltiplas vezes e tirar a média
        times = []
        for _ in range(3):  # 3 execuções para média
            t = run_program(input_data)
            if t is not None:
                times.append(t)
        
        if times:
            avg_time = sum(times) / len(times)
            # Complexidade teórica: O(N * (N + K))
            complexity = n * (n + k)
            results.append({
                'n': n,
                'k': k,
                'complexity': complexity,
                'time': avg_time
            })
            print(f"{n:<10} {k:<12} {complexity:<15} {avg_time:<12.6f}")
        else:
            print(f"{n:<10} {'ERRO':<12}")
    
    print("=" * 70)
    
    if not results:
        print("Nenhum resultado válido obtido!")
        return
    
    # Criar gráfico
    complexities = [r['complexity'] for r in results]
    times = [r['time'] for r in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(complexities, times, 'b-o', linewidth=2, markersize=6, label='Tempo medido')
    
    # Adicionar linha de tendência linear
    z = np.polyfit(complexities, times, 1)
    p = np.poly1d(z)
    plt.plot(complexities, p(complexities), "r--", alpha=0.8, label='Tendência linear')
    
    plt.xlabel('f(n,m) = N × (N + K)', fontsize=12)
    plt.ylabel('Tempo (s)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Formato científico para eixo X se necessário
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    
    plt.tight_layout()
    plt.savefig('benchmark_results.png', dpi=300)
    print("\nGráfico salvo em: benchmark_results.png")
    plt.show()
    
    # Salvar resultados em arquivo
    with open('benchmark_results.txt', 'w') as f:
        f.write("RESULTADOS DA AVALIAÇÃO EXPERIMENTAL\n")
        f.write("=" * 70 + "\n")
        f.write(f"{'N (nós)':<10} {'K (arestas)':<12} {'f(N,K)':<15} {'Tempo (s)':<12}\n")
        f.write("-" * 70 + "\n")
        for r in results:
            f.write(f"{r['n']:<10} {r['k']:<12} {r['complexity']:<15} {r['time']:<12.6f}\n")
        f.write("=" * 70 + "\n")
        f.write(f"\nComplexidade teórica: O(N × (N + K))\n")
        f.write(f"Coeficiente angular da regressão linear: {z[0]:.2e}\n")
    
    print("Resultados salvos em: benchmark_results.txt")

if __name__ == "__main__":
    main()
