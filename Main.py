__author__ = 'Gabriel'

import sys
import json
from tkinter.filedialog import askopenfilenames
from Buffer import WriteOnDataBlock
import DataIO

FreeDataBlockIndex = 0

def LoadAndWriteJSON(targetDataBlockAddress: int) -> None:

    filenames = askopenfilenames()

    print(filenames)

    '''
    with open(filename, "rb") as f:

        dataRaw = f.read()

        WriteOnDataBlock(targetDataBlockAddress, dataRaw)

        #dataStr = dataRaw.decode()
        #print(dataStr)

        #data
    '''

    pass

def EraseDatafile():

    DataIO.EraseAllData()

    pass