#!/usr/bin/python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

filename='driving_log.csv'
#
# | filename | empty | empty | steering | throttle | brakes | speed | Pos X:Y:Z | Rot X:Y:Z |
# |----------|-------|-------|----------|----------|--------|-------|----------------|----------------|
# | IMG/center_2017_03_06_21_15_27_656.jpg | | | 0.07247914 | 0.7352967 | 0 | 0.6671922 | 1239.393:754.3097:29.65825 | 356.0383:175.2307:0.3258028 |


class dataset001:
    def load001(csvfname):
        """
        Load dataset from csv file
        """
        data=[]
        with open(csvfname, 'r') as csvfile:
            data_tmp = list(csv.reader(csvfile, delimiter=','))
            for row in data_tmp:
                x7=[float(x) for x in row[7].split(':')]
                x8=[float(x) for x in row[8].split(':')]

                data.append(((row[0],row[1],row[2]),np.array([float(row[3]),float(row[4]),float(row[5]),float(row[6])]+x7+x8)))
        return data

    def showData(data, rng=[0,-1], show_plot=False, save_fname=None):
        f, ((ax1, ax2, ax3,ax4),(ax5, ax6,ax7,ax8),(ax9, ax10,ax11,ax12)) = plt.subplots(3, 4)
        ax1.plot(data[rng[0]:rng[1],0],'r')
        ax1.set_title('Steering')
        ax2.plot(data[rng[0]:rng[1],1],'g')
        ax2.set_title('Throttle')
        ax3.plot(data[rng[0]:rng[1],2],'b')
        ax3.set_title('Brakes')
        ax4.plot(data[rng[0]:rng[1],3],'k')
        ax4.set_title('Speed')
        ax5.plot(data[rng[0]:rng[1],4],'r')
        ax5.set_title('Pos X')
        ax6.plot(data[rng[0]:rng[1],5],'g')
        ax6.set_title('Pos Y')
        ax7.plot(data[rng[0]:rng[1],6],'b')
        ax7.set_title('Pos Z')
        ax8.plot(data[rng[0]:rng[1],7],'k')
        ax8.set_title('Rot X')
        ax9.plot(data[rng[0]:rng[1],8],'r')
        ax9.set_title('Rot Y')
        ax10.plot(data[rng[0]:rng[1],9],'g')
        ax10.set_title('Rot Z')

        ax11= f.add_subplot(3,4,11, projection= '3d')
        ax12= f.add_subplot(3,4,12, projection= '3d')

        ax11.scatter(data[rng[0]:rng[1],4],data[rng[0]:rng[1],5],data[rng[0]:rng[1],6])
        ax11.set_title('3D position')
        ax12.scatter(data[rng[0]:rng[1],7],data[rng[0]:rng[1],8],data[rng[0]:rng[1],9])
        ax12.set_title('3D rotation')

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
        ax7.set_xticks(_rng)
        ax7.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax8.set_xticks(_rng)
        ax8.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax9.set_xticks(_rng)
        ax9.set_xticklabels([str(x) for x in _rng], rotation=30)
        ax10.set_xticks(_rng)
        ax10.set_xticklabels([str(x) for x in _rng], rotation=30)

        if not save_fname is None:
            plt.savefig(save_fname, dpi=300)
        if show_plot:
            plt.show()

def main():
    data_001 = dataset001.load001(filename)
    print('='*40)
    print('='*8,'dataset 001','='*8)
    print('='*40)
    print('Records count: ',len(data_001))
    print('First row: ',data_001[0])

    #split to images, values
    images, values = zip(*data_001)
    values = np.array(values)

    print('Images len: ',len(images))
    print('Images first row: ',images[0])
    print('Values shape: ',values.shape)
    print('Values first row: ',list(values[0]))
    print('Min values:', ['%.3f'%x for x in list(np.amin(values, axis=0))])
    print('Max values:', ['%.3f'%x for x in list(np.amax(values, axis=0))])

    dataset001.showData(values, save_fname='full.png',show_plot=True)
    dataset001.showData(values, rng=(0,5000), save_fname='first5000.png')

if __name__ == '__main__':
    main()
