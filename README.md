# financial-dashboards
Creating a series of financial dashboards based on IN and OUT documents

Using streamlit, pandas and other data modeling packages. Documentation will come later on.

# Core Documents
We will base all the financial dashboards on two documents, IN(income) and OUT(expenses), as follows:

**1. Income Receivables (IN)**
- Money that you expect to receive from sales, services, or other income sources.
- Columns for this document:
  - Issue Date
  - Invoice/Receipt Number
  - Client Name
  - Description (Project)
  - Quantity
  - Unit Price
  - Currency
  - Amount
  - VAT
  - Total Amount
  - Status
  - Paid Date
  - Category
  - Type
  - Payment Method

**2. Expense Payables (OUT)**
- Amounts that you owe for expenses incurred but not yet paid.
- Columns for this document
  - Payment Date
  - Invoice/Receipt Number
  - Supplier Name
  - Currency
  - Amount
  - Due Date
  - Category
  - Description