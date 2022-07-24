from typing import List
from pandas import DataFrame, Series, Timestamp
import yfinance as yf
from alphabot.models import DailyPrice, Symbol

class DailyPriceModel():

  def __init__(self) -> None:
    self._tableName = 'alphabot_dailyprice'

  def getHistoricalDataFrame(self, ticker: str, period: str) -> DataFrame:
    self._symbol = ticker
    tickerObject = yf.Ticker(ticker)
    return tickerObject.history(period)

  def saveRecords(self, dataFrame: DataFrame) -> bool:
    for index, row in dataFrame.iterrows():
      self.saveRecord(index, row)
    return True
  
  def saveRecord(self, priceDate: Timestamp, data: Series) -> bool:
    symbolId = Symbol.objects.get(symbol = self._symbol).id
    dailyPrice = DailyPrice(
      date = priceDate.tz_localize('EST'),
      open = data.values[0],
      high = data.values[1],
      low = data.values[2],
      close = data.values[3],
      volume = data.values[4],
      dividends = data.values[5],
      stock_splits = data.values[6],
      symbol_id = symbolId
    )
    dailyPrice.save()
    return True
