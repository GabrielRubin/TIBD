__author__ = 'Gabriel'

import json
import sys

DATABLOCK_MAX_SIZE      = 4096
DATAFILE_MAX_DATABLOCKS = 65536

'''
from ListaDeCompras import Produto
from ListaDeCompras import ListaDeCompras

produto0   = Produto(0, "Leite", 5.50)
produto1   = Produto(1, "Ovomaltino", 10.0)
produto2   = Produto(2, "Pera", 3.0)

produtos = [produto0, produto1, produto2]

listaJuvenil = ListaDeCompras(produtos, "Garotinho Juvenil")

jsonObj = json.dumps(listaJuvenil.ToJason(), indent=3, sort_keys=True)

s = bytes(jsonObj, 'utf-8')

print(s)

with open("testData", "wb") as f:
    f.write(s)

with open("testData", "rb") as f:
    print(f.read().decode('utf-8'))
'''

def LoadDataBlock(dataBlockAddress: int, debug = False) -> int:

    """

    :param dataBlockAddress: Specify the address of the datablock
    :param debug: Specify if the information readed should be printed or not (defalt: False)
    :return: raw Datablock (as a binary str)
    """
    with open("dataFile", "rb") as f:

        f.seek(DATABLOCK_MAX_SIZE * dataBlockAddress, 0)

        data  = f.read(DATABLOCK_MAX_SIZE)

        if debug:

            index1 = int.from_bytes(data[:1], byteorder=sys.byteorder)
            index2 = int.from_bytes(data[1:2], byteorder=sys.byteorder)
            index = index1 * 256 + index2

            print("Datablock address = {0} :: Desired address = {1}".format(index, dataBlockAddress))
            print("Datablock size = {0}".format(len(data)))
            print("Datablock contents:")
            print(data)

    return data

#def WriteOnDataFile(data, dataBlockAddress):
    #LoadDataBlock(dataBlockAddress)
    #dataBlock = ReadDataBlock(dataBlockAddress)
    #print(dataBlock)

def WriteToDataFile(data, dataBlockAddress):

    print(data)

    with open("dataFile", "r+b") as f:

        f.seek(dataBlockAddress * DATABLOCK_MAX_SIZE)

        f.write(data)

        f.close()


def EraseAllData() -> None:

    """

    ERASE ALL DATA - CREATE A NEW DATAFILE!
    """
    chunkSize = DATAFILE_MAX_DATABLOCKS

    byteChunk = "0"

    dataBlockAddress1 = [0]

    dataBlockAddress2 = [0]

    dataBlockIndex = 0

    for i in range(4, DATABLOCK_MAX_SIZE+1):
        byteChunk += "x"

    print("Creating new dataFile...")

    with open("dataFile", "wb") as f:

        while(chunkSize > 0):

            chunkSize -= 1

            dataBlockAddress1[0] = dataBlockIndex // 256
            dataBlockAddress2[0] = dataBlockIndex %  256

            hexa = bytes(dataBlockAddress1) + bytes(dataBlockAddress2)

            numberOfData = int(bin(0)[0:2] + bin(0)[2:].zfill(8), 2).to_bytes(1, byteorder=sys.byteorder)

            f.write(hexa + numberOfData + byteChunk.encode('utf-8')[1:])

            dataBlockIndex += 1

        f.close()

#LoadDataBlock(0, True)

#EraseAllData()