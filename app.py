import pandas as pd
from services.in_invoices import Payable
from services.out_invoices import Receivable, Receipt

in_payables = Payable(id=1,
                      date='2021-01-01',
                      name='ABC Corporation',
                      amount=1920.40,
                      description='Project X',
                      due_date='2021-01-31')

print(in_payables)