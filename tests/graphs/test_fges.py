import os
import unittest
import numpy as np
import pandas as pd
from pyrca.graphs.causal.fges import FGES


class TestFGES(unittest.TestCase):

    def test(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        data = np.loadtxt(os.path.join(directory, "../data/data_linear.txt"), skiprows=1)
        try:
            from pyrca.thirdparty.causallearn.utils.TXT2GeneralGraph import txt2generalgraph
            graph = txt2generalgraph(os.path.join(directory, "../data/graph.txt"))
            df = pd.DataFrame(data, columns=[f"X{i}" for i in range(1, 21)])
            graph = pd.DataFrame((graph.graph < 0).astype(int), columns=df.columns, index=df.columns)
            model = FGES(FGES.config_class())
            r = model.train(df)
        except (ImportError, AssertionError) as e:
            print(str(e))
            return
        diff = np.sum(np.abs(r.values - graph.values))
        self.assertLessEqual(diff, 6)


if __name__ == "__main__":
    unittest.main()
