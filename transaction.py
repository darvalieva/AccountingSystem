class Transaction:
    """Класс Транзакция (Операция)"""
    def __init__(self, t_id, description, amount, t_type, category="Общее"):
        self.t_id = t_id
        self.description = description
        self.amount = amount
        self.t_type = t_type  # 'income' или 'expense'
        self.category = category

    def __str__(self):
        sign = "📈" if self.t_type == 'income' else "📉"
        return f"{sign} Операция #{self.t_id} [{self.category}]: {self.description} ({self.amount} руб.)"