import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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