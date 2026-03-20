class Employee:
    """Класс Сотрудник"""
    def __init__(self, full_name, position, salary):
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.status = "Активен"

    def pay_salary(self):
        """Симуляция выплаты зарплаты"""
        return f"💰 Сотруднику {self.full_name} выплачено {self.salary} руб."

    def __str__(self):
        return f"👤 {self.full_name} | {self.position} | {self.salary} руб. | [{self.status}]"