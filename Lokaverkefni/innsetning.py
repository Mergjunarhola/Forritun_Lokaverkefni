# innsetning
# Jón Benediktsson
# dags: 2.5.2017

Stokkur = {}
tempnafn = ""
templisti = []
stada = True
while stada:

    tempnafn = input("hvað er nafnið? ")
    templisti.append(float(input("Þyngd í Kílóum: ")))
    templisti.append(int(input("Mjólkurlagni dætra: ")))
    templisti.append(float(input("Einkunn ullar: ")))
    templisti.append(int(input("Fjöldi afkvæma: ")))
    templisti.append(float(input("Einkunn læris: ")))
    templisti.append(int(input("Frjósemi: ")))
    templisti.append(int(input("Gerð/Þykkt bakvöðva: ")))
    templisti.append(float(input("Einkun fyrir malir: ")))
    Stokkur[tempnafn]=templisti
    templisti=[]
    print(Stokkur)
    if input("viltu halda áfram ") == "nei":
        stada = False

for x in Stokkur:
    print(x+" >> "+str(Stokkur[x][0]))