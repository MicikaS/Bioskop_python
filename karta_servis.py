def karte():
    import bioskop
    i=1
    while(i<3):
        print('Dobrodosli u bioskop Singidunum, preostalo je ', bioskop.sm, 'slobodnih mesta')
        ime_prezime=input('Unesite vase ime i prezime: ')
        try:
            broj=int(input('Unesite broj karata koliko zelite da rezervisete: '))
        except ValueError:
            print("Niste uneli broj")
            print('')
            continue
        else:
            bioskop.rezervisanje(ime_prezime,broj)
            print('')
        
        


        i=i+1

    for e in bioskop.rezervacije:
        print(e)
    m=None
    for e in bioskop.rezervacije:
        
        if (e['ime_prezime']=='Marko Markovic'):
            m=e['broj']
    if m is not None:
        print('Marko je uzeo ',m,' karte/karata')
    else:
        print('Marko Markovic nije napravio nijednu rezervaciju')

