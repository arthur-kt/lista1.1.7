"""
Lista 1, parte 1, exercício 7

Descrição: Este programa apresenta a resolução de uma questão da lista 1 da cadeira de Economia Computacional
Autor:Arthur Kafrouni Tomazi
Data: 23/06/2023
Versão: 0.0.1
"""

# Atribuição de variáveis

n = 0
pg_0 = 0
pg_n = 0
q = 0
soma_pg = 0

# Entrada de dados

n = float(input("Quantidade de termos (n): "))
pg_0 = float(input("Primeiro termo: "))
q = float(input("Razão: "))

# Processamento de dados

pg_n = pg_0 * (q**(n-1))
soma_pg = (pg_0*((q**n)-1))/(q-1)

# Saída de dados

print(f'A progressão geométrica que contém {n} termos, começando pelo termo {pg_0} e de razão {q}, resulta no termo final {pg_n} e a soma de seus termos é {soma_pg}')