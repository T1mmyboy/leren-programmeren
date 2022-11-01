employees = {}

for i in range(3):
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")

    employees[name] = salary


# 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
print(employees)