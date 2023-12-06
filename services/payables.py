from dataclasses import dataclass
from typing import Optional

@dataclass
class Invoice:
    id: int
    date: str
    client_name: str
    amount: float

    def import_file(self):
        print(f"Importing {self.name} receivable...")


@dataclass
class Payable(Invoice):
    due_date: str
    description: Optional[str] = None


@dataclass
class Receipt(Invoice):
    paid_date: str
    description: Optional[str] = None