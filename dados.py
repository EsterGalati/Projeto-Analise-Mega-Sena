import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# Função para limpar e converter valores monetários
def clean_currency(value):
    if isinstance(value, str):
        return float(value.replace("R$", "").replace(".", "").replace(",", "."))
    return value


# Carregar o arquivo Excel
file_path = "Mega-Sena.xlsx"  # Atualize o caminho do arquivo conforme necessário
mega_sena_data = pd.read_excel(file_path)

# Converter 'Data do Sorteio' para datetime
mega_sena_data["Data do Sorteio"] = pd.to_datetime(
    mega_sena_data["Data do Sorteio"], dayfirst=True
)

# Converter colunas de 'Bola' para inteiros
bola_columns = ["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]
mega_sena_data[bola_columns] = mega_sena_data[bola_columns].astype(int)

# Análise 1: Números mais sorteados
bola_counts = (
    mega_sena_data[bola_columns]
    .melt(var_name="Bola", value_name="Número")["Número"]
    .value_counts()
    .sort_index()
)

# Análise 2: Evolução dos valores acumulados ao longo do tempo
mega_sena_data["Acumulado 6 acertos"] = mega_sena_data["Acumulado 6 acertos"].replace(
    {"R\$0,00": "R$ 0,00"}
)
mega_sena_data["Acumulado 6 acertos"] = mega_sena_data["Acumulado 6 acertos"].apply(
    clean_currency
)

# Análise 3: Frequência de concursos sem ganhadores
mega_sena_data["Sem Ganhadores"] = mega_sena_data["Ganhadores 6 acertos"] == 0
sem_ganhadores_frequencia = mega_sena_data["Sem Ganhadores"].mean() * 100

# Análise 4: Distribuição dos prêmios por estado (apenas os principais)
estado_counts = (
    mega_sena_data["Cidade / UF"].dropna().str.split("; ").explode().value_counts()
)
estado_counts = estado_counts[
    estado_counts > 5
]  # Filtrar estados com mais de 5 prêmios

# Análise 5: Quantidade de ganhadores por faixa de prêmio
ganhadores_faixa = mega_sena_data[
    ["Ganhadores 6 acertos", "Ganhadores 5 acertos", "Ganhadores 4 acertos"]
].sum()

# Análise 6: Correlação entre os números sorteados
correlation_matrix = mega_sena_data[bola_columns].corr()

# Análise 7: Média de números sorteados por concurso
media_numeros = mega_sena_data[bola_columns].mean()

# Análise 8: Distribuição dos valores dos prêmios de 6 acertos ao longo do tempo
mega_sena_data["Rateio 6 acertos"] = mega_sena_data["Rateio 6 acertos"].replace(
    {"R\$0,00": "R$ 0,00"}
)
mega_sena_data["Rateio 6 acertos"] = mega_sena_data["Rateio 6 acertos"].apply(
    clean_currency
)

# Análise 9: Análise de tendência dos prêmios acumulados
tendencia_acumulado = (
    mega_sena_data[["Data do Sorteio", "Acumulado 6 acertos"]]
    .set_index("Data do Sorteio")
    .resample("Y")
    .mean()
)


# Função para plotar gráficos individualmente
def plot_graphs():
    plt.figure(figsize=(10, 6))
    bola_counts.plot(kind="bar", color="skyblue")
    plt.title("Números mais sorteados")
    plt.xlabel("Número")
    plt.ylabel("Frequência")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(
        mega_sena_data["Data do Sorteio"],
        mega_sena_data["Acumulado 6 acertos"],
        color="green",
    )
    plt.title("Evolução dos valores acumulados ao longo do tempo")
    plt.xlabel("Data do Sorteio")
    plt.ylabel("Valor Acumulado (R$)")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(
        ["Sem Ganhadores", "Com Ganhadores"],
        [sem_ganhadores_frequencia, 100 - sem_ganhadores_frequencia],
        color=["red", "blue"],
    )
    plt.title("Frequência de concursos sem ganhadores")
    plt.ylabel("Percentual (%)")
    plt.show()

    plt.figure(figsize=(10, 6))
    estado_counts.plot(kind="bar", color="purple")
    plt.title("Distribuição dos prêmios por estado (principais)")
    plt.xlabel("Estado")
    plt.ylabel("Quantidade de prêmios")
    plt.show()

    plt.figure(figsize=(10, 6))
    ganhadores_faixa.plot(kind="bar", color="orange")
    plt.title("Quantidade de ganhadores por faixa de prêmio")
    plt.xlabel("Faixa de prêmio")
    plt.ylabel("Quantidade de ganhadores")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="none")
    plt.colorbar(label="Correlação")
    plt.title("Correlação entre os números sorteados")
    plt.xticks(range(len(bola_columns)), bola_columns, rotation=45)
    plt.yticks(range(len(bola_columns)), bola_columns)
    plt.show()

    plt.figure(figsize=(10, 6))
    media_numeros.plot(kind="bar", color="cyan")
    plt.title("Média de números sorteados por concurso")
    plt.xlabel("Número")
    plt.ylabel("Média")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(
        mega_sena_data["Data do Sorteio"],
        mega_sena_data["Rateio 6 acertos"],
        color="magenta",
    )
    plt.title("Distribuição dos valores dos prêmios de 6 acertos ao longo do tempo")
    plt.xlabel("Data do Sorteio")
    plt.ylabel("Valor do Prêmio (R$)")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(
        tendencia_acumulado.index,
        tendencia_acumulado["Acumulado 6 acertos"],
        color="brown",
    )
    plt.title("Análise de tendência dos prêmios acumulados")
    plt.xlabel("Ano")
    plt.ylabel("Média Acumulada (R$)")
    plt.show()


# Plotar os gráficos
plot_graphs()

# Mostrar as estatísticas
print(f"Números mais sorteados:\n{bola_counts.head()}\n")
print(f"Frequência de concursos sem ganhadores: {sem_ganhadores_frequencia:.2f}%")
print(f"Distribuição dos prêmios por estado:\n{estado_counts}\n")
print(f"Quantidade de ganhadores por faixa de prêmio:\n{ganhadores_faixa}\n")
print(f"Correlação entre os números sorteados:\n{correlation_matrix}\n")
print(f"Média de números sorteados por concurso:\n{media_numeros}\n")
print(f"Tendência dos prêmios acumulados ao longo dos anos:\n{tendencia_acumulado}\n")

# Perguntar ao usuário se deseja exportar os resultados em PDF
export_pdf = (
    input("Deseja exportar os resultados das análises em PDF? (sim/não): ")
    .strip()
    .lower()
)

if export_pdf == "sim":
    with PdfPages("Mega_Sena_Analises.pdf") as pdf:
        plt.figure(figsize=(10, 6))
        bola_counts.plot(kind="bar", color="skyblue")
        plt.title("Números mais sorteados")
        plt.xlabel("Número")
        plt.ylabel("Frequência")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.plot(
            mega_sena_data["Data do Sorteio"],
            mega_sena_data["Acumulado 6 acertos"],
            color="green",
        )
        plt.title("Evolução dos valores acumulados ao longo do tempo")
        plt.xlabel("Data do Sorteio")
        plt.ylabel("Valor Acumulado (R$)")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.bar(
            ["Sem Ganhadores", "Com Ganhadores"],
            [sem_ganhadores_frequencia, 100 - sem_ganhadores_frequencia],
            color=["red", "blue"],
        )
        plt.title("Frequência de concursos sem ganhadores")
        plt.ylabel("Percentual (%)")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        estado_counts.plot(kind="bar", color="purple")
        plt.title("Distribuição dos prêmios por estado (principais)")
        plt.xlabel("Estado")
        plt.ylabel("Quantidade de prêmios")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        ganhadores_faixa.plot(kind="bar", color="orange")
        plt.title("Quantidade de ganhadores por faixa de prêmio")
        plt.xlabel("Faixa de prêmio")
        plt.ylabel("Quantidade de ganhadores")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="none")
        plt.colorbar(label="Correlação")
        plt.title("Correlação entre os números sorteados")
        plt.xticks(range(len(bola_columns)), bola_columns, rotation=45)
        plt.yticks(range(len(bola_columns)), bola_columns)
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        media_numeros.plot(kind="bar", color="cyan")
        plt.title("Média de números sorteados por concurso")
        plt.xlabel("Número")
        plt.ylabel("Média")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.plot(
            mega_sena_data["Data do Sorteio"],
            mega_sena_data["Rateio 6 acertos"],
            color="magenta",
        )
        plt.title("Distribuição dos valores dos prêmios de 6 acertos ao longo do tempo")
        plt.xlabel("Data do Sorteio")
        plt.ylabel("Valor do Prêmio (R$)")
        pdf.savefig()
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.plot(
            tendencia_acumulado.index,
            tendencia_acumulado["Acumulado 6 acertos"],
            color="brown",
        )
        plt.title("Análise de tendência dos prêmios acumulados")
        plt.xlabel("Ano")
        plt.ylabel("Média Acumulada (R$)")
        pdf.savefig()
        plt.close()

    print("Resultados exportados para 'Mega_Sena_Analises.pdf'")
