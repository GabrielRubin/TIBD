__author__ = 'Gabriel'

import DataIO
from DataBlock import DataBlock

class Buffer:

    def __init__(self):

        self.BUFFER_MAX_SIZE = 256

        self.dataBlockArray = []

    def SelectFrameToDiscard(self) -> int:

        #TODO: CLOCK discard

        selected = 0

        dataBlock = self.GetDataBlock(selected)

        DataIO.WriteToDataFile(dataBlock.ToBytes(), dataBlock.address)

        pass

    def LoadDataToBuffer(self, dataBlockAddress: int) -> DataBlock:

        data = DataIO.LoadDataBlock(dataBlockAddress, True)

        dataBlock = DataBlock(data)

        if len(self.dataBlockArray) >= self.BUFFER_MAX_SIZE:

            framePos = self.SelectFrameToDiscard()

            self.dataBlockArray[framePos] = dataBlock

        else:
            self.dataBlockArray.append(dataBlock)

        return dataBlock

    def GetDataBlock(self, dataBlockAddress: int) -> DataBlock:

        for i in range(0, len(self.dataBlockArray)):

            if self.dataBlockArray[i].address == dataBlockAddress:

                return self.dataBlockArray[i]

        return self.LoadDataToBuffer(dataBlockAddress)

    def WriteOnDataBlock(self, dataBlockAddress: int, data) -> None:

        dataBlock = self.GetDataBlock(dataBlockAddress)

        dataBlock.data.append(data)

        pass

    def SaveAllToDataFile(self) -> None:

        for dataBlock in self.dataBlockArray:

            DataIO.WriteToDataFile(dataBlock.ToBytes(), dataBlock.address)

    def PrintDatablock(self, datablockAddress : int) -> None:

        data = self.GetDataBlock(datablockAddress)
        data.DebugInfo()

    def EraseDatafile(self):

        DataIO.EraseAllData()