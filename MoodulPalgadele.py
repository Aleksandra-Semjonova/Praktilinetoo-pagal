def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    :param list i: inimeste järjend
    :param list p: Palgate järjend
    :param list n: inimeste arv
    :rtype: list,list
    """
    if n>0:
        for j in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk:"))
            i.append(nimi)
            p.append(palk)
    return i,p 
def andmed_veerudes(i:list,p:list):
    """Funksioon  kuvab ekranile kahe järjendite andmed veerudes 
    :param list i: Inimeste järjend andmed veerudes
    :param list p:  Palgate järjend
    """
    for j in  range(len(i)):
        print(i[j],"-",p[j])

def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsiioon kutsutab anmeid ja tagastab listid.
    :param list i: Inimeste järjend
    :param list p:  Palgate järjend
    :rtype: list,list
    """
    nimi=input("Keda kutsutada ära(nimi: )")
    
    for j in range(len(i)-1):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p
def kellel_on_suurim_palk(i:list,p:list)->list:
    """Funktsiioon leiab kõige suutim palk.
    :param list i: Inimeste järjend
    :param list p:  Palgate järjend
    :rtype: list,list
    """
    nimed=[]
    max_palk=max(p)
    ind=1
    for palk in p:
        if palk==max_palk: 
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed
def kellel_on_väiksem_palk(i:list,p:list)->list:
    """Funktsiioon leiab kõige väiksem palk.
    :param list i: Inimeste järjend
    :param list p:  Palgate järjend
    :rtype: list,list
    """
    nimed=[]
    min_palk=min(p)
    ind=p.index(min_palk)
    mitu=p.count(min_palk)
    for j in range(mitu):
        nimi=i[p.index(min_palk,ind)]
        nimed.append(nimi)
        ind+=i[]
    return nimed

def sorteerimine(i:list,p:list):
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p
def vordsed_palgad(i:list,p:list)->list:
    """Funktsiioon kes saavad võrdset palka.
    :param list i: Inimeste järjend
    :param list p:  Palgate järjend
    :rtype: list,list
    """
    for id_, palgad in enumerate(p):
        print(id_,palgad)
    for palk in p:
        n=p.count(palk)
        ind=p.index(palk) 
        if n>1:
            subnimed=[] 
            for j in range(n):
                nimi=i[p.index(palk,ind)]
                subnimed.append(nimi) 
                p.pop(ind)


def otsi_nime_järgi(i:list,p:list)->list:
    """"Funktsiioon 
    :param list i: Inimeste järjend
    :param list p:  Palgate järjend
    :rtype: list,list
    """
    palgad={}
    nimi=input("nimi: ")
    for nimi in i:
        n=i.count(nimi)
        ind=i.index(nimi)
        if n>1:
            subp=[] 
            for j in range(n):
                palk=p[i.index(nimi,ind)] 
                subp.pop
                p.pop(ind)
                i.pop(ind)
                ind=+1
            palgad[palk]=subp



def inimeste_nimikiri():
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    :param list i: inimeste järjend
    :param list p: Palgate järjend
    :param list n: inimeste arv
    :rtype: list,list
    """


