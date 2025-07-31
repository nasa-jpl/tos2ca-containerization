import os
from utils.plot import mask_plot

def plot_driver(jobID, chunkID):

    print('Running plots for %s-%s' % (jobID, chunkID))
    mask_plot(jobID, chunkID)
    print("Job complete")

    return

if __name__ == '__main__':

    plot_driver(os.environ['JOBID'], os.environ['CHUNKID'])
