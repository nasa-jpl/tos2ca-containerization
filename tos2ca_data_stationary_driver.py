import os
import json
from database.connection import openDB, closeDB
from database.queries import getJobInfo, updateStatus

def tos2ca_data_stationary_driver(jobID, chunkID):
        
    # Open the database connection and get the info for this chunkedJobID
    db, cur = openDB()
    print(cur)

    info = getJobInfo(cur, jobID, chunkID)[0]
    print(info)
    # Load in the data dictionary that tells which reader to use
    with open('/data/code/data-dictionaries/tos2ca-data-collection-dictionary.json') as j:
        dataDict = json.load(j)
    curator = dataDict[info['dataset']]['curator']  

    print("Running curation: %s-%s using: %s_stationary" % (jobID, chunkID, curator))

    if curator == "gpm_curator":
        from iolib.gpm import gpm_curator_stationary
        gpm_curator_stationary(jobID, chunkID)
    elif curator == "merra2_curator":
        from iolib.merra2 import merra2_curator_stationary
        merra2_curator_stationary(jobID, chunkID)
    else:
        updateStatus(db, cur, jobID, 'failed', chunkID=chunkID)
        exit('No available curator.')
    print("Job complete")
        
    closeDB(db)

    return

if __name__ == '__main__':

    tos2ca_data_stationary_driver(os.environ['JOBID'], os.environ['CHUNKID'])    
