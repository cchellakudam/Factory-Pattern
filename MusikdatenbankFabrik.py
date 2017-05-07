from abc import ABCMeta, abstractmethod
import time
__author__ = 'DD'

class MusikdatenbankFabrik(metaclass=ABCMeta):
    """ Die Basisklasse fuer Fabriken
    """

    def __init__(self):
        self.geladen = False
        self.playlist=[]
        self.duration=0

    @abstractmethod
    def lade_musik(self):
        pass

    def abspielen(self):
        pass
       # if not self.geladen:
           # self.lade_musik()
       # for song in self.playlist:
           # song.abspielen()
           # time.sleep(1)
       # print('Wir sind am Ende der Playliste angelangt. Auf Wiedersehen!')
