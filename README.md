# analiza-bancara — starter

Cele două proiecte ale tale, `banking-transaction-analysis` și `bank-customer-analysis`, într-unul singur. Problemele sunt în `resurse/exercitii-analiza-bancara.pdf`, teoria în `resurse/teorie-analiza-bancara.pdf`. Cele 17 funcții din fișă sunt în `analiza.py`, în ordinea ei, pe 3 niveluri, cu semnăturile tipate și corpul `pass`: la clasă (`client_nou` … `total_pe`), de exersat (`clienti_dupa_id` … `clienti_fara_tranzactii`), provocări (`segment` … `raport`). Înlocuiești `pass` cu codul problemei, îi adaugi numele în `import`-ul din `main.py` și o apelezi din `main()`.

Datele: `clienti.csv` (10 clienți) și `tranzactii.csv` (30 de tranzacții). O tranzacție nu mai are numele și orașul clientului, doar `client_id` — numele și orașul se află din `clienti.csv`.

**Windows (terminalul din VS Code)**
```
py -3 -m venv .venv
.venv\Scripts\activate
```

```
python main.py
```

Verificare: `where python` arată `.venv`; până completezi `citeste_tranzactii`, `main.py` afișează `None` — de ce?
