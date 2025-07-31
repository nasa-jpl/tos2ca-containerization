import os
from utils.ncTools import combineCuratedFiles, combineInterpolatedFiles
from utils.fortracc import stitchFortracc
from database.connection import openDB, closeDB


def combine_driver(jobID):

    db, cur = openDB()
    sql = 'SELECT stage, status FROM jobs WHERE jobID=%s'
    cur.execute(sql, (jobID))
    results = cur.fetchone()
    stage = results['stage']
    status = results['status']
    if stage == 'phdef' and status == 'fortracc':
        stitchFortracc(jobID)
    elif stage == 'curation' and status == 'complete':
        #combineCuratedFiles(jobID)
        combineInterpolatedFiles(jobID)
    else:
        exit('Not sure what to stitch.')
    print("Job complete")
    closeDB(db)

    return


if __name__ == '__main__':

    combine_driver(os.environ['JOBID'])
