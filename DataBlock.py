__author__ = 'Gabriel'

import sys

class DataBlock:

    def __init__(self, rawData : int):
        #self.address = 0
        self.data    = []

        self.DATABLOCK_MAX_SIZE = 4096

        addressHex1  = int.from_bytes(rawData[:1], byteorder=sys.byteorder)
        addressHex2  = int.from_bytes(rawData[1:2], byteorder=sys.byteorder)
        self.address = addressHex1 * 256 + addressHex2

        numberOfData = int.from_bytes(rawData[2:3], byteorder=sys.byteorder)

        dataOffset   = 4 + (3 * numberOfData)

        for i in range(0, numberOfData):

            itemInfo  = rawData[3 * (i+1) : (3 * (i+1)) + 3]

            dataBin   = bin(int.from_bytes(itemInfo, byteorder='little'))

            dataBin   = dataBin[0:2] + dataBin[2:].zfill(24)

            itemIndex = int(dataBin[0:14], 2)

            print("ItemIndex: {0}".format(itemIndex))

            itemSize  = int(dataBin[14:26], 2)

            print("ItemSize: {0}".format(itemSize))

            jsonFile  = rawData[dataOffset + itemIndex - 1 : dataOffset + itemIndex + itemSize - 1]

            print(jsonFile)

            self.data.append(jsonFile)

    def ToBytes(self):

        blockAddress = bytes([self.address // 256]) + bytes([self.address %  256])

        numberOfData = len(self.data).to_bytes(1, byteorder=sys.byteorder)

        nextIndex = 0

        hexTable  = bytes()

        hexData   = bytes()

        for i in range(0, len(self.data)):

            itemIndex = nextIndex

            itemSize  = len(self.data[i])

            nextIndex += itemSize

            binItemIndex = bin(itemIndex)[0:2] + bin(itemIndex)[2:].zfill(12)
            binItemSize  = bin(itemSize)[0:2]  + bin(itemSize)[2:].zfill(12)

            hexTableEntry = int('0b' + binItemSize[6:14], 2).to_bytes(1, byteorder=sys.byteorder) + \
                            int('0b' + binItemIndex[10:14] + binItemSize[2:6], 2).to_bytes(1, byteorder=sys.byteorder) + \
                            int(binItemIndex[0:10], 2).to_bytes(1, byteorder=sys.byteorder)

            hexTable += hexTableEntry

            hexData  += self.data[i]

            totaldata = blockAddress + numberOfData + hexTable + hexData

            byteChunk = ""

            for i in range(len(totaldata), self.DATABLOCK_MAX_SIZE+1):
                byteChunk += "x"

        return totaldata + byteChunk.encode('utf-8')[1:]