import pandas as pd
from services.payables import Payable, Receipt
from services.receivables import Receivables

in_payables = Payable(id=1,
                      date='2021-01-01',
                      client_name='ABC Corporation',
                      amount=1920.40,
                      description='Project X',
                      due_date='2021-01-31')

print(in_payables)