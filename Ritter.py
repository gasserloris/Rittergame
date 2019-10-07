from random import randint
class Ritter:
    name = "Ritter"
    stärke = 0
    rüstung = 0
    leben = 0

    def __init__(self, name):
        self.name = name
        self.stärke = randint(15, 50)
        self.rüstung = randint(1, 10)
        self.leben = randint(60, 100)

    def verteidigen(self, gegnerStärke):
        self.leben = self.leben - (gegnerStärke - self.rüstung)

    def angreifen(self, gegner):
        gegner.verteidigen(self.stärke)
        print(self.name, "Du greifst",gegner.name,"an")

    def gibStärke(self):
        return self.stärke

    def gibLeben(self):
        return self.leben > 0

    def gibRüstung(self):
        return self.rüstung

    def info(self):
        return self.name + " Leben: " + str(self.leben)

    def first_or_second(self,gegner):

        while True:
            choice = input("1_ = angreifen or 2_ = Heilen: ")
            if choice == "1":
                self.angreifen(gegner)
                break
            if choice == "2":
                self.heilen()
                break

    def heilen(self):
        self.leben = randint(5, 15) + self.leben
        print(self.name,"Dein Ritter hat sich geheilt.")