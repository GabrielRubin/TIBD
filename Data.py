__author__ = 'Gabriel'
import sys

class Data:

    def __init__(self):

        self.id            = -1
        self.content       = None
        self.isFragmented  = False
        self.isFirst       = True
        self.nextDatablock = None

        pass

    def InitFromRaw(self, rawData, posInfo):

        """

        :param rawData: Raw Data * in Bytes! *
        :param posInfo: Information contained in the datablock * in Bits! *
        """

        self.isFragmented  = bool(int(posInfo[1 : 2])) #  1 bit
        self.isFirst       = bool(int(posInfo[2 : 3])) #  1 bit (o mais da direita)

        if self.isFragmented:

            self.content       = rawData[3 : len(rawData)-4].decode()
            self.nextDatablock = int(rawData[len(rawData) - 4 : len(rawData)], 2)
            if self.isFirst:
                self.id = None
            else:
                self.id = int.from_bytes(rawData[0 : 4], byteorder=sys.byteorder)  # 32 bits - as 4 bytes
        else:

            self.content       = rawData[4 : len(rawData)].decode()
            self.nextDatablock = None
            self.id            = int.from_bytes(rawData[0 : 4], byteorder=sys.byteorder)  # 32 bits - as 4 bytes

        pass

    def InitFromBuffer(self, dataId : int, content : str, isFragmented = False, isFirst = False, nextDataBlock = None):

        self.id      = dataId
        self.content = content
        self.isFragmented  = isFragmented
        self.isFirst       = isFirst
        self.nextDatablock = nextDataBlock

        pass

    def Split(self, currDataBlockMaxSize : int, nextDataBlock : int):

        print("whaaat")

        self.DebugInfo()

        content0 = self.content[0 : currDataBlockMaxSize]

        data0 = Data()
        data1 = Data()

        if self.isFragmented:
            data0.InitFromBuffer(self.id, content0, True, False, nextDataBlock)
        else:
            data0.InitFromBuffer(self.id, content0, True, True, nextDataBlock)

        content1 = self.content[currDataBlockMaxSize : len(self.content)]
        data1.InitFromBuffer(None, content1, True, False, nextDataBlock)

        return (data0, data1)

    def GetLenght(self) -> int:

        if not self.isFragmented and self.isFirst:
            print("ok")
            return len(self.id.to_bytes(4, byteorder=sys.byteorder)[2:]) + len(self.content)

        if not self.isFragmented:
            print("yey")
            return len(self.content)

        if self.isFirst:
            print("wow")
            return len(self.id.to_bytes(4, byteorder=sys.byteorder[2:])) + len(self.content) + len(self.nextDatablock.to_bytes(4, byteorder=sys.byteorder))

        print("derp")

        return len(self.content) + len(self.nextDatablock.to_bytes(4, byteorder=sys.byteorder))

    def ToBytes(self):

        if not self.isFragmented:

            dataId  = self.id.to_bytes(4, byteorder=sys.byteorder)
            content = self.content.encode()

            rawData = dataId + content

            return rawData
        else:
            if self.nextDatablock is not None:
                return self.content.encode() + self.nextDatablock.to_bytes(4, byteorder=sys.byteorder)
            else:
                return self.content.encode()

    def DebugInfo(self) -> None:

        print("data: id = {0}, isFragmented = {1}, isFirstFragment = {2}, nextDataBlock = {3}"
              .format(self.id, self.isFragmented, self.isFirst, self.nextDatablock))

        print("content:")
        print(self.content)
        print("bytes:")
        print(self.ToBytes())