from itertools import cycle
import sys

global inicio
global ntotal
global outfile

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    r = (-s) % 11
    if r!=10:
        return str(r)
    else:
        return "k"


def main():
    inicio = 10000000
    ntotal = 100
    outfile = ""
    singuion = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-i':
            inicio = int(sys.argv[i+1])
        elif sys.argv[i] == '-n':
            ntotal = int(sys.argv[i+1])
        elif sys.argv[i] == '-o':
            outfile = sys.argv[i+1]
        elif sys.argv[i] == '-sg':
            singuion = True
    result=[]
    for i in range(inicio, inicio+ntotal):
        if (singuion):
            rut = str(i) + str(digito_verificador(i))
        else:
            rut = str(i) + "-" +str(digito_verificador(i))
        result.append(rut)
    if(outfile != ""):
        g = open(outfile,'w+')
        for k in result:
            g.write(k+"\n")
        g.close()
    else:
        print(result)


if __name__ == "__main__":
    main()
