__author__ = 'Gabriel'
import sys
from tkinter import *
from tkinter import filedialog
import Main

def OpenFileDialog():

    root = Tk()

    value = filedialog.askopenfilenames(parent = root, title='Select JSON files')

    root.destroy()

    return value

def AddFileToDatafile() -> None:

    print("select the datablock")

    value = GetUserInputNumber(0, Main.DataIO.DATAFILE_MAX_DATABLOCKS)

    filenames = OpenFileDialog()

    Main.LoadAndWriteJSON(filenames, value)

    pass

def CheckDataBlockContent () -> None:

    value = GetUserInputNumber(0, Main.DataIO.DATAFILE_MAX_DATABLOCKS)

    print("\n*** BLOCK INFO ***\n")

    Main.PrintDatablockInfo(value)

    print("\n******************")

    pass

def DeleteDatafile() -> None:

    Main.EraseDatafile()

    pass

def Quit() -> None:

    sys.exit()
    pass

UIOptions = { 1 : AddFileToDatafile, 2 : CheckDataBlockContent, "delete" : DeleteDatafile, "q" : Quit }

def PrintUserOptions() -> None:

    print("Options:")

    for option in UIOptions.items():
        print("---")
        print(str(option[0]) + " - " + option[1].__name__)

    print("---")
    pass

def GetUserInputNumber(fromValue : int, toValue : int) -> int:

    while True:
        try:
            value = int(input("Enter a value from {0} to {1} ....".format(fromValue, toValue)))
            if value < fromValue or value > toValue:
                print("Invalid value! This value is not valid!")
            else:
                return value
        except ValueError:
            print("Invalid value! This is not a number!")
            continue

    return None

def GetUserInput() -> None:

    while True:

        print("---------------------------------")

        PrintUserOptions()

        user_input = input("Select operation... ")

        if user_input is not None:

            try:
                try:
                    value = int(user_input)
                except ValueError:
                    value = user_input

                UIOptions[value]()

            except KeyError:

                print("***********")
                print("Invalid Option!!! Please select one of the following options")
                print("***********")

    pass

GetUserInput()