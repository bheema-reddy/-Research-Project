import luigi
import pandas as pd
import json
from Pipeline.DataLoading import LoadDataTask
from IgniteConnect import IgniteConnector
import logging
import time

logging.basicConfig(
    filename='apache_ignite.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class StoreInIgniteTask(luigi.Task):

    def getConnection(self):
        self.instance = IgniteConnector()
        self.instance.connect()
        return self.instance.get_client()

    def run(self):
        df = pd.read_csv('Data/1h9t_traj.xyz.gz', compression='gzip', delim_whitespace=True, names=['atoms', 'x', 'y', 'z'], skiprows=2)
        unique_atoms_frame = df.groupby('atoms').agg(lambda x: x.tolist()).reset_index()

        client = self.getConnection()

        dfAsDict = unique_atoms_frame.to_dict(orient='records')
        dfAsDict = {record.pop('atoms'): record for record in dfAsDict}
        cache = client.get_or_create_cache("xyz_trajectory")

        startWrite = time.time()
        for key in dfAsDict.keys():
            cache.put(key, str(dfAsDict[key]))

        endWrite = time.time()

        logging.info("Write Speed = {} secs".format(round(endWrite - startWrite,2)))

        startRead = time.time()
        xyzData = cache.get_all(dfAsDict.keys())
        endRead = time.time()

        logging.info("Data XYZ trajectory")
        logging.info("Read Speed = {} secs".format(round(endRead - startRead,2)))

