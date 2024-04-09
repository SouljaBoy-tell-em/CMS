import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy.signal import savgol_filter, find_peaks


class COORD:
    def __init__(self, x, y):
        self.x = x
        self.y = y


Y = None
X = None


def AVARAGE_MEANING(list):
    return (list[0] + list[len(list) - 1]) / 2

def APPROXIMATE(X, Y):
    listX = np.array(X)
    listY = np.array(Y)

    dif = listY - AVARAGE_MEANING(listX)
    difMax = np.max(dif)
    difMin = np.min(dif)
    guess = np.array([(difMax - difMin) / 2,
                     2 * np.pi * abs(np.fft.fftfreq(len(listX),
                    (listX[1] - listX[0]))[np.argmax(abs(np.fft.fft(listY))[1:]) + 1]),
                     0,
                     np.mean(listY)]
                    )

    def SIN(t, A, w, p, c):
        return A * np.sin(w * t + p) + c

    popt, pcov = scipy.optimize.curve_fit(SIN, listX, listY, p0=guess)
    A, w, p, c = popt
    f = w / (2 * np.pi)
    fitfunc = lambda t: A * np.sin(w * t + p) + c
    return {"amp": A,
            "omega": w,
            "phase": p,
            "offset": c,
            "freq": f,
            "period": 1 / f,
            "fitfunc": fitfunc,
            "maxcov": np.max(pcov),
            "rawres": (guess, popt, pcov)
            }

def CHECK_DIFFERENCE(indexes, number, DIF_PARAM):

    sum = 0
    for i in range(0, len(indexes), 1):
        sum = sum + indexes[i].y

    if(abs((sum / len(indexes)) - number) >= DIF_PARAM):
        return False

    for i in range(0, len(indexes), 1):
        if(abs(indexes[i].y - number) >= DIF_PARAM):
            return False;

    return True

def DETECT_IDLE_AREA(Y):
    awesome_indexes = []
    save_indexes = []

    for i in range(0, len(Y), 1):
        if(len(save_indexes) == 0):
            save_indexes.append(COORD(i, Y[i]))
            continue

        if(CHECK_DIFFERENCE(save_indexes, Y[i], 1) == True):
            save_indexes.append(COORD(i, Y[i]))
            continue

        if(len(save_indexes) > 1):
            awesome_indexes.extend(save_indexes)
        save_indexes = []

    return awesome_indexes
def DETECT_MAX_EXTREMUMS(Y):
    max_peaks, properties = find_peaks(Y)
    return max_peaks

def DETECT_MIN_EXTREMUMS(Y):
    min_peaks, properties = find_peaks(-Y)
    return min_peaks

def GET_COORDS(coords):
    listX = []
    listY = []
    for i in range(0, len(coords), 1):
        listX.append(coords[i].y)
        listY.append(coords[i].x)
    return listX, listY


def INITIALIZE(file):
    global X, Y
    Y = np.load(file, allow_pickle=True)
    X = np.arange(len(Y))
def SAVGOL_INIT(Y):
    return savgol_filter(Y, 51, 3)



INITIALIZE('pu-l3.npy')
figure, axis = plt.subplots(5, 1)

axis[0].plot(X, Y)
axis[0].scatter(DETECT_MAX_EXTREMUMS(Y),
            Y[DETECT_MAX_EXTREMUMS(Y)],
            color='g', label='local maximums')
axis[0].scatter(DETECT_MIN_EXTREMUMS(Y),
            Y[DETECT_MIN_EXTREMUMS(Y)],
            color='r', label='local minimums')
axis[0].legend()

Y_new = SAVGOL_INIT(Y)
axis[1].plot(X, Y_new)
axis[1].scatter(DETECT_MAX_EXTREMUMS(Y_new),
            Y_new[DETECT_MAX_EXTREMUMS(Y_new)],
            color='g', label='local maximums')
axis[1].scatter(DETECT_MIN_EXTREMUMS(Y_new),
            Y_new[DETECT_MIN_EXTREMUMS(Y_new)],
            color='r', label='local minimums')

listX, listY = GET_COORDS(DETECT_IDLE_AREA(Y))
axis[2].plot(X, Y)
axis[2].scatter(listY, listX, color='orange', label='idle areas')

Y_new = savgol_filter(Y + np.sin(X), 100, 4)
axis[3].plot(X, Y_new)

axis[4].plot(X, Y)
axis[4].plot(X, APPROXIMATE(X, Y)["fitfunc"](X), "r", linewidth=2)

plt.show()
