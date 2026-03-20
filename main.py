from employee import Employee
from department import Department
from transaction import Transaction
from report import Report


class AccountingSystem:
    """Класс Бухгалтерия Предприятия"""

    def __init__(self, company_name):
        self.company_name = company_name
        self.departments = []
        self.transactions = []
        self.next_trans_id = 1

    def add_department(self, name):
        dept = Department(name)
        self.departments.append(dept)
        return dept

    def add_transaction(self, description, amount, t_type, category="Общее"):
        trans = Transaction(self.next_trans_id, description, amount, t_type, category)
        self.transactions.append(trans)
        self.next_trans_id += 1
        return trans

    def generate_balance_report(self):
        report = Report(f"Финансовый отчет «{self.company_name}»")
        income = sum(t.amount for t in self.transactions if t.t_type == 'income')
        expense = sum(t.amount for t in self.transactions if t.t_type == 'expense')
        report.add_line(f"Доходы: {income} руб.")
        report.add_line(f"Расходы: {expense} руб.")
        report.add_line(f"Чистая прибыль: {income - expense} руб.")

        total_salary = sum(dept.get_salary_cost() for dept in self.departments)
        report.add_line(f"Фонд оплаты труда (ФОТ): {total_salary} руб.")
        report.add_line(f"Всего отделов: {len(self.departments)}")
        report.show()


# === ДЕМОСТРАЦИЯ РАБОТЫ ===
if __name__ == "__main__":
    print("🚀 Запуск информационной системы «Бухгалтерия предприятия»...")
    system = AccountingSystem("КубГТУ Предприятие")

    # 1. Создаем отделы
    print("\n📂 Создание структуры предприятия...")
    dept_it = system.add_department("IT Отдел")
    dept_hr = system.add_department("Отдел кадров")

    # 2. Нанимаем сотрудников
    print("🤝 Прием сотрудников на работу...")
    emp1 = Employee("Иванов И.И.", "Разработчик", 80000)
    emp2 = Employee("Петров П.П.", "Тестировщик", 60000)
    emp3 = Employee("Сидорова А.А.", "HR-менеджер", 55000)

    dept_it.add_employee(emp1)
    dept_it.add_employee(emp2)
    dept_hr.add_employee(emp3)

    print(f"   {emp1}")
    print(f"   {emp2}")
    print(f"   {emp3}")

    # 3. Финансовые операции
    print("\n💸 Проводка финансовых операций...")
    system.add_transaction("Выручка за услуги", 250000, 'income', "Продажи")
    system.add_transaction("Закупка ПК", 120000, 'expense', "Закупки")
    system.add_transaction("Аренда офиса", 40000, 'expense', "Аренда")

    # 4. Выплата зарплат
    print("\n🗓️ День выплаты зарплаты...")
    for dept in system.departments:
        print(f"   {dept}")
        for emp in dept.employees:
            print(f"   → {emp.pay_salary()}")
            system.add_transaction(f"Зарплата {emp.full_name}", emp.salary, 'expense', "ФОТ")

    # 5. Итоговый отчет
    system.generate_balance_report()
    print("✅ Система бухгалтерии успешно завершила работу")