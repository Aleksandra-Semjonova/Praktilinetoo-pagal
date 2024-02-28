from MoodulPalgadele import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("0-Naita andmed veerudes\n1-andmete lisamine\n2-Anfmete eemaldamine\n")
    valik=int(input())
    if valik==1:
        inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
    elif valik==0:
        andmed_veerudes(inimesed,palgad)
    elif valik==2:
        andmete_eemaldamine_nimi_jargi(inimesed,palgad)
    elif valik==3:
        nimed=kellel_on_suurim_palk(inimesed,palgad)
    elif valik==4:
        nimed=kellel_on_väiksem_palk(inimesed,palgad)
