from unittest import TestCase
import numpy as np 
import pandas as pd
import yfinance as yf


from alphabot.MachineLearningEngine.SupervisedLearning.Perceptron import Perceptron

class TestPerceptron(TestCase):
  def test_perceptron(self):
    model = Perceptron()
    s = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    df = pd.read_csv(s, header=None, encoding="utf-8")
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)
    X = df.iloc[0:100, [0, 2]].values
    model.fit(X, y)
    result = model.predict(X)
    # spy = yf.Ticker("SPY")
    # print(spy.info.get("holdings"))
    # # print(type(spy.info.get("holdings")))
    # print(len(spy.info.get("holdings")))
    # for value in spy.info.get("holdings"):
    #   print(value.get("symbol"))
    baba = yf.Ticker("BABA")
    print(baba.info)
    self.assertEqual(100, result.size)