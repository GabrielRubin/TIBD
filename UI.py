__author__ = 'Gabriel'
import sys
from tkinter import *
from tkinter import filedialog
from Control import Control

DATABLOCK_MAX_SIZE      = 4096
DATAFILE_MAX_DATABLOCKS = 65536

class UI:

    def __init__(self):

        self.UIOptions = { 1 : self.AddFileToDatafile, 2 : self.CheckDataBlockContent, "delete" : self.DeleteDatafile, "s" : self.SaveAllChanges, "q" : self.Quit }

        self.control = Control()

    def AddFileToDatafile(self) -> None:

        #print("select the datablock")

        #value = self.GetUserInputNumber(0, DATAFILE_MAX_DATABLOCKS)

        root = Tk()

        filenames = filedialog.askopenfilenames(parent = root, title='Select JSON files')

        print(filenames)

        root.destroy()

        self.control.LoadAndWriteJSON(filenames, filenames)

    def CheckDataBlockContent (self) -> None:

        value = self.GetUserInputNumber(0, DATAFILE_MAX_DATABLOCKS)

        print("\n*** BLOCK INFO ***\n")

        self.control.PrintDataBlock(value)

        print("\n******************")

    def SaveAllChanges(self) -> None:

        print("Saving data...")

        self.control.SaveBeforeQuit()

        print("DONE.")

    def DeleteDatafile(self) -> None:

        self.control.EraseDatafile()

    def Quit(self) -> None:

        self.SaveAllChanges()

        print("Bye bye!")

        sys.exit()

    def PrintUserOptions(self) -> None:

        print("Options:")

        for option in self.UIOptions.items():
            print("---")
            print(str(option[0]) + " - " + option[1].__name__)

        print("---")

    def GetUserInputNumber(self, fromValue : int, toValue : int) -> int:

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

    def GetUserInput(self) -> None:

        while True:

            print("---------------------------------")

            self.PrintUserOptions()

            user_input = input("Select operation... ")

            if user_input is not None:

                try:
                    try:
                        value = int(user_input)
                    except ValueError:
                        value = user_input

                    self.UIOptions[value]()

                except KeyError:

                    print("***********")
                    print("Invalid Option!!! Please select one of the following options")
                    print("***********")