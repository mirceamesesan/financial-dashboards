from dataclasses import dataclass
from typing import Optional

@dataclass
class Invoice:
    id: int
    date: str
    name: str
    amount: float


@dataclass
class Receivable(Invoice):
    due_date: str
    description: Optional[str] = None


@dataclass
class Receipt(Invoice):
    paid_date: str
    description: Optional[str] = None