class Report:
    """Класс Отчет"""
    def __init__(self, title):
        self.title = title
        self.content = []

    def add_line(self, line):
        self.content.append(line)

    def show(self):
        print("\n" + "=" * 60)
        print(f"📊 {self.title}".center(60))
        print("=" * 60)
        for line in self.content:
            print(f"   {line}")
        print("=" * 60 + "\n")