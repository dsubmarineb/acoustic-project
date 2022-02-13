import sys
import simpleaudio
import pyaudio

def main():
    print("Hello")
    print(sys.argv[0])
    print(sys.argv[1])

    fileName = input("Enter audio file name: ")
    print(f'Processing "{fileName}"')
    makePlot(fileName)


def makePlot(fileName: str):
    print("Making plot")
    return

main()