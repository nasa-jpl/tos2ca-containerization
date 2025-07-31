import os
import json
from database.connection import openDB, closeDB
from database.queries import getJobInfo, updateStatus

def tos2ca_data_driver(jobID, chunkID):
        
    # Open the database connection and get the info for this chunkedJobID
    db, cur = openDB()
    print(cur)

    info = getJobInfo(cur, jobID, chunkID)[0]
    print(info)
    if info["stage"] == "curation":
        # Load in the data dictionary that tells which reader to use
        with open('/data/code/data-dictionaries/tos2ca-data-collection-dictionary.json') as j:
            dataDict = json.load(j)
        curator = dataDict[info['dataset']]['curator']  

        print("Running curation: %s-%s using: %s" % (jobID, chunkID, curator))

        if curator == "ascat_curator":
            print('ASCAT data cannot currently be run in a container')
            updateStatus(db, cur, jobID, 'failed', chunkID=chunkID)
        elif curator == "ecco_curator":
            from iolib.ecco import ecco_curator
            ecco_curator(jobID, chunkID)
        elif curator == "gpm_curator":
            from iolib.gpm import gpm_curator
            gpm_curator(jobID, chunkID)
        elif curator == "merra2_curator":
            from iolib.merra2 import merra2_curator
            merra2_curator(jobID, chunkID)
        elif curator == "oscar_curator":
            from iolib.oscar import oscar_curator
            oscar_curator(jobID, chunkID)
        else:
            updateStatus(db, cur, jobID, 'failed', chunkID=chunkID)
            exit('No available curator.')
    else:
        # Load in the data dictionary that tells which reader to use
        with open('/data/code/data-dictionaries/tos2ca-phdef-dictionary.json') as j:
            dataDict = json.load(j)
        reader = dataDict[info['dataset']]['reader']

        print("Running phdef: %s-%s using: %s" % (jobID, chunkID, reader))
        
        if reader == 'merra2_reader':
            from iolib.merra2 import merra2_reader
            merra2_reader(jobID, chunkID)
        elif reader == 'gpm_reader':
            from iolib.gpm import gpm_reader
            gpm_reader(jobID, chunkID)
        elif reader == 'ecco_reader':
            from iolib.ecco import ecco_reader
            ecco_reader(jobID, chunkID)
        elif reader == 'mur_reader':
            from iolib.mur import mur_reader
            mur_reader(jobID, chunkID)
        elif reader == 'sea_surface_reader':
            from iolib.sea_surface import sea_surface_reader
            sea_surface_reader(jobID, chunkID)
        elif reader == 'oisss_reader':
            from iolib.oisss import oisss_reader
            oisss_reader(jobID, chunkID)
        else:
            updateStatus(db, cur, jobID, 'failed', chunkID=chunkID)
            exit('No available reader.')

    print("Job complete")
        
    closeDB(db)

    return

if __name__ == '__main__':

    tos2ca_data_driver(os.environ['JOBID'], os.environ['CHUNKID'])    
