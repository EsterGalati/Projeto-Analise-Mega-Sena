import pandas as pd


# Função para limpar e converter valores monetários
def clean_currency(value):
    if isinstance(value, str):
        return float(value.replace("R$", "").replace(".", "").replace(",", "."))
    return value


# Função para realizar a análise de dados
def perform_analysis(file_path):
    # Carregar o arquivo Excel
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
    mega_sena_data["Acumulado 6 acertos"] = mega_sena_data[
        "Acumulado 6 acertos"
    ].replace({"R\$0,00": "R$ 0,00"})
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
        .resample("YE")
        .mean()
    )

    return (
        mega_sena_data,
        bola_counts,
        sem_ganhadores_frequencia,
        estado_counts,
        ganhadores_faixa,
        correlation_matrix,
        media_numeros,
        tendencia_acumulado,
    )
