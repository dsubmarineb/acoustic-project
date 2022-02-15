import sys
from tracemalloc import stop
import simpleaudio
import pyaudio
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Hello")
    print(sys.argv[0])
    # print(sys.argv[1])

    # fileName = input("Enter audio file name: ")
    # print(f'Processing "{fileName}"')

    x1, y1 = makeWave(1, 1)
    x2, y2 = makeWave(2, 1)
    x3, y3 = makeWave(3, 1)

    plt.plot(x1, y1, label='1')
    plt.plot(x2, y2, label='2')
    plt.plot(x3, y3, label='3')
    plt.legend()
    plt.show()

    
    # makePlot(fileName)


# def makePlot(fileName: str):
#     print("Making plot")
#     return

def makePlot(x, y):
    plt.plot(x, y)
    plt.show()

    return

def makeWave(frequency: float, cycles: float) -> tuple[np.ndarray, np.ndarray]:
    print("Making wave")
    print(f"Frequency: {frequency}")
    print(f"Cycles: {cycles}")
    omega = 2*np.pi*frequency
    period = 1/frequency
    # x = np.arange(0, period*cycles, period/10)

    end = period*cycles
    x = np.linspace(0, end, num=int(end*cycles*100))
    y = np.sin(omega*x)

    return (x, y)


main()