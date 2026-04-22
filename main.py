from colorama import Fore, Style, init
import random

# Inicializa o colorama para funcionar corretamente no Windows e outros sistemas
init(autoreset=True)

words_data = {
    "Jeans": "Palavra de origem inglesa incorporada ao português sem tradução. Refere-se a uma peça de vestuário comum no dia a dia, associada à praticidade e versatilidade. Seu uso demonstra a influência da cultura anglo-saxônica no nosso idioma.",
    "Rock": "Termo de origem inglesa utilizado para designar um gênero musical. Também está associado à liberdade de expressão e identidade cultural. Sua permanência em inglês evidencia a influência internacional no vocabulário português.",
    "Look": "Significa olhar, aparência ou visual. Vem do inglês antigo “lōcian”, usado pelos povos anglo-saxões com o sentido de olhar ou observar.",
    "Link": "Significa ligação, conexão ou elo. Vem do inglês antigo “hlenc”, que significava elo de corrente, algo que conecta uma coisa à outra.",
    "Streaming": "Refere-se à tecnologia de transmissão contínua de dados de áudio e vídeo por meio da internet, permitindo o acesso ao conteúdo sem a necessidade de realizar o download do arquivo. A palavra tem origem no termo stream, que significa riacho ou fluxo de água, relacionando assim ao seu significado, expressando o fluxo de dados como um rio",
    "Selfie": "Trata-se de um registro de si mesmo, geralmente capturada por meio de dispositivos móveis e bastante presente nas interações digitais. Vindo do inglês antigo, vem da palavra self, que traduzida significa si mesmo, junto ao sufixo ie que possibilita um tom casual.",
    "Blush": "Vem do inglês to blush, que significa “corar” (ficar com as bochechas avermelhadas). A palavra tem raiz no inglês antigo blyscan, relacionada a “ficar vermelho de emoção”. Como substantivo, blush é o produto de maquiagem usado nas bochechas para dar um tom rosado, simulando esse efeito natural de “corar”.",
    "Gloss": "Vem do inglês, com raiz no grego glōssa (γλῶσσα), que significa “língua” ou “palavra difícil”. Com o tempo, passou a significar “explicação” e depois “brilho/superfície brilhante”. Pode significar brilho ou acabamento brilhante. No dia a dia, é muito usado como abreviação de lip gloss, que é um produto de maquiagem para dar brilho aos lábios.",
    "Folclore": "é um gênero da cultura de origem popular, que representa a identidade social de uma comunidade através de atividades culturais que nasceram, individualmente ou coletivamente, e se desenvolveram com o povo. Tem sua origem da junção do inglês \"folk\", que significa “povo, raça” e -lore, com o sentido de conhecimento",
    "Lanche": "Curiosamente, em inglês significa \"almoço\", mas no Brasil adaptamos para a refeição leve entre as principais.",
    "Marketing": "Vem do inglês “market” (mercado), surgido nos Estados Unidos no início do século XX, com o desenvolvimento das práticas comerciais e publicitárias. Refere-se ao conjunto de estratégias usadas para divulgar, promover e vender produtos ou serviços, buscando atrair e fidelizar consumidores.",
    "Delivery": "Vem do inglês “to deliver” (entregar), popularizado nos Estados Unidos com o crescimento dos serviços de entrega. Refere-se ao serviço de entrega de produtos em domicílio, principalmente alimentos, feito por restaurantes, lojas ou aplicativos.",
    "Hobby": "Deriva de hobyn (cavalo pequeno) e hobby-horse (cavalo de pau infantil). A metáfora surgiu da ideia de \"montar\" um interesse com o mesmo entusiasmo de uma criança brincando. Atividade de lazer praticada por prazer e relaxamento, sem caráter profissional. É o termo padrão, raramente trocado por \"passatempo\" ou \"entretenimento\".",
    "Feedback": "Junção de feed (alimentar) e back (de volta). Surgiu na eletrônica (anos 1920) para descrever o retorno de um sinal que ajusta um sistema. Resposta ou reação a um comportamento ou processo. Avaliação de desempenho focada em melhoria ou reconhecimento. Transbordou para a vida pessoal, sendo usado para pedir opiniões sobre situações cotidianas (como o gosto de um jantar ou uma peça de roupa).",
    "Trend": "Significa tendência, algo que está em alta ou se tornando popular. Vem do inglês antigo “trendan”, que significava girar, mudar de direção ou seguir um curso, ideia que evoluiu para indicar algo que se desenvolve ou ganha popularidade ao longo do tempo.",
    "Login": "Significa entrada em um sistema, acesso ou autenticação. Vem do inglês “log in”, formado por “log” (registro, diário) + “in” (dentro). O termo passou a ser usado na computação com o sentido de registrar a entrada de um usuário em um sistema.",
    "Night": "A Origem: Vem da palavra anglo-saxônica neaht. O Significado: É uma das palavras mais estáveis da história. Desde aquela época, já descrevia o período de escuridão. É interessante porque ela é quase igual em outras línguas germânicas (como Nacht no alemão), o que prova que os anglo-saxões trouxeram essa base direto das tribos do norte da Europa.",
    "Love": "A Origem: Deriva da palavra anglo-saxônica lufu. O Significado: No inglês antigo, lufu representava um sentimento profundo de afeição, desejo e cuidado. Ela vem de uma raiz ainda mais antiga que significa \"permitir\" ou \"aprovar\". Ou seja, amar alguém no sentido original era considerar aquela pessoa \"valiosa\" ou \"querida\".",
    "Handebol": "Esporte coletivo jogado com as mãos, onde o objetivo é marcar gols na baliza adversária. Vem do alemão Handball (Hand = mão; Ball = bola).",
    "Spoiler": "Refere-se ao ato de revelar partes cruciais de um enredo (livros, filmes, séries ou jogos) antes que a pessoa o veja, \"estragando\" a surpresa. Vem do verbo inglês to spoil, que significa \"estragar\", \"apodrecer\" ou \"saquear\".",
    "Download": "Origem: É uma palavra composta da língua inglesa.- Down: significa \"para baixo\". Load: significa \"carregar\" ou \"carga\". Significado: Literalmente significa \"carregar para baixo\". No mundo da tecnologia, refere-se ao processo de transferir dados ou arquivos de um servidor ou computador remoto para o seu dispositivo (computador, celular, etc.).",
    "Gmail": "É uma sigla e junção de duas palavras.- G: Vem de Google, a empresa que criou o serviço. Mail: Abreviação da palavra inglesa electronic mail, que significa \"correio eletrônico\". Significa literalmente \"Correio Eletrônico do Google\". É o serviço de e-mail gratuito oferecido pela Google.",
    "Fitness": "Origem: do inglês “fitness”, de “fit” (em forma). Popularizou-se no século XX, nos Estados Unidos. Significado atual: boa forma física e estilo de vida saudável.",
    "Personal Trainer": "Origina do inglês “personal trainer” (treinador pessoal), surgido nos Estados Unidos. Significa profissional que orienta treinos de forma individualizada.",
    "Site": "Originado do latim situs (lugar), o site foi criado por Tim Berners-Lee nos anos 90 como um espaço virtual para organizar informações via hipertexto. Em resumo, ele funciona como um endereço digital único onde páginas conectadas centralizam conteúdos, serviços ou identidades, tornando a comunicação global acessível através de um ponto fixo na rede.",
    "Coquetel": "Vem do inglês cocktail (rabo de galo). Antigamente, cavalos de raça mista tinham o rabo cortado para cima, parecendo o de um galo. Como eram animais \"misturados\", o nome passou a batizar bebidas que também misturavam vários ingredientes.",
    "Blecaute": "Vem do inglês blackout (escurecer tudo). Ficou famoso na Segunda Guerra Mundial, quando cidades inteiras apagavam as luzes à noite para não serem vistas por aviões inimigos. Hoje, usamos para definir a falta de energia ou um \"branco\" na memória.",
    "Story": "Vem do inglês story (história). O termo se popularizou com as redes sociais para descrever postagens rápidas e informais. Hoje, refere-se a fotos ou vídeos temporários que ficam visíveis por apenas 24 horas, criando um senso de urgência e cotidiano.",
    "Feed": "Vem do inglês feed (alimentar/fluxo). Originalmente usado para fluxos de dados, nas redes sociais virou o \"estoque\" de conteúdo. É a página principal ou o perfil onde as publicações ficam organizadas de forma permanente, servindo como uma vitrine fixa do usuário.",
    "Show": "Vem do inglês show (mostrar/exibir). A palavra se consolidou nos palcos dos Estados Unidos e Reino Unido para definir qualquer espetáculo visual. Hoje, usamos o termo para descrever apresentações ao vivo, especialmente musicais, onde o foco é o entretenimento e a performance para um público.",
    "Milk-shake": "Vem do inglês milk shake (leite batido). Criada nos Estados Unidos no século XIX, a expressão descrevia literalmente o ato de bater o leite com outros ingredientes. Atualmente, define aquela bebida clássica e cremosa que mistura leite e sorvete, sendo um ícone de lanchonetes ao redor do mundo.",
    "Deletar":"Vem do verbo 'to delete'. Curiosamente, ela se tornou tão comum que ganhou uma conjugação completa em português, substituindo muitas vezes o nosso 'apagar' ou 'excluir'",
    "Layout":"Em vez de dizermos 'esquema gráfico','configuração' ou 'disposição visual', usamos layout para falar desde a organização de um site até o arranjo dos móveis em uma sala."
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
