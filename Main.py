__author__ = 'Gabriel'

import sys
import json
from Buffer import WriteOnDataBlock
import DataIO

FreeDataBlockIndex = 0

def LoadAndWriteJSON(filenames, targetDataBlock = 0) -> None:

    for filename in filenames:

        with open(filename, "rb") as f:

            dataRaw = f.read()

            WriteOnDataBlock(targetDataBlock, dataRaw)

    pass

def PrintDatablockInfo(address : int):

    DataIO.LoadDataBlock(address, True)

    pass

def EraseDatafile():

    DataIO.EraseAllData()

    pass