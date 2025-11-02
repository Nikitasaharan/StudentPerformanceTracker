class Student:
    def __init__(self, sid, name, grade, course):
        self.sid = sid
        self.name = name
        self.grade = grade
        self.course = course

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insertStudent(self, student):
        index = self.hash_function(student.sid)
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Linear probing
        self.table[index] = student

    def display(self):
        for i, s in enumerate(self.table):
            if s:
                print(f"ID: {s.sid}, Name: {s.name}, Grade: {s.grade}, Course: {s.course}")

def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j].grade > students[j+1].grade:
                students[j], students[j+1] = students[j+1], students[j]
    return students

def sequential_search(students, name):
    for s in students:
        if s.name.lower() == name.lower():
            return s
    return None

# Sample Data
students = [
    Student(101, "Nikita", 89, "Data Structures"),
    Student(102, "Kartikeya", 78, "Java Programming"),
    Student(103, "Riya", 92, "Machine Learning")
]

# Hash Table
ht = HashTable(10)
for s in students:
    ht.insertStudent(s)

print("Student Records in Hash Table:")
ht.display()

print("\nSorted by Grades (Bubble Sort):")
sorted_students = bubble_sort(students)
for s in sorted_students:
    print(f"{s.name} - {s.grade}")

name = "Kartikeya"
found = sequential_search(students, name)
if found:
    print(f"\nSearch Result: {found.name} scored {found.grade}")
else:
    print("\nStudent not found")
