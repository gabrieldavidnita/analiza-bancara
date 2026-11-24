from analiza import(
    citeste_tranzactii,
    citeste_clienti,
    total,
    medie,
    total_pe
)




def main():
    tranzactii = citeste_tranzactii("tranzactii.csv")
    # print(tranzactii[0]['suma'])
    print("------------")
    clienti=citeste_clienti("clienti.csv")
    print(len(clienti) )
    print(len(clienti[0]))
    print(clienti[0]['nume'])
    print(clienti[3]['oras'])
    sold=clienti[4]['sold'] + 1
    print(sold )
    print(clienti[-1]['client_id'] )
    # print(clienti)
    print("----------")
    #total_suma=total(tranzactii)
    print(total(tranzactii))
    print(medie(tranzactii))
    print(total([{'suma': 100}, {'suma': 250}]))
    print(medie([{'suma': 100}, {'suma': 250}]))
    print(total([]))
    print(medie([]))
    print("-----------------")
    print(total_pe(tranzactii, 'tip') )
    print(total_pe(tranzactii, 'client_id')[101] )
    print(total_pe(tranzactii, 'client_id')[104])
    print(total_pe(tranzactii, 'client_id')[999] )
    print(len(total_pe(tranzactii, 'client_id')))
    print(total_pe([], 'tip') )
    

   

     
if __name__ == "__main__":
    main()
    # note = [
    #     {"elev": "Ana",  "materie": "Mate", "nota": 9},
    #     {"elev": "Ion",  "materie": "Info", "nota": 7},
    #     {"elev": "Ana",  "materie": "Mate", "nota": 9},
    #     {"elev": "Maria","materie": "Info", "nota": 8},
    #     {"elev": "Ion",  "materie": "Mate", "nota": 6},
    # ]

    # groups={}
    # for e in note:
    #    grup=e["nota"]
    #    if grup in groups:
    #       groups[grup]+=1
    #    else:
    #       groups[grup]=1
    # print(groups[9])

