import csv


def client_nou(client_id: int, nume: str, oras: str, sold: int) -> dict:
    pass


def descrie(client: dict) -> str:
    pass


def mareste_sold(client: dict, suma: int) -> dict:
    pass


def din_liste(ids: list, nume: list, orase: list, solduri: list) -> list:
    pass


def citeste_tranzactii(nume_fisier: str) -> list:
    tranzactii=[]
    with open(nume_fisier, "r") as fisier:
        cititor=csv.reader(fisier)
        next(cititor)
        for id, client_id,tip,suma in cititor:
            tranzactii.append({"id":int(id),"client_id": int(client_id),"tip": tip, "suma": int(suma)}) 
    return tranzactii
    


def citeste_clienti(nume_fisier: str) -> list:
    clienti=[]
    with open(nume_fisier, "r") as fisier:
        cititor=csv.reader(fisier)
        next(cititor)
        for client_id, nume,varsta,oras,sold,venit_lunar, nr_tranzactii in cititor :
            clienti.append({"client_id":int(client_id), "nume":nume, "varsta":varsta, "oras":oras,
                            "sold":int(sold), "venit_lunar":venit_lunar, "nr_tranzactii":nr_tranzactii})
    return clienti
            
        
        


def total(tranzactii: list) -> int:
    s=0
    for n in tranzactii:
        s+=n["suma"]
    return s


def medie(tranzactii: list) -> float:
    if len(tranzactii) == 0 :
        return 0.0

    return round(total(tranzactii)/len(tranzactii),2)


def total_pe(tranzactii: list, cheie: str) -> dict:
   totaluri={}
   for tranzactie in tranzactii:
    grup=tranzactie[cheie]
    if grup in totaluri :
       totaluri[grup]+=tranzactie["suma"]
    else:
        totaluri[grup]=tranzactie["suma"]
   return totaluri



def clienti_dupa_id(clienti: list) -> dict:
    pass


def tranzactii_cu_client(tranzactii: list, clienti: list) -> list:
    pass


def total_pe_oras(tranzactii: list, clienti: list) -> dict:
    pass


def clienti_fara_tranzactii(tranzactii: list, clienti: list) -> list:
    pass


def segment(client: dict) -> str:
    pass


def total_pe_segment(tranzactii: list, clienti: list) -> dict:
    pass


def tranzactii_orfane(tranzactii: list, clienti: list) -> list:
    pass


def raport(tranzactii: list, clienti: list, fisier_iesire: str) -> None:
    pass
