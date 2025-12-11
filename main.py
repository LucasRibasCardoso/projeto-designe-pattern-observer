import time
import sys
from podcast_catalogo import PodcastCatalogo
from cliente_podcast import ClientePodcast


def exibir_menu():
    """Exibe o menu de opções do sistema."""
    print("\n" + "="*60)
    print("SISTEMA DE PODCASTS - PADRÃO OBSERVER")
    print("="*60)
    print("1. Consultar episódios do catálogo local")
    print("2. Exibir informações do sistema")
    print("3. Adicionar novo cliente (subscriber)")
    print("4. Limpar catálogo local")
    print("5. Sair")
    print("="*60)


def selecionar_cliente(lista_clientes):
    """Exibe lista de clientes e retorna o cliente selecionado ou None."""
    print("\nSelecione o cliente:")
    for idx, cliente in enumerate(lista_clientes, 1):
        print(f"{idx}. {cliente.obter_nome()}")
    
    try:
        escolha = int(input("\nCliente: ").strip())
        if 1 <= escolha <= len(lista_clientes):
            return lista_clientes[escolha - 1]
        print("\n[ERRO] Opção inválida!")
    except ValueError:
        print("\n[ERRO] Por favor, digite um número válido!")
    
    return None


def consultar_episodios(lista_clientes):
    """Consulta e exibe os episódios do catálogo local de um cliente."""
    cliente = selecionar_cliente(lista_clientes)
    if cliente:
        cliente.listar_episodios()


def exibir_informacoes(catalogo, lista_clientes):
    """Exibe informações gerais do sistema."""
    print("\n" + "="*60)
    print("INFORMAÇÕES DO SISTEMA")
    print("="*60)
    print(f"Total de episódios publicados: {len(catalogo.obter_episodios())}")
    print(f"Total de subscribers ativos: {catalogo.obter_total_subscribers()}")
    print("\nClientes registrados:")
    for idx, cliente in enumerate(lista_clientes, 1):
        print(f"  {idx}. {cliente.obter_nome()} - {cliente.obter_total_episodios()} episódios recebidos")
    print("="*60)


def adicionar_cliente(catalogo, lista_clientes):
    """Adiciona um novo cliente (subscriber) ao sistema."""
    nome = input("\nNome do novo cliente: ").strip()
    if nome:
        novo_cliente = ClientePodcast(nome)
        catalogo.attach(novo_cliente)
        lista_clientes.append(novo_cliente)
        print(f"\n[SISTEMA] Cliente '{nome}' registrado com sucesso!")
    else:
        print("\n[ERRO] Nome inválido!")


def limpar_catalogo(lista_clientes):
    """Limpa o catálogo local de um cliente selecionado."""
    cliente = selecionar_cliente(lista_clientes)
    if cliente:
        cliente.limpar_catalogo()


def sair(catalogo):
    """Encerra o sistema de forma segura."""
    print("\n[SISTEMA] Encerrando o sistema...")
    catalogo.parar_publicacao_automatica()
    sys.exit(0)


def processar_opcao(opcao, catalogo, lista_clientes):
    """Processa a opção selecionada usando match-case."""
    match opcao:
        case "1":
            consultar_episodios(lista_clientes)
        case "2":
            exibir_informacoes(catalogo, lista_clientes)
        case "3":
            adicionar_cliente(catalogo, lista_clientes)
        case "4":
            limpar_catalogo(lista_clientes)
        case "5":
            sair(catalogo)
        case _:
            print("\n[ERRO] Opção inválida! Tente novamente.")


def main():
    """Função principal que executa o sistema."""
    print("\n" + "="*60)
    print("INICIANDO SISTEMA DE PODCASTS")
    print("="*60)
    
    # Criar o Publisher (Catálogo de Podcasts)
    catalogo = PodcastCatalogo("PodcastHub")
    
    # Criar Subscribers (Clientes/Agregadores)
    cliente1 = ClientePodcast("Spotify")
    cliente2 = ClientePodcast("Apple Podcasts")
    
    # Registrar subscribers no publisher
    catalogo.attach(cliente1)
    catalogo.attach(cliente2)
    
    lista_clientes = [cliente1, cliente2]
    
    # Iniciar publicação automática de episódios
    catalogo.iniciar_publicacao_automatica()
    
    print("\n[SISTEMA] Aguardando alguns segundos para receber os primeiros episódios...")
    time.sleep(3)
    
    # Loop infinito do menu
    while True:
        try:
            exibir_menu()
            opcao = input("\nEscolha uma opção: ").strip()
            processar_opcao(opcao, catalogo, lista_clientes)
        except KeyboardInterrupt:
            sair(catalogo)


if __name__ == "__main__":
    main()
