from colorama import Fore, Style, init
import random

# Inicializa o colorama para funcionar corretamente no Windows e outros sistemas
init(autoreset=True)

words_data = {
    "Jeans": "Palavra de origem inglesa incorporada ao português sem tradução. Refere-se a uma peça de vestuário comum...",
    "Rock": "Termo de origem inglesa utilizado para designar um gênero musical. Associado à liberdade de expressão.",
    "Look": "Significa olhar, aparência ou visual. Vem do inglês antigo 'lōcian'.",
    "Link": "Significa ligação, conexão ou elo. Vem do inglês antigo 'hlenc' (elo de corrente).",
    "Streaming": "Transmissão contínua de dados. Origem no termo 'stream' (fluxo/riacho).",
    "Selfie": "Registro de si mesmo. Do inglês antigo 'self' + sufixo casual 'ie'.",
    "Blush": "Do inglês 'to blush' (corar). Raiz no inglês antigo 'blyscan'.",
    "Gloss": "Do grego 'glōssa' para o inglês, significando brilho ou superfície brilhante.",
    "Folclore": "Junção de 'folk' (povo) e 'lore' (conhecimento).",
    "Lanche": "Adaptação brasileira do inglês 'lunch' (que lá significa almoço).",
    "Marketing": "Estratégias de mercado. Vem de 'market' (mercado).",
    "Delivery": "Serviço de entrega. Do inglês 'to deliver'.",
    "Hobby": "Deriva de 'hobyn' (cavalo pequeno). Atividade de lazer.",
    "Feedback": "Retorno de informação. Junção de 'feed' (alimentar) e 'back' (de volta).",
    "Trend": "Tendência. Do inglês antigo 'trendan' (girar/mudar de direção).",
    "Login": "Entrada em sistema. De 'log' (registro) + 'in' (dentro).",
    "Night": "Vem do anglo-saxão 'neaht'. Período de escuridão.",
    "Love": "Deriva de 'lufu'. Sentimento profundo de afeição.",
    "Handebol": "Esporte com as mãos. Do alemão 'Handball'.",
    "Spoiler": "Revelar enredo. Do verbo 'to spoil' (estragar/saquear).",
    "Download": "Carregar para baixo. 'Down' (baixo) + 'Load' (carga).",
    "Gmail": "Google + Mail (Correio Eletrônico).",
    "Fitness": "Boa forma física. De 'fit' (em forma).",
    "Personal Trainer": "Treinador pessoal.",
    "Site": "Lugar virtual. Do latim 'situs'.",
    "Coquetel": "De 'cocktail' (rabo de galo). Mistura de bebidas.",
    "Blecaute": "Do inglês 'blackout'. Falta de luz ou memória.",
    "Story": "História. Postagens temporárias de 24 horas.",
    "Feed": "Fluxo de conteúdo organizado.",
    "Show": "Espetáculo ou exibição pública.",
    "Milk-shake": "Leite batido com sorvete."
}

palavras_lista = list(words_data.keys())
total_palavras = len(palavras_lista)

print(Fore.CYAN + Style.BRIGHT +
      '=== Dicionário de Palavras Estrangeiras (Anglo Saxônica)===')

while True:
    print(Fore.WHITE + "\n" + "-"*50)
    entrada = input(
        f'Escolha um número de 1 a {total_palavras}: ').strip().lower()

    try:
        escolha = int(entrada)

        if 1 <= escolha <= total_palavras:
            palavra = random.choice(palavras_lista)

            print(f"\n{Fore.YELLOW}Palavra selecionada: {Fore.GREEN}{palavra}")
            print(
                f"{Fore.YELLOW}Origem e Significado: {Style.RESET_ALL}{words_data[palavra]}")
        else:
            print(
                Fore.RED + f"Erro: Digite um número válido entre 1 e {total_palavras}.")

    except ValueError:
        print(Fore.RED + "Ops... parece que você digitou errado. Por favor, digite um numéro inteiro.")
