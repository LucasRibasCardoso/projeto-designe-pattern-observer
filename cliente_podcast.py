from typing import List
from observer import Observer
from datetime import datetime


class ClientePodcast(Observer):
    """
    Subscriber que representa um cliente/agregador de podcasts.
    Recebe notificações do Publisher e mantém seu próprio catálogo local.
    Simula aplicativos como Spotify, Apple Podcasts, Google Podcasts, etc.
    """
    
    def __init__(self, nome: str):
        self._nome = nome
        self._catalogo_local: List[dict] = []
    
    def update(self, episodio: str) -> None:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._catalogo_local.append({
            'episodio': episodio,
            'data_recebimento': timestamp
        })
        print(f"  → [{self._nome}] Episódio recebido: {episodio}")
    
    def listar_episodios(self) -> None:
        if not self._catalogo_local:
            print(f"\n[{self._nome}] Catálogo vazio. Nenhum episódio recebido ainda.")
            return
        
        print(f"\n{'='*60}")
        print(f"CATÁLOGO LOCAL - {self._nome}")
        print(f"{'='*60}")
        print(f"Total de episódios: {len(self._catalogo_local)}\n")
        
        for idx, item in enumerate(self._catalogo_local, 1):
            print(f"{idx}. {item['episodio']}")
            print(f"   Recebido em: {item['data_recebimento']}\n")
        print(f"{'='*60}\n")
    
    def obter_total_episodios(self) -> int:
        return len(self._catalogo_local)
    
    def limpar_catalogo(self) -> None:
        self._catalogo_local.clear()
        print(f"[{self._nome}] Catálogo local limpo.")
    
    def obter_nome(self) -> str:
        return self._nome
    
    def obter_ultimo_episodio(self) -> str:
        if self._catalogo_local:
            return self._catalogo_local[-1]['episodio']
        return None
