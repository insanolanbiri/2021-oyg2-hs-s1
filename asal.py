#!/usr/bin/python3

# bilsemde böyle bişey yapmadık ama canım sıkılmış olsa gerek,
# evde böyle bişey yapmışım.
import sys


def asal(max:int) -> list:
    """
    asal sayı bulma şeyi, sanırsam `sieve of eratostenes` diye geçiyor

    `max`: asal sayıların bulunacağı maksimum değer
    """
    durum=[True for _ in range(max)]
    durum[0]=durum[1]=None
    for i in range(2,len(durum)):
        if durum[i]:
            for j in range(i+1,len(durum)):
                if j%i==0:
                    durum[j]=False
    out=[i for i in range(2,len(durum)) if durum[i]]
    return out

def main():
    """
    verilen 1. argümana kadar olan asal sayıları yazdıran main method.
    çalıştırırken argüman veriyorsunuz: `./asal.py <max>` gibi.
    """
    
    try:
        if not sys.argv[1]:
            raise Exception
        max=int(sys.argv[1])
    except:
        print("bana bir sayı vermen lazım")
        return 1
    else:
        print(asal(max))
        return 0

if __name__=="__main__":
    sys.exit(main())