import time
import random
import threading
from typing import List
from observer import Subject, Observer


class PodcastCatalogo(Subject):
    """
    Publisher que mantém o catálogo de episódios e notifica os subscribers.
    Representa o serviço de distribuição de podcasts (como Spotify, Apple Podcasts, etc).
    """
    
    def __init__(self, nome: str):
        self._nome = nome
        self._episodios: List[str] = []
        self._observers: List[Observer] = []
        self._contador_episodios = 0
        self._executando = False
        self._thread = None
    
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[PUBLISHER] Novo subscriber registrado. Total: {len(self._observers)}")
    
    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[PUBLISHER] Subscriber removido. Total: {len(self._observers)}")
    
    def notify(self, episodio: str) -> None:
        print(f"\n[PUBLISHER] Notificando {len(self._observers)} subscriber(s) sobre: {episodio}")
        for observer in self._observers:
            observer.update(episodio)
    
    def adicionar_episodio(self, episodio: str) -> None:
        self._episodios.append(episodio)
        print(f"[PUBLISHER] Novo episódio disponível: {episodio}")
        self.notify(episodio)
    
    def _gerar_episodios_automaticamente(self) -> None:
        while self._executando:
            # Intervalo aleatório entre 5 e 15 segundos
            tempo_espera = random.randint(5, 15)
            time.sleep(tempo_espera)
            
            if self._executando:
                self._contador_episodios += 1
                nome_episodio = f"episodio{self._contador_episodios:02d}"
                self.adicionar_episodio(nome_episodio)
    
    def iniciar_publicacao_automatica(self) -> None:
        if not self._executando:
            self._executando = True
            self._thread = threading.Thread(
                target=self._gerar_episodios_automaticamente,
                daemon=True
            )
            self._thread.start()
            print(f"[PUBLISHER] {self._nome} iniciado - Publicando episódios automaticamente")
    
    def parar_publicacao_automatica(self) -> None:
        self._executando = False
        if self._thread:
            self._thread.join(timeout=2)
        print(f"[PUBLISHER] {self._nome} pausado")
    
    def obter_episodios(self) -> List[str]:
        return self._episodios.copy()
    
    def obter_total_subscribers(self) -> int:
        return len(self._observers)
