
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/ValentinIon89/delta-architecture-linguistics/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/ValentinIon89/delta-architecture-linguistics/tree/main)


# Arhitectura operatorială Δ a transformării gramaticale

Acest material conține un prototip demonstrativ în Python, cu exemple inspirate de articolul „The Δ Architecture of Grammatical Transformation” (Ion Valentin Ciocioc, 2026) și de anexele A și B.

## Scop și limite

Scriptul redă manual exemple prestabilite pentru cele opt regimuri Δ. Este un material didactic, nu o implementare oficială a cadrului și nu un clasificator automat al datelor lingvistice.

În reprezentarea din program, R₀ este păstrat ca identificator relațional abstract, separat de baza de suprafață folosită pentru afișarea formelor. Segmentarea, poziția componentelor și efectul semantic sunt furnizate explicit în exemple; programul nu le deduce din forme și nu implementează diagnosticul complet pentru păstrarea sau înlocuirea lui R₀.

Δ(→) redă corespondența orientată dintre configurații, fără să clasifice intervenția asupra materialului intern. Δ(><) este ilustrat prin *trust → distrust* și *urs → ursoaică*; efectul semantic sau gramatical este indicat manual, nu calculat. Integrarea formală a materialului poate fi descrisă separat prin Δ(+). Δ(±) clasifică domeniul paradigmatic ca întreg; relațiile locale dintre forme sunt afișate separat ca Δ(−/+) atunci când reprezintă înlocuirea materialului în aceeași poziție.

Pentru Δ(~), *la ~ al* este numai o ilustrație construită a permutării, iar *ask ~ aks* este exemplul englezesc atestat menționat în articol și în Appendix A. Afișarea permutării nu validează continuitatea empirică a lui R₀.

Rezultatele sunt reprezentări ilustrative ale exemplelor codificate. Ele nu validează empiric cadrul și nu înlocuiesc procedura analitică din articol și anexe.

## Regimurile ilustrate

1. **Δ(→), corespondență direcțională** — *zi → zile*.
2. **Δ(+), integrare** — *merg → mergeam*.
3. **Δ(><), reorientare semantică sau gramaticală** — *trust → distrust* și *urs → ursoaică*.
4. **Δ(−/+), înlocuire corelată** — *casă → case*.
5. **Δ(>/<), cuplare relațională** — *ο άντρας*.
6. **Δ(−), eliminare** — *αγελάδα → γελάδα*.
7. **Δ(~), reorganizare pozițională** — permutarea construită *la ~ al* și alternanța atestată *ask ~ aks*.
8. **Δ(±), organizare paradigmatică cumulativă** — paradigma greacă *γράφω, γράφεις, γράφει, γράφουμε, γράφετε, γράφουν*.

## Rulare

Este suficient Python 3. Culorile din terminal sunt opționale și folosesc `colorama` dacă pachetul este instalat.

```bash
python delta_architecture.py
```
