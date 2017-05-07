

from factory_musikdatenbank import MusikdatenbankFileFabrik

__author__ = 'Chrstopher Chellakudam'




if __name__ == '__main__':

    fabrik = MusikdatenbankFileFabrik()
    #fabrik = MusikdatenbankMockupFabrik()
    #fabrik.lade_musik()
    fabrik.abspielen()