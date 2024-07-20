from abc import ABC, abstractmethod
from transitions import Machine
from functools import reduce


class Observer(ABC):
    @abstractmethod
    def update(self, dispositivo):
        pass

class Dispositivo(ABC):
    def __init__(self):
        self._observers = []

    def adicionar_observador(self, observador):
        self._observers.append(observador)

    def remover_observador(self, observador):
        self._observers.remove(observador)

    def notificar_observadores(self):
        for observador in self._observers:
            observador.update(self)

    @abstractmethod
    def obter_status(self):
        pass

    @abstractmethod
    def esta_ligado(self):
        pass

class Luz(Dispositivo):
    states = ['desligada', 'ligada']

    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=Luz.states, initial='desligada')
        self.machine.add_transition(trigger='ligar', source='desligada', dest='ligada', after='notificar_observadores')
        self.machine.add_transition(trigger='desligar', source='ligada', dest='desligada', after='notificar_observadores')

    def obter_status(self):
        return f'Luz está {self.state}'

    def esta_ligado(self):
        return self.state == 'ligada'

class Termostato(Dispositivo):
    states = ['desligado', 'aquecendo', 'esfriando']

    def __init__(self, temperatura_inicial):
        super().__init__()
        self.temperatura = temperatura_inicial
        self.machine = Machine(model=self, states=Termostato.states, initial='desligado')
        self.machine.add_transition(trigger='aquecer', source='desligado', dest='aquecendo', after='notificar_observadores')
        self.machine.add_transition(trigger='esfriar', source='desligado', dest='esfriando', after='notificar_observadores')
        self.machine.add_transition(trigger='desligar', source=['aquecendo', 'esfriando'], dest='desligado', after='notificar_observadores')

    def obter_status(self):
        return f'Termostato está {self.state} a {self.temperatura}°C'

    def esta_ligado(self):
        return self.state in ['aquecendo', 'esfriando']

class SistemaSeguranca(Dispositivo):
    states = ['desarmado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa']

    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=SistemaSeguranca.states, initial='desarmado')
        self.machine.add_transition(trigger='armar_com_gente_em_casa', source='desarmado', dest='armado_com_gente_em_casa', after='notificar_observadores')
        self.machine.add_transition(trigger='armar_sem_gente_em_casa', source='desarmado', dest='armado_sem_ninguem_em_casa', after='notificar_observadores')
        self.machine.add_transition(trigger='desarmar', source=['armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'], dest='desarmado', after='notificar_observadores')

    def obter_status(self):
        return f'Sistema de segurança está {self.state}'

    def esta_ligado(self):
        return self.state != 'desarmado'

class CasaInteligente:
    _instance = None

    def __new__(cls, max_dispositivos):
        if cls._instance is None:
            cls._instance = super(CasaInteligente, cls).__new__(cls)
            cls._instance.dispositivos = []
            cls._instance.max_dispositivos = max_dispositivos
        return cls._instance
    
    def set_max_dispositivos(self, max_dispositivos):
        self.max_dispositivos = max_dispositivos

    def adicionar_dispositivo(self, dispositivo):
        if len(self.dispositivos) < self.max_dispositivos:
            self.dispositivos.append(dispositivo)
        else:
            print("Limite de dispositivos atingido.")

    def remover_dispositivo(self, dispositivo):
        if dispositivo in self.dispositivos:
            self.dispositivos.remove(dispositivo)
        else:
            print("Dispositivo não encontrado.")

    def listar_dispositivos(self):
        for i, dispositivo in enumerate(self.dispositivos):
            print(f'{i}: {dispositivo.obter_status()}')

    def obter_status_todos_dispositivos(self):
        return [dispositivo.obter_status() for dispositivo in self.dispositivos]

    def desligar_todas_luzes(self):
        list(map(lambda d: d.desligar() if isinstance(d, Luz) else None, self.dispositivos))

    def obter_dispositivos_ligados(self):
        return list(filter(lambda d: d.esta_ligado(), self.dispositivos))

    def contar_dispositivos_ligados(self):
        return reduce(lambda total, d: total + (1 if d.esta_ligado() else 0), self.dispositivos, 0)

class DispositivoFactory:
    @staticmethod
    def criar_dispositivo(tipo, *args):
        if tipo == 'Luz':
            return Luz()
        elif tipo == 'Termostato':
            return Termostato(*args)
        elif tipo == 'SistemaSeguranca':
            return SistemaSeguranca()
        else:
            raise ValueError("Tipo de dispositivo desconhecido")

class EstadoDispositivoObserver(Observer):
    def update(self, dispositivo):
        print(f'Notificação: {dispositivo.obter_status()}')


    