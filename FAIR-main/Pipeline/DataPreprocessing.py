import luigi
from Pipeline.DataLoading import LoadDataTask
import pandas as pd

class PreprocessDataTask(luigi.Task):
    def requires(self):
        return LoadDataTask()

    def output(self):
        return luigi.LocalTarget("Data/dataprocess_stage_output.csv")

    def run(self):
        dataFrame = pd.read_csv("Data/dataload_stage_output.csv")
        dataFrame.dropna()
        dataFrame.to_csv(self.output().path, index=False)

