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

        dataOffset   = 3 + (2 * numberOfData)

        currentOffset = 0

        for i in range(0, numberOfData):

            itemInfo  = rawData[3 + (2*i) : (3 + (2*i)) + 2]

            dataBin   = bin(int.from_bytes(itemInfo, byteorder='little'))

            dataBin   = dataBin[0:2] + dataBin[2:].zfill(16)

            itemSize  = int(dataBin[0:14],  2)

            self.isDivided = bool(int(dataBin[14:18], 2))

            print(self.isDivided)

            print("ItemSize: {0}".format(itemSize))

            jsonFile  = rawData[dataOffset + currentOffset : dataOffset + currentOffset + itemSize]

            print(jsonFile)

            self.data.append(jsonFile)

            currentOffset += itemSize

        pass

    def ToBytes(self):

        blockAddress = bytes([self.address // 256]) + bytes([self.address %  256])

        numberOfData = len(self.data).to_bytes(1, byteorder=sys.byteorder)

        hexTable  = bytes()

        hexData   = bytes()



        for i in range(0, len(self.data)):

            itemSize  = len(self.data[i])

            binItemSize  = bin(itemSize)[0:2] + bin(itemSize)[2:].zfill(12)

            print(binItemSize)

            isDivided = False #temp

            isItemBin = bin(isDivided)[2:].zfill(4)

            hexTableEntry = int('0b' + binItemSize[10:14] + isItemBin, 2).to_bytes(1, byteorder=sys.byteorder) + \
                            int(binItemSize[0:10], 2).to_bytes(1, byteorder=sys.byteorder)

            print(hexTableEntry)

            hexTable += hexTableEntry

            hexData  += self.data[i]

        totaldata = blockAddress + numberOfData + hexTable + hexData

        byteChunk = ""

        for i in range(len(totaldata), self.DATABLOCK_MAX_SIZE+1):
            byteChunk += "x"

        return totaldata + byteChunk.encode('utf-8')[1:]