__author__ = 'Gabriel'

import sys
import json
from tkinter.filedialog import askopenfilename
from Buffer import WriteOnDataBlock

def LoadAndWriteJSON(targetDataBlockAddress: int) -> None:

    filename = askopenfilename()

    with open(filename, "rb") as f:

        dataRaw = f.read()

        WriteOnDataBlock(targetDataBlockAddress, dataRaw)

        #dataStr = dataRaw.decode()
        #print(dataStr)

        #data

    pass

'''
items = 3

dataEntry = [0   , 1001, 2001]
dataSize  = [1000, 1000, 1000]

binItems = int(bin(items)[0:2] + bin(items)[2:].zfill(8), 2).to_bytes(1, byteorder=sys.byteorder)

#binItems = bytes([int(bin(items)[0:2] + bin(items)[2:].zfill(8), 2)])

dataEntry1 = bin(dataEntry[0])[0:2] + bin(dataEntry[0])[2:].zfill(12)
dataSize1  = bin(dataSize[0])[0:2]  + bin(dataSize[0])[2:].zfill(12)

dataEntry2 = bin(dataEntry[1])[0:2] + bin(dataEntry[1])[2:].zfill(12)
dataSize2  = bin(dataSize[1])[0:2]  + bin(dataSize[1])[2:].zfill(12)

dataEntry3 = bin(dataEntry[2])[0:2] + bin(dataEntry[2])[2:].zfill(12)
dataSize3  = bin(dataSize[2])[0:2]  + bin(dataSize[2])[2:].zfill(12)

data1 = int('0b' + dataSize1[6:14], 2).to_bytes(1, byteorder=sys.byteorder) + \
        int('0b' + dataEntry1[10:14] + dataSize1[2:6], 2).to_bytes(1, byteorder=sys.byteorder) + \
        int(dataEntry1[0:10], 2).to_bytes(1, byteorder=sys.byteorder)
data2 = int('0b' + dataSize2[6:14], 2).to_bytes(1, byteorder=sys.byteorder) + \
        int('0b' + dataEntry2[10:14] + dataSize2[2:6], 2).to_bytes(1, byteorder=sys.byteorder) + \
        int(dataEntry2[0:10], 2).to_bytes(1, byteorder=sys.byteorder)
data3 = int('0b' + dataSize3[6:14], 2).to_bytes(1, byteorder=sys.byteorder) + \
        int('0b' + dataEntry3[10:14] + dataSize3[2:6], 2).to_bytes(1, byteorder=sys.byteorder) + \
        int(dataEntry3[0:10], 2).to_bytes(1, byteorder=sys.byteorder)

#data1 = bytes([int('0b' + dataSize1[6:14], 2)]) + bytes([int('0b' + dataEntry1[10:14] + dataSize1[2:6], 2)]) + bytes([int(dataEntry1[0:10], 2)])
#data2 = bytes([int('0b' + dataSize2[6:14], 2)]) + bytes([int('0b' + dataEntry2[10:14] + dataSize2[2:6], 2)]) + bytes([int(dataEntry2[0:10], 2)])
#data3 = bytes([int('0b' + dataSize3[6:14], 2)]) + bytes([int('0b' + dataEntry3[10:14] + dataSize3[2:6], 2)]) + bytes([int(dataEntry3[0:10], 2)])

#dataBin = bin(int.from_bytes(data1, byteorder='little'))

#dataBin = dataBin[0:2] + dataBin[2:].zfill(24)

#binDec1 = int(dataBin[0:14], 2)
#binDec2 = int(dataBin[14:26], 2)

#print(binItems)
#print(data1)
#print(data2)
#print(data3)
'''

LoadAndWriteJSON(0)