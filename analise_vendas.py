import pandas as pd

# Criando o DataFrame
df = pd.DataFrame({
    "data": [
        "2024-01","2024-01","2024-01","2024-02","2024-02","2024-02",
        "2024-03","2024-03","2024-03","2024-04","2024-04","2024-04"
    ],
    "cidade": [
        "SP","RJ","MG","SP","RJ","MG",
        "SP","RJ","MG","SP","RJ","MG"
    ],
    "produto": [
        "A","A","A","B","B","B",
        "A","B","A","B","A","B"
    ],
    "canal": [
        "Online","Loja","Online","Loja","Online","Loja",
        "Online","Loja","Online","Loja","Online","Loja"
    ],
    "vendas": [
        120,200,150,300,250,180,
        400,100,350,500,450,320
    ]
})

# 1. Cidade com maior volume de vendas
cidade_maior = df.groupby("cidade")["vendas"].sum().idxmax()

# 2. Produto com maior média de vendas
produto_maior = df.groupby("produto")["vendas"].mean().idxmax()

# 3. Mês com maior volume de vendas
mes_maior = df.groupby("data")["vendas"].sum().idxmax()

# 4. Vendas acima de 300 ordenadas
vendas_altas = df.loc[df["vendas"] > 300].sort_values(by="vendas", ascending=False)

# 5. Canal com maior volume de vendas
canal_maior = df.groupby("canal")["vendas"].sum().idxmax()

# Exibindo resultados
print(f"Cidade com maior volume: {cidade_maior}")
print(f"Produto com maior média: {produto_maior}")
print(f"Mês com maior volume: {mes_maior}")
print(f"Canal com maior volume: {canal_maior}")
print("\nVendas acima de 300:\n", vendas_altas)




Adicionando análise de vendas com pandas
