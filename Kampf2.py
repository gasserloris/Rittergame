from Ritter import Ritter

name = input("Wie heissen Sie: ")

Userritter = Ritter(name)
Computerritter = Ritter("Arthur")
print(Computerritter.info(),"vs", Userritter.info())

while Userritter.gibLeben() and Computerritter.gibLeben():
    Userritter.first_or_second(Computerritter)
    if not Computerritter.gibLeben():
        print(Userritter.info(), "hat gewonnen")
        break
    print(Userritter.info(), Computerritter.info())
    Computerritter.angreifen(Userritter)
    if not Userritter.gibLeben():
        print(Computerritter.info(), "hat gewonnen")
        break
    print(Userritter.info(), Computerritter.info(),"\n")
print("Der Kampf ist vorbei")