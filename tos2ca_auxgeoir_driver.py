import os
from utils.auxgeoir import callAuxGeoIRSparse

def auxgeoir_driver(jobID, chunkID):

    print('Running AUX-GEOIR for %s-%s' % (jobID, chunkID))
    callAuxGeoIRSparse(jobID, chunkID)
    print("Job complete")

    return

if __name__ == '__main__':

    auxgeoir_driver(os.environ['JOBID'], os.environ['CHUNKID'])
