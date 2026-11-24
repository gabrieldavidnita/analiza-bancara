from analiza import citeste_tranzactii


def main():
    tranzactii = citeste_tranzactii("tranzactii.csv")
    print(tranzactii)


if __name__ == "__main__":
    main()
