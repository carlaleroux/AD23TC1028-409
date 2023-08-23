print(__name__)
'''
function menor()
{
  if n1 < n2
  {
    menor = n1;
  }
  else
  {
    menor = n2;
  }
  if n3 < menor
  {
    menor = n3;
  }
  return  menor;
}
inicio;
call menor(n1,n2,n3);
fin;
'''
def menor_a_tres(mon1,mon2,mon3):
    """Método que calcula el menor de tres números

    Args:
        mon1 (int): Primer numero
        mon2 (int): SEgundo numero
        mon3 (int): Tercer numero
    Return:
        menor (int) : El menor de tres
    """
    menor = 0
    if mon1 < mon2:
        menor = mon1
    else:
        menor = mon2
    if mon3 < menor:
        menor = mon3
    return menor

def main():
    r = menor_a_tres(4,1,6)
    print(r)
    r = menor_a_tres(40,100,36)
    print(r)

if __name__ == "__main__":
    main()

#print(main())