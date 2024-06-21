import matplotlib.pyplot as plt


def plot_graph(
    choice,
    mega_sena_data,
    bola_counts,
    sem_ganhadores_frequencia,
    estado_counts,
    ganhadores_faixa,
    correlation_matrix,
    media_numeros,
    tendencia_acumulado,
):
    if choice == 1:
        plt.figure(figsize=(10, 6))
        bola_counts.plot(kind="bar", color="skyblue")
        plt.title("Números mais sorteados")
        plt.xlabel("Número")
        plt.ylabel("Frequência")
        plt.show()
    elif choice == 2:
        plt.figure(figsize=(10, 6))
        plt.plot(
            mega_sena_data["Data do Sorteio"],
            mega_sena_data["Acumulado 6 acertos"],
            color="green",
        )
        plt.title("Evolução dos valores acumulados ao longo do tempo")
        plt.xlabel("Data do Sorteio")
        plt.ylabel("Valor Acumulado (Milhões de R$)")
        plt.show()
    elif choice == 3:
        plt.figure(figsize=(10, 6))
        plt.bar(
            ["Sem Ganhadores", "Com Ganhadores"],
            [sem_ganhadores_frequencia, 100 - sem_ganhadores_frequencia],
            color=["red", "blue"],
        )
        plt.title("Frequência de concursos sem ganhadores")
        plt.ylabel("Percentual (%)")
        plt.show()
    elif choice == 4:
        plt.figure(figsize=(10, 6))
        estado_counts.plot(kind="bar", color="purple")
        plt.title("Distribuição dos prêmios por estado (principais)")
        plt.xlabel("Estado")
        plt.ylabel("Quantidade de prêmios")
        plt.show()
    elif choice == 5:
        plt.figure(figsize=(10, 6))
        ganhadores_faixa.plot(kind="bar", color="orange")
        plt.title("Quantidade de ganhadores por faixa de prêmio")
        plt.xlabel("Faixa de prêmio")
        plt.ylabel("Quantidade de ganhadores")
        plt.show()
    elif choice == 6:
        plt.figure(figsize=(10, 6))
        plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="none")
        plt.colorbar(label="Correlação")
        plt.title("Correlação entre os números sorteados")
        plt.xticks(
            range(len(correlation_matrix)), correlation_matrix.columns, rotation=45
        )
        plt.yticks(range(len(correlation_matrix)), correlation_matrix.index)
        plt.show()
    elif choice == 7:
        plt.figure(figsize=(10, 6))
        media_numeros.plot(kind="bar", color="cyan")
        plt.title("Média de números sorteados por concurso")
        plt.xlabel("Número")
        plt.ylabel("Média")
        plt.show()
    elif choice == 8:
        plt.figure(figsize=(10, 6))
        plt.plot(
            mega_sena_data["Data do Sorteio"],
            mega_sena_data["Rateio 6 acertos"],
            color="magenta",
        )
        plt.title("Distribuição dos valores dos prêmios de 6 acertos ao longo do tempo")
        plt.xlabel("Data do Sorteio")
        plt.ylabel("Valor do Prêmio (Milhões de R$)")
        plt.show()
    elif choice == 9:
        plt.figure(figsize=(10, 6))
        plt.plot(
            tendencia_acumulado.index,
            tendencia_acumulado["Acumulado 6 acertos"],
            color="brown",
        )
        plt.title("Análise de tendência dos prêmios acumulados")
        plt.xlabel("Ano")
        plt.ylabel("Média Acumulada (Milhões de R$)")
        plt.show()
    else:
        print("Escolha inválida. Tente novamente.")
