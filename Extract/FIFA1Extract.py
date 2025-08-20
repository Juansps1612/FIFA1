import requests 
import pandas as pd 
import numpy as np 
class NvidiaExtract:
 def _init_(self,csv_path):
  self.csv=csv_path
 def querries(self):
  data=pd.read_csv(self.csv)
 def response():
  return data.head(5)