import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

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
def upload_sdg_var_change(value):
#  row = app_tables.sdg_vars.get(key=key)
  # Convert JSON String to Python
  print(value)
  print(type(value))
  vd = json.loads(value)
  # Print Dictionary

  print(vd[0]['vensim_name'])
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
