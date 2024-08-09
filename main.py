def exibir_filmes():
    filmes = {
        1: "Filme A",
        2: "Filme B",
        3: "Filme C",
        4: "Filme D",
        5: "Filme E"
    }
    print("Filmes disponíveis:")
    for numero, nome in filmes.items():
        print(f"{numero}. {nome}")
    return filmes

def escolher_filme(filmes):
    while True:
        try:
            escolha_filme = int(input("Escolha o número do filme (1-5): "))
            if escolha_filme < 1 or escolha_filme > 5:
                print("Número de filme inválido. Tente novamente.")
                continue
            return filmes[escolha_filme]
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def calcular_valor_assentos(quantidade_assentos):
    preco_por_assento = 15.0  # Valor do ingresso por assento
    return preco_por_assento * quantidade_assentos

def gerar_nota_fiscal(filme, assentos, valor_total, pagamento):
    nota = (
        f"--- NOTA FISCAL ---\n"
        f"Filme: {filme}\n"
        f"Assentos: {', '.join(map(str, assentos))}\n"
        f"Valor Total: R$ {valor_total:.2f}\n"
        f"Forma de Pagamento: {pagamento}\n"
        f"--------------------"
    )
    print(nota)

def escolher_assentos():
    while True:
        try:
            assentos = input("Digite os números dos assentos escolhidos (1-20), separados por vírgula: ")
            assentos = list(map(int, assentos.split(',')))
            assentos_validos = True
            assentos_ja_escolhidos = []
            for assento in assentos:
                if assento < 1 or assento > 20:
                    print("Número de assento inválido. Tente novamente.")
                    assentos_validos = False
                    break
                if assento in assentos_ja_escolhidos:
                    print("Você não pode escolher assentos duplicados. Tente novamente.")
                    assentos_validos = False
                    break
                assentos_ja_escolhidos.append(assento)
            if assentos_validos:
                return assentos
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def escolher_forma_pagamento():
    while True:
        pagamento = input("Escolha a forma de pagamento (Pix, dinheiro, cartão): ").strip().lower()
        if pagamento not in ['pix', 'dinheiro', 'cartão']:
            print("Forma de pagamento inválida. Tente novamente.")
            continue
        return pagamento.capitalize()

def main():
    filmes = exibir_filmes()
    filme_escolhido = escolher_filme(filmes)
    
    assentos = escolher_assentos()
    quantidade_assentos = len(assentos)
    valor_total = calcular_valor_assentos(quantidade_assentos)
    
    pagamento = escolher_forma_pagamento()
    
    gerar_nota_fiscal(filme_escolhido, assentos, valor_total, pagamento)
    print("Reserva concluída com sucesso!")

if __name__ == "__main__":
    main()
