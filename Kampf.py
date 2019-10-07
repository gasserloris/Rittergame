from random import randint
from Ritter import Ritter
import sys

Alfred = Ritter("Alfred")
Wayne = Ritter("Wayne")

print(Alfred.info(), "vs", Wayne.info(), "\n")

while Alfred.gibLeben() and Wayne.gibLeben():
    Alfred.angreifen(Wayne)
    if not Wayne.gibLeben():
        print(Alfred.info(), "hat gewonnen")
        sys.exit(0)
    print(Alfred.info(), Wayne.info())
    Wayne.angreifen(Alfred)
    if not Alfred.gibLeben():
        print(Wayne.info(), "hat gewonnen")
        sys.exit(0)
    print(Alfred.info(), Wayne.info())


