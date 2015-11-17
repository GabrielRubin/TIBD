__author__ = 'Gabriel'

import sys

from Data import Data

class DataBlock:

    def __init__(self, rawData):
        #self.address = 0
        self.data    = []

        self.DATABLOCK_MAX_SIZE = 4096

        addressHex1  = int.from_bytes(rawData[:1], byteorder=sys.byteorder)
        addressHex2  = int.from_bytes(rawData[1:2], byteorder=sys.byteorder)
        self.address = addressHex1 * 256 + addressHex2

        numberOfData = int.from_bytes(rawData[2:3], byteorder=sys.byteorder)

        print(numberOfData)

        dataOffset   = 3 + (2 * numberOfData)

        currentOffset = 0

        for i in range(0, numberOfData):

            itemInfo  = rawData[3 + (2*i) : (3 + (2*i)) + 2]

            dataBin   = bin(int.from_bytes(itemInfo, byteorder='little'))

            dataBin   = dataBin[0:2] + dataBin[2:].zfill(16)

            itemSize  = int(dataBin[0:14],  2)

            itemFlags = dataBin[14:18]

            data = Data()

            data.InitFromRaw(rawData[dataOffset + currentOffset : dataOffset + currentOffset + itemSize], itemFlags)

            self.data.append(data)

            currentOffset += itemSize

        pass

    def GetFreeSpaceSize(self) -> int:

        return self.DATABLOCK_MAX_SIZE - len(self.ToBytes(False))

    def ToBytes(self, fill : bool = True):

        blockAddress = bytes([self.address // 256]) + bytes([self.address %  256])

        numberOfData = len(self.data).to_bytes(1, byteorder=sys.byteorder)

        hexTable  = bytes()

        hexData   = bytes()

        for i in range(0, len(self.data)):

            itemSize  = len(self.data[i].ToBytes())

            binItemSize  = bin(itemSize)[0:2] + bin(itemSize)[2:].zfill(12)

            isFragBin      = bin(self.data[i].isFragmented)[2:]
            isFirstFragBin = bin(self.data[i].isFirst)[2:]

            flags = (isFragBin + isFirstFragBin).zfill(4)

            hexTableEntry = int('0b' + binItemSize[10:14] + flags, 2).to_bytes(1, byteorder=sys.byteorder) + \
                            int(binItemSize[0:10], 2).to_bytes(1, byteorder=sys.byteorder)

            hexTable += hexTableEntry

            hexData  += self.data[i].ToBytes()

        totaldata = blockAddress + numberOfData + hexTable + hexData

        byteChunk = ""

        if fill:
            for i in range(len(totaldata), self.DATABLOCK_MAX_SIZE+1):
                byteChunk += "x"

            return totaldata + byteChunk.encode('utf-8')[1:]

        return totaldata

    def DebugInfo(self):

        print("Bytes: ")
        print(self.ToBytes())
        print("stored values: Data and Address ")
        for data in self.data:
            data.DebugInfo()
        print(self.address)

