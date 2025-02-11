import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
import pandas as pd
import csv

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def save_data(key, value):
  row = app_tables.mytable.get(key=key)
  if row:
    row.update(value=value)
  else:
    app_tables.mytable.add_row(key=key, value=value)
    
@anvil.server.callable
def get_data(key):
  row = app_tables.mytable.get(key=key)
  return row['value']

@anvil.server.callable
def upload_sdg_var_change(data):
  app_tables.sdg_vars.delete_all_rows()
  l = len(data)
  for i in range(1, l):
    d = data[i]
    d = d.replace('\"', '')
    dro = d.split(',')
    for j in range(0,13):
      print(str(i) + ' ' + str(j) + ' value: ' + dro[j] + ' type: ' + str(type(dro[j])))
    
    app_tables.sdg_vars.add_row(sdg_nbr=float(dro[0]), sdg=dro[1], indicator=dro[2], vensim_name=dro[3], green=float(dro[4]), red=float(dro[5]),
                              lowerbetter=float(dro[6]), ymin=float(dro[7]),ymax=float(dro[8]),subtitle=dro[9],ta=dro[10],pct=float(dro[11]), id=float(dro[12]))
#  app_tables.mytable.add_row(id=id[0], sdg_nbr: sdg_var[0],
#    "sdg": "No poverty",
#    "indicator": "Fraction of population living below $6.85 per day (%)",
#    "vensim_name": "Fraction of population below existential minimum",
#    "green": "5",
#    "red": "13",
#    "lowerbetter": "1",
#    "ymin": "0",
#    "ymax": "65",
#    "subtitle": "Million people living in poverty (Mp)",
#    "ta": "Poverty",
#    "pct": "100",
#    "id": "1"
#  vd = json.
#  if row:
#    row.update(value=value)
#  else:
#    app_tables.mytable.add_row(key=key, value=value)
