__author__ = 'Gabriel'
import sys
import Main

def AddFileToDatafile() -> None:

    Main.LoadAndWriteJSON(0)

    pass

def DeleteDatafile() -> None:

    Main.EraseDatafile()

    pass

def Quit() -> None:

    sys.exit()
    pass

UIOptions = { 1 : AddFileToDatafile, 1138 : DeleteDatafile, "q" : Quit }

def PrintUserOptions() -> None:

    print("Opcoes:")

    for option in UIOptions.items():
        print("---")
        print(str(option[0]) + " - " + option[1].__name__)

    print("---")
    pass

def GetUserInput() -> None:

    PrintUserOptions()

    while True:

        user_input = input("Select operation...")

        print(user_input)

        if user_input is not None:

            try:
                UIOptions[int(user_input)]()

            except KeyError:

                print("***********")
                print("Invalid Option!!! Please select one of the following options")
                print("***********")

                PrintUserOptions()

    pass

GetUserInput()