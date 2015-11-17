__author__ = 'Gabriel'

import sys
import json

from Buffer import Buffer
from Data   import Data

class Control:

    def __init__(self) -> None:

        "Start the Main info Here (LIKE THE CURRENT_BLOCK_INDEX"

        self.currentBlockIndex = 0
        self.buffer = Buffer()
        self.fileId = 0

        pass

    def LoadAndWriteJSON(self, filenames, targetDataBlock = 0) -> None:

        for filename in filenames:

            with open(filename, "rb") as f:

                dataRaw = f.read()

                self.StoreJSONFile(self.fileId, dataRaw)

                self.fileId += 1

                #self.buffer.WriteOnDataBlock(targetDataBlock, dataRaw)

        pass

    def StoreJSONFile(self, fileId : int, jsonFile) -> None:

        data = Data()

        data.InitFromBuffer(fileId, jsonFile.decode(), False, True)

        dataBlock = self.buffer.GetDataBlock(self.currentBlockIndex)

        while True:

            if dataBlock.GetFreeSpaceSize() < data.GetLenght():

                dividedData = data.Split(dataBlock.GetFreeSpaceSize(), self.GetNextFreeDataBlock())

                self.buffer.WriteOnDataBlock(self.currentBlockIndex, dividedData[0])

                self.currentBlockIndex = self.GetNextFreeDataBlock()

                dataBlock = self.buffer.GetDataBlock(self.currentBlockIndex)

                data = dividedData[1]

            else:

                if data.isFragmented:
                    data.nextDatablock = None

                self.buffer.WriteOnDataBlock(self.currentBlockIndex, data)

                break

    def SaveBeforeQuit(self):

        self.buffer.SaveAllToDataFile()

    def GetNextFreeDataBlock(self) -> int:

        return self.currentBlockIndex + 1

    def EraseDatafile(self):

        self.buffer.EraseDatafile()

    def PrintDataBlock(self, target : int):

        self.buffer.PrintDatablock(target)