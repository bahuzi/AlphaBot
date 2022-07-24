from typing import List
import json, os
from alphabot.models import Symbol

class SymbolModel():

  def __init__(self) -> None:
    self._tableName = 'alphabot_symbol'

  def readFile(self, path: str) -> List:
    file = open(path,"r")
    data = file.read()
    file.close()
    return data
  
  def readJson(self, fileName: str, path: str) -> List:
    self._exchange = fileName[0:4]
    return json.loads(self.readFile(path+"/"+fileName))

  def saveRecords(self, data: List) -> bool:
    for value in data:
      self.saveRecord(value)
    return True
  
  def saveRecord(self, data: dict) -> bool:
    symbol = Symbol(
      symbol = data.get("symbol"),
      name = data.get("name"),
      country = data.get("country"),
      exchange = self._exchange,
      industry = data.get("industry"),
      sector = data.get("symsectorbol"),
    )
    symbol.save()
    return True
