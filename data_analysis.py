import pandas as pd


def clean_currency(value):
    if isinstance(value, str):
        return float(value.replace("R$", "").replace(".", "").replace(",", ".")) / 1e6
    return value / 1e6


estado_map = {
    "AC": "AC",
    "AL": "AL",
    "AP": "AP",
    "AM": "AM",
    "BA": "BA",
    "CE": "CE",
    "DF": "DF",
    "ES": "ES",
    "GO": "GO",
    "MA": "MA",
    "MT": "MT",
    "MS": "MS",
    "MG": "MG",
    "PA": "PA",
    "PB": "PB",
    "PR": "PR",
    "PE": "PE",
    "PI": "PI",
    "RJ": "RJ",
    "RN": "RN",
    "RS": "RS",
    "RO": "RO",
    "RR": "RR",
    "SC": "SC",
    "SP": "SP",
    "SE": "SE",
    "TO": "TO",
    "SÃO PAULO": "SP",
    "SAO PAULO": "SP",
    "RIO DE JANEIRO": "RJ",
    "CURITIBA": "PR",
    "BRASÍLIA": "DF",
    "BRASILIA": "DF",
    "PORTO ALEGRE": "RS",
    "SALVADOR": "BA",
    "FORTALEZA": "CE",
    "BELO HORIZONTE": "MG",
    "RECIFE": "PE",
    "GOIÂNIA": "GO",
    "GOIANIA": "GO",
    "MANAUS": "AM",
    "JOÃO PESSOA": "PB",
    "JOAO PESSOA": "PB",
    "CAMPO GRANDE": "MS",
    "FLORIANÓPOLIS": "SC",
    "FLORIANOPOLIS": "SC",
    "VITÓRIA": "ES",
    "NATAL": "RN",
    "TERESINA": "PI",
    "MACAPÁ": "AP",
    "PALMAS": "TO",
}


def normalize_uf(location):
    if isinstance(location, str):
        location = location.strip().upper()
        parts = location.split("/")
        if len(parts) == 2:
            state = parts[1].strip()
            return estado_map.get(state, state)
        return estado_map.get(location, location)
    return location


def perform_analysis(file_path):
    mega_sena_data = pd.read_excel(file_path)

    mega_sena_data["Data do Sorteio"] = pd.to_datetime(
        mega_sena_data["Data do Sorteio"], dayfirst=True
    )

    bola_columns = ["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]
    mega_sena_data[bola_columns] = mega_sena_data[bola_columns].astype(int)

    bola_counts = (
        mega_sena_data[bola_columns]
        .melt(var_name="Bola", value_name="Número")["Número"]
        .value_counts()
        .sort_index()
    )

    mega_sena_data["Acumulado 6 acertos"] = mega_sena_data[
        "Acumulado 6 acertos"
    ].replace({"R\$0,00": "R$ 0,00"})
    mega_sena_data["Acumulado 6 acertos"] = mega_sena_data["Acumulado 6 acertos"].apply(
        clean_currency
    )

    mega_sena_data["Sem Ganhadores"] = mega_sena_data["Ganhadores 6 acertos"] == 0
    sem_ganhadores_frequencia = mega_sena_data["Sem Ganhadores"].mean() * 100

    mega_sena_data["UF"] = mega_sena_data["Cidade / UF"].apply(normalize_uf)

    estado_counts = mega_sena_data["UF"].dropna().value_counts()
    estado_counts = estado_counts[
        estado_counts > 5
    ]  

    ganhadores_faixa = mega_sena_data[
        ["Ganhadores 6 acertos", "Ganhadores 5 acertos", "Ganhadores 4 acertos"]
    ].sum()

    correlation_matrix = mega_sena_data[bola_columns].corr()

    media_numeros = mega_sena_data[bola_columns].mean()

    mega_sena_data["Rateio 6 acertos"] = mega_sena_data["Rateio 6 acertos"].replace(
        {"R\$0,00": "R$ 0,00"}
    )
    mega_sena_data["Rateio 6 acertos"] = mega_sena_data["Rateio 6 acertos"].apply(
        clean_currency
    )

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
