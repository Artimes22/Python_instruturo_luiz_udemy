# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras Classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstratmethods são métodos que não tem corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser intânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstratmethods).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso 
# use @abstratmethods como decorador mais interno.

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
l = LogPrintMixin()
l.log_success('OK')