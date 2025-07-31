import os
from utils.interpolation import interpolator_stationary

def tos2ca_interpolation_stationary_driver(jobID, chunkID):

    print('Running interpolation for %s-%s' % (jobID, chunkID))
    interpolator_stationary(int(jobID), int(chunkID))
    print("Job complete")

    return

if __name__ == '__main__':

    tos2ca_interpolation_stationary_driver(os.environ['JOBID'], os.environ['CHUNKID'])
