from pulp import LpMaximize, LpProblem, LpVariable

# Створення об'єкту проблеми для максимізації
model = LpProblem(name="Production_Optimization", sense=LpMaximize)

# Оголошення змінних рішення
lemonade = LpVariable(name="Lemonade_units", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_juice_units", lowBound=0, cat="Integer")

# Додавання обмежень на ресурси
model += 2 * lemonade + fruit_juice <= 100  # Вода
model += lemonade <= 50  # Цукор
model += lemonade <= 30  # Лимонний сік
model += 2 * fruit_juice <= 40  # Фруктове пюре

# Додавання функції максимізації
model += lemonade + fruit_juice

# Вирішення проблеми
model.solve()

# Виведення результатів
print(f"Кількість одиниць Лимонаду: {lemonade.varValue}")
print(f"Кількість одиниць Фруктового соку: {fruit_juice.varValue}")
