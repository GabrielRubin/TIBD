__author__ = 'Gabriel'

import DataIO as IO
from DataBlock import DataBlock

BUFFER_MAX_SIZE = 256

buffer     = []
bufferSize = 0

def LoadDataToBuffer(dataBlockAddress: int) -> None:

    data = IO.LoadDataBlock(dataBlockAddress, True)

    dataBlock = DataBlock(data)

    if bufferSize >= BUFFER_MAX_SIZE:
        DiscardFrame()

    buffer.append(dataBlock)

    print(dataBlock)

    return dataBlock

def GetDataBlockFromBuffer(dataBlockAddress: int) -> DataBlock:

    for i in range(0, len(buffer)):

        if buffer[i].address == dataBlockAddress:

            return buffer[i]

    #Datablock not found
    return LoadDataToBuffer(dataBlockAddress)

def WriteOnDataBlock(dataBlockAddress: int, data) -> None:

    dataBlock = GetDataBlockFromBuffer(dataBlockAddress)

    dataBlock.data.append(data)

    SaveDataBlockToDataFile(dataBlock)

    pass

def SaveDataBlockToDataFile(dataBlock: DataBlock) -> None:

    IO.WriteToDataFile(dataBlock.ToBytes(), dataBlock.address)

def DiscardFrame() -> None:

    pass

#LoadDataToBuffer(0)