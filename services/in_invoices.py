from dataclasses import dataclass
from typing import Optional

@dataclass
class Invoice:
    id: int
    date: str
    name: str
    amount: float

    def import_file(self):
        print(f"Importing {self.name} receivable...")


@dataclass
class Payable(Invoice):
    due_date: str
    description: Optional[str] = None