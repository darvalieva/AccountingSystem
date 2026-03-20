class Department:
    """Класс Отдел"""
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_salary_cost(self):
        """Подсчет общих расходов на зарплату в отделе"""
        return sum(emp.salary for emp in self.employees)

    def __str__(self):
        return f"🏢 Отдел: {self.name} | Сотрудников: {len(self.employees)} | ФОТ: {self.get_salary_cost()} руб."