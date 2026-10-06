# Delivery Route Assignment in Directed Acyclic Graphs

## Overview
This project addresses the problem of assigning delivery routes to trucks based on the number of distinct paths between distribution centers in a directed acyclic graph (DAG). 
It was developed as the 2nd project for the course **Analysis and Synthesis of Algorithms (2025/2026)** at Instituto Superior Técnico.

The company *Entregas Caracol Lda.* operates a fleet of trucks that perform deliveries between intersections in a geographic area. 
Each intersection is represented as a node, and each one-way road as a directed edge. Due to the absence of cycles, bridges, or tunnels, the road network forms a DAG.

For every possible delivery from point `A` to point `B`, the number of distinct paths between them determines which truck is assigned.

---

## Problem Definition

Given:
- A directed acyclic graph with `N` nodes (intersections).
- `M` trucks, numbered from `1` to `M`.
- A range of truck numbers `[m1, m2]`.
- A set of directed edges representing roads.

The truck assigned to a delivery from `A` to `B` is computed as:

Truck(A, B) = 1 + (#paths(A, B) mod M)


Only pairs `(A, B)` for which at least one path exists are considered.

---

## Input Format

The program reads from **standard input**:

1. An integer `N` (N ≥ 2): number of intersections.
2. An integer `M` (M ≥ 2): number of trucks.
3. Two integers `m1 m2`: range of truck numbers to output.
4. An integer `K` (K ≥ 1): number of directed roads.
5. `K` lines, each with two integers `ai bi`, representing a directed edge from `ai` to `bi`.

---

## Output Format

For each truck number `C` in the range `[m1, m2]`, output one line:

C<truck_number> A1,B1 A2,B2 ...


- Each `(A,B)` pair represents a delivery assigned to that truck.
- Pairs are ordered lexicographically.
- Pairs with no possible delivery paths are excluded.
- If a truck has no assigned routes, only `C<truck_number>` is printed.

---

## Implementation Notes

- The solution should efficiently count the number of paths between all valid `(A, B)` pairs in a DAG.
- Recursive solutions are discouraged due to stack limitations; iterative approaches are recommended.

---


### Compilation

```bash
g++ -std=c++11 -O3 -Wall deliveriesCaracol.cpp -lm

