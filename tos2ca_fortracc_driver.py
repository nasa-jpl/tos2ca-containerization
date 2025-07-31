import os
from utils.fortracc import callFortraccSparse

def fortracc_driver(jobID, chunkID):

    print('Running ForTraCC for %s-%s' % (jobID, chunkID))
    callFortraccSparse(jobID, chunkID)
    print("Job complete")

    return

if __name__ == '__main__':

    fortracc_driver(os.environ['JOBID'], os.environ['CHUNKID'])
