#!/usr/bin/python3
"""
One loader for all datasets!
"""

from  dataset_session_5.loaderSession5 import datasetSession5
import numpy as np

dataset_session_5_filename='dataset_session_5/output.csv'

def main():
    data_session_5 = datasetSession5.loadSession5(dataset_session_5_filename)
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

    # Plot data
    # datasetSession5.showData(values, save_fname='full.png')
    # datasetSession5.showData(values, rng=(0,5000), save_fname='first5000.png')

if __name__ == '__main__':
    main()
