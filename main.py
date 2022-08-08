from Maquina import Maquina
import sys

# mensagens
valida = "\nRepresentacao MTU valida\n"
invalida = "\nRepresentacao MTU invalida\n"

if __name__ == '__main__':
    try:
        arquivo = open(sys.argv[1], 'r')
    except:
        print("Erro ao abrir arquivo")

    rMw = arquivo.read()

    if rMw[:3] == "000":
        rMw = rMw[3:]
        segOcorrencia = rMw.find("000")


        if segOcorrencia == -1:
            print(invalida)
            exit(0)
        else:
            rM = rMw[:segOcorrencia]
            rM = rM.split("00")

            if len(rM) == 1:
                print(invalida)
                exit(0)

            w = rMw[segOcorrencia+3:]

            terOcorrencia = w.find("000")

            if terOcorrencia == -1:
                print(invalida)
                exit(0)
            else:
                w = w[:len(w)-4]
                w = w.split('0')

                w.append('111')

                print(valida)

                Maquina(rM, w).executarMaquina()
    else:
        print(invalida)
