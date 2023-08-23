print(__name__)

def mayor_a_tres(mon1,mon2,mon3):
    menor = 0
    if mon1 > mon2:
        menor = mon1
    else:
        menor = mon2
    if mon3 > menor:
        menor = mon3
    return(menor)

def main():
    r = mayor_a_tres(4,1,6)
    print(r)
    r = mayor_a_tres(40,100,36)
    print(r)

if __name__ == "__main__":
    main()

#print(main())