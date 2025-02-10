from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json


class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def file_loader_1_change(self, file, **event_args):
    text = file.get_bytes()
    data = json.loads(text)
    anvil.server.call('save_data', 'key', data)
    alert('The file has been uploaded and saved to table')

  def button_1_click(self, **event_args):
    data = anvil.server.call('get_data', 'key')
    print(type(data))
    alert('The value read from the table is: {}'.format(data))

  def upload_sdg_var_change(self, file, **event_args):
    text = file.get_bytes()
    print(type(text))
    tsplit = text.splitlines(keepends=False)
    print(type(tsplit))
    anvil.server.call('upload_sdg_var_change', tsplit)
    alert('The file has been uploaded and saved to table')
