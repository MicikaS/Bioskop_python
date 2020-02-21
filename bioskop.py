sm=100
rezervacije=[]

def rezervisanje(ime_prezime,broj):
    global sm
    if sm<broj:
        print('Ne moze se rezervisati toliko mesta, preostalo je',sm,' slobodnih mesta')
    else:
        nova={
            "ime_prezime":ime_prezime,
            "broj":broj
        }
        rezervacije.append(nova)
        sm=sm-broj
    return sm
    
