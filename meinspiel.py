class MeinSpiel:
    bilder = ["Bilder/Grass.jpg","Bilder/Hase.jpg"]
    spielfeld = [] 

    def __init__(self, felderX, felderY):
        for x in range(felderX):
            self.spielfeld.append([])
            for y in range(felderY):
                self.spielfeld[x].append(0)

    def anfangsKonfiguration(self):
        self.spielfeld[5][5] = 1

