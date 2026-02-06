from dataclasses import dataclass

# Создаем класс с декоратором @dataclass
@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float

    # Отображение информации о студенте
    def display_info(self) -> None:
        """
        Метод выводит информацию о студенте в удобном виде
        с использованием форматированной строки.

        :return: None
        """
        print(f"Имя: {self.name} | Возраст: {self.age} | Специальность: {self.major} | Средний балл: {self.gpa:.2f}")

    # Расчет оценки студента
    def calculate_grade(self) -> str:
        """
        Метод возвращает строковую оценку студента
        на основе его среднего балла.

        :return: str: Оценка студента.

        >>> test_student = Student("Dagny", 21, "Engineering", 4.7)
        >>> test_student.calculate_grade()
        'Отлично'
        """
        if self.gpa >= 4.5:
            return "Отлично"
        elif self.gpa >= 4:
            return "Хорошо"
        elif self.gpa >= 3:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

# Функция сортировки списка студентов
def sort_students(students: list[Student]) -> list[Student]:
    """
    Метод принимает список объектов Student.
    Возвращает сортированный список объектов Student по атрибуту gpa.

    :param students: list[Student]: Список объектов Student.
    :return: list[Student]: Сортированный список объектов Student по атрибуту gpa.
    """
    return sorted(students, key=lambda student: student.gpa, reverse=True)

# Основная функция программы
def main() -> None:
    """
    Основная функция программы

    :return: None
    """
    # Создание списка студентов
    students = [
        Student("Alice", 20, "Computer Science", 3.8),
        Student("Bob", 22, "Engineering", 3.2),
        Student("Charlie", 21, "Mathematics", 4.5),
        Student("David", 23, "Physics", 2.7),
        Student("Eve", 19,"Biology", 3.9)
    ]

    # Отображение информации о студентах
    for student in students:
        student.display_info()
    print()

    # Сравнение студентов
    print("Are Alice and Bob the same student?", students[0] == students[1])
    print("Are Alice and Eve the same student?", students[0] == students[4])
    print()

    # Расчет и вывод оценок
    for student in students:
        print(f"{student.name} — Grade: {student.calculate_grade()}")
    print()

    # Вывод списка студентов после сортировки
    for student in sort_students(students):
        student.display_info()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()