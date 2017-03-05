#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

filename='output.csv'

# | filename | empty | empty | steering | throttle | brakes | speed | acceleration x | acceleration y |
# |----------|-------|-------|----------|----------|--------|-------|----------------|----------------|
# | images/center_00000000.jpg |  |  | -0.0855263158 | 0 | 0.0436 | 45 | 0.4666666667 | -0.0666666667 |

class datasetSession5:
    def loadSession5(csvfname):
        """
        Load dataset from csv file
        """
        data=None
        with open(csvfname, 'r') as csvfile:
            data = list(csv.reader(csvfile, delimiter=','))
            data = [((x[0],x[1],x[2]),np.array([float(x[3]),float(x[4]),float(x[5]),float(x[6]),float(x[7]),float(x[8])])) for x in data]
        return data

    def showData(data, rng=[0,-1], show_plot=False, save_fname=None):
        f, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2, 3)
        ax1.plot(data[rng[0]:rng[1],0],'r')
        ax1.set_title('Steering')
        ax2.plot(data[rng[0]:rng[1],1],'g')
        ax2.set_title('Throttle')
        ax3.plot(data[rng[0]:rng[1],2],'b')
        ax3.set_title('Brakes')
        ax4.plot(data[rng[0]:rng[1],3],'k')
        ax4.set_title('Speed')
        ax5.plot(data[rng[0]:rng[1],4],'m')
        ax5.set_title('Acceleration X')
        ax6.plot(data[rng[0]:rng[1],5],'y')
        ax6.set_title('Acceleration Y')

        plt.tight_layout(pad=3, w_pad=0.5, h_pad=2.0)

        #fix for calculating number of values
        if rng[1]==-1:
            rng[1]=len(data)

        #5 ticks with labels
        _rng=range(rng[0],rng[1],int((rng[1]-rng[0])/5))
        ax1.set_xticks(_rng)
        ax1.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax2.set_xticks(_rng)
        ax2.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax3.set_xticks(_rng)
        ax3.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax4.set_xticks(_rng)
        ax4.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax5.set_xticks(_rng)
        ax5.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax6.set_xticks(_rng)
        ax6.set_xticklabels([str(x) for x in _rng], rotation=30)

        if not save_fname is None:
            plt.savefig(save_fname, dpi=300)
        if show_plot:
            plt.show()

    #Here data generator will be provided
    # def generator(data):
    #     for image, values in data:
    #         values = np.array(values)
    #         yield

def main():
    data_session_5 = datasetSession5.loadSession5(filename)
    print('='*40)
    print('='*8,'Session 5 dataset info','='*8)
    print('='*40)
    print('Records count: ',len(data_session_5))
    print('First row: ',data_session_5[0])

    #split to images, values
    images, values = zip(*data_session_5)
    values = np.array(values)

    print('Images len: ',len(images))
    print('Images first row: ',images[0])
    print('Values shape: ',values.shape)
    print('Values first row: ',list(values[0]))
    print('Min values:', np.amin(values, axis=0))
    print('Max values:', np.amax(values, axis=0))

    datasetSession5.showData(values, save_fname='full.png')
    datasetSession5.showData(values, rng=(0,5000), save_fname='first5000.png')

if __name__ == '__main__':
    main()
