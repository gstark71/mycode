import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 7
    localnetMeans = (20, 35, 30, 35, 40, 45, 50) #LAN length of outage (mins)
    wanMeans = (25, 32, 34, 20, 27, 39, 15) #WAN length of outage (min)
    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.75

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4", "Q5", "Q7", "Q7"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/2018summaryGS.pdf")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/2018summaryGS.pdf")

if __name__ == "__main__":
    main()
print("Script complete!")
