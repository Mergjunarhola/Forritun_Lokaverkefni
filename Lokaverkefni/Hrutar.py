#Hrutar
#Höfundur: Jón Benediktsson
#dags: 8.5.2017
from random import *

class Dealer:
    def __init__(self,spilarar,Stokkur,infospilara,passw):
        self.__players = spilarar
        self.__typeP = infospilara
        self.__Nafnstokk= "Spilinn"

        try:
            skra = open(self.__Nafnstokk+".txt", "r", encoding="UTF-8")
        except IOError:
            print("halltu kjafti")

        else:
            skrac = ""
            skrac = (skra.read())
            skra.close()
            skrac = skrac.split("\n")
            upply = []
            self.__gildi = []
            self.__lysingar = []
            self.__stokkur=[]
            carstokk=[]
            for x in range(len(skrac)):
                upply.append(skrac[x].split(";"))

            for x in range(len(upply)):
                if x == 0:
                    self.__gildi=upply[0]
                elif x == 1:
                    self.__lysingar=upply[0]
                else:
                    for y in range(len(self.__gildi)):
                        if self.__gildi[y]=="n":
                            carstokk.append(upply[x][y])
                        elif self.__gildi[y]=="f":
                            carstokk.append(float(upply[x][y]))
                        elif self.__gildi[y]=="i":
                            carstokk.append(int(upply[x][y]))
                    self.__stokkur.append(carstokk)
                    carstokk=[]

            self.__spilararIleik=[]
            self.__hverDattUt=[]
            self.__pottur=[]
            self.__stigatafla=[]
            self.__spilEinstakklinga=[]
            self.__Lykilord=passw
            self.__turn=0
            self.__Jaft=[]
            self.__conturn=0
            self.__gera=-1
            self.__geracon=-1
            for x in range(len(self.__players)):
                self.__stigatafla.append(0)


    def Gefa(self):
        self.__spilEinstakklinga = []
        self.__spilararIleik = self.__players
        used=[]
        randomspil=0
        for x in range(len(self.__players)):
            self.__spilEinstakklinga.append([])
            for y in range(len(self.__stokkur)//len(self.__players)):
                randomspil=randint(0,len(self.__stokkur)-1)
                while randomspil in used:
                    randomspil = randint(0, len(self.__stokkur) - 1)
                self.__spilEinstakklinga[x].append(randomspil)
    def GetState(self):
        utk=True
        if self.__conturn==0:
            if len(self.__spilararIleik):
                utk=False
        return utk

    def GetPnum(self,name):
        pnum=self.__players.index(name)
        return self.__players

    def Gera(self):
        gerutk=0
        if self.__conturn > 0:
            if self.__geracon == -1:
                self.__geracon = self.__Jaft.index(self.__spilararIleik[self.__gera])
                gerutk = self.__spilararIleik.index(self.__Jaft[self.__geracon])
            else:
                self.__geracon = (self.__geracon+1)%len(self.__Jaft)
                gerutk = self.__spilararIleik.index(self.__Jaft[self.__geracon])
        else:
            self.__gera = (self.__gera+1)%len(self.__spilararIleik)
            gerutk = self.__gera
        return gerutk



    def Plcheck(self):















flag=True


while flag:
    while Dealer.GetState():
















