markdown
# Arhitectura Operatorială Δ a Transformării Gramaticale

Acest repository conține implementarea oficială în Python a cadrului teoretico-matematic descris în articolul științific **"The Δ Architecture of Grammatical Transformation"** (2026) scris de Ion Valentin Ciocioc.

## 📌 Despre Proiect
Sistemul transpune în cod software un operator abstract unic ($\Delta$) capabil să clasifice și să execute transformări lingvistice prin 8 regimuri distincte, asigurând stabilitatea nucleului relațional $R_0$. 

Este un cadru descriptiv-comparativ conceput pentru a modela structuri formale trans-lingvistice (aplicate pe limba română, engleză și greacă modernă).

## 🗂️ Structura și Regimurile Implementate
Codul din `delta_architecture.py` rulează următorii operatori structurali descriși în lucrare:
1. **Regimul Direcțional** $\Delta(\rightarrow)$ — Exemplu: *zi $\rightarrow$ zile*
2. **Regimul Aditiv** $\Delta(+)$ — Exemplu: *merg $\rightarrow$ mergeam*
3. **Redistribuirea Semantică Direcțională** $\Delta(\succ\prec)$ — Exemplu: *trust $\rightarrow$ distrust*
4. **Regimul Substituțional** $\Delta(-/+)$ — Exemplu: *casă $\rightarrow$ case*
5. **Cuplarea Relațională** $\Delta(\succ/\prec)$ — Exemplu: *ο άντρας* (articol / substantiv)
6. **Regimul Reductiv** $\Delta(-)$ — Exemplu: *αγελάδα $\rightarrow$ γελάδα*
7. **Reorganizarea Pozițională** $\Delta(\sim)$ — Permutări de inventar structural (*la $\rightarrow$ al*)
8. **Flexibilitatea Paradigmatică Cumulativă** $\Delta(\pm)$ — Matricea completă a flexiunii verbale

## 🚀 Ghid de Rulare Rapidă
Pentru a testa manual matricea de transformare direct în terminalul tău:

1. Instalați dependența cromatică:
   ```bash
   pip install colorama
   ```
2. Rulați executabilul Python:
   ```bash
   python delta_architecture.py
   ```