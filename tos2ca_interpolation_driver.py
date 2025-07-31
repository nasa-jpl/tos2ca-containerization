import os
from utils.interpolation import interpolator

def interpolation_driver(jobID, chunkID):

    print('Running interpolation for %s-%s' % (jobID, chunkID))
    interpolator(int(jobID), int(chunkID))
    print("Job complete")

    return

if __name__ == '__main__':

    interpolation_driver(os.environ['JOBID'], os.environ['CHUNKID'])
