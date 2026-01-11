import math
from os import path
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    prob_name = "STS-07vC10Ra" ##FBS-04O7" ##02CartonPacks" ##01Slaughterhouse" ##STS-05vC10Es" ##FBS-AB20-ar175"  ##"FBS-AB20-ar10"
    file_name = path.dirname(__file__) + "/" + prob_name + ".txt"
    points = np.loadtxt(file_name, delimiter="\t")
    print(points.shape)
    x = np.zeros(5)
    y = np.zeros(5)
    fac_num = (int)(points[0][0])

    for index in range(1,fac_num+1):
        ps = points[index]
        fac = ps[0]
        x[0] = ps[1]
        y[0] = ps[2]
        x[1] = ps[1] + (ps[3] - ps[1]) * 2
        y[1] = y[0]
        x[2] = x[1]
        y[2] = y[0] + (ps[4] - ps[2]) * 2
        x[3] = x[0]
        y[3] = y[2]
        x[4] = x[0]
        y[4] = y[0]
        plt.plot(x, y)
        plt.text((x[2]+x[0])/2, (y[2]+y[0])/2, str(int(fac)))


##    plt.scatter(px,py,marker="*")
    plt.xlabel(prob_name + "--" + str(points[fac_num+1][0]))
    plt.show()

