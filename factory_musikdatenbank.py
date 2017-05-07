
import Product
from MusikdatenbankFabrik import MusikdatenbankFabrik

from Musikstueck import Musikstueck


class MusikdatenbankFileFabrik(MusikdatenbankFabrik, Musikstueck):

    def lade_musik(self):
        directory = 'C:/Users/Kithu/Desktop/NewFactory/Musik'
        return directory
    def abspielen(self):
      Product.start()

