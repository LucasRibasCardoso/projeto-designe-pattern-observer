import time
from podcast_catalogo import PodcastCatalogo
from cliente_podcast import ClientePodcast


def exemplo_basico():
    print("="*60)
    print("EXEMPLO BÁSICO - PADRÃO OBSERVER")
    print("="*60)
    
    # Criar Publisher
    catalogo = PodcastCatalogo("PodcastHub")
    
    # Criar Subscribers
    spotify = ClientePodcast("Spotify")
    apple = ClientePodcast("Apple Podcasts")
    google = ClientePodcast("Google Podcasts")
    
    # Registrar Subscribers no Publisher
    catalogo.attach(spotify)
    catalogo.attach(apple)
    catalogo.attach(google)
    
    print("\n[EXEMPLO] Adicionando episódios manualmente...")
    
    # Adicionar episódios manualmente
    catalogo.adicionar_episodio("episodio01")
    catalogo.adicionar_episodio("episodio02")
    catalogo.adicionar_episodio("episodio03")
    
    print("\n[EXEMPLO] Consultando catálogos locais:")
    spotify.listar_episodios()
    apple.listar_episodios()
    google.listar_episodios()


def exemplo_automatico():
    """Exemplo com publicação automática."""
    print("\n" + "="*60)
    print("EXEMPLO AUTOMÁTICO - PUBLICAÇÃO EM BACKGROUND")
    print("="*60)
    
    # Criar Publisher e Subscribers
    catalogo = PodcastCatalogo("NerdcastHub")
    cliente1 = ClientePodcast("Cliente1")
    cliente2 = ClientePodcast("Cliente2")
    
    # Registrar
    catalogo.attach(cliente1)
    catalogo.attach(cliente2)
    
    # Iniciar publicação automática
    catalogo.iniciar_publicacao_automatica()
    
    print("\n[EXEMPLO] Aguardando 20 segundos para receber episódios...")
    time.sleep(20)
    
    # Parar publicação
    catalogo.parar_publicacao_automatica()
    
    print("\n[EXEMPLO] Episódios recebidos pelos clientes:")
    cliente1.listar_episodios()
    cliente2.listar_episodios()


def exemplo_adicionar_remover_subscriber():
    print("\n" + "="*60)
    print("EXEMPLO - ADICIONAR/REMOVER SUBSCRIBERS DINAMICAMENTE")
    print("="*60)
    
    catalogo = PodcastCatalogo("DynamicHub")
    cliente1 = ClientePodcast("Cliente1")
    cliente2 = ClientePodcast("Cliente2")
    
    # Adicionar primeiro cliente
    catalogo.attach(cliente1)
    catalogo.adicionar_episodio("episodio01")
    
    # Adicionar segundo cliente
    catalogo.attach(cliente2)
    catalogo.adicionar_episodio("episodio02")
    
    # Remover primeiro cliente
    catalogo.detach(cliente1)
    catalogo.adicionar_episodio("episodio03")
    
    print("\n[EXEMPLO] Cliente1 (foi removido antes do episodio03):")
    cliente1.listar_episodios()
    
    print("\n[EXEMPLO] Cliente2 (recebeu todos os episódios):")
    cliente2.listar_episodios()


if __name__ == "__main__":
    # Executar exemplos
    exemplo_basico()
    time.sleep(2)
    
    exemplo_automatico()
    time.sleep(2)
    
    exemplo_adicionar_remover_subscriber()
    
    print("\n" + "="*60)
    print("EXEMPLOS CONCLUÍDOS")
    print("="*60)
