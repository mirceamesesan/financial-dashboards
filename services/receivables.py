from dataclasses import dataclass

@dataclass
class Receivables:
    id: int
    name: str
    amount: float
    date: str
    status: str

    def import_file(self):
        print(f"Importing {self.name} receivable...")