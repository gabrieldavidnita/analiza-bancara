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
    pass


def citeste_clienti(nume_fisier: str) -> list:
    pass


def total(tranzactii: list) -> int:
    pass


def medie(tranzactii: list) -> float:
    pass


def total_pe(tranzactii: list, cheie: str) -> dict:
    pass


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
