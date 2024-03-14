import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()  

# Визначення функції, яку ми інтегруємо
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0
b = 2
n = 1000000  # Кількість випадкових точок

# Генерування випадкових координат x та y всередині прямокутника
x_values = np.random.uniform(a, b, n)
y_values = np.random.uniform(0, f(b), n)

# Обчислення кількості точок, що потрапили під криву
points_under_curve = sum(y_values <= f(x_values))

# Обчислення площі прямокутника та площі під кривою
rectangle_area = (b - a) * f(b)
area_under_curve = rectangle_area * (points_under_curve / n)

# перевірка за допомогою quad

# Визначення функції
def f(x):
    return x ** 2

# Обчислення точного значення інтеграла
exact_value = 8/3

# Обчислення значення інтеграла за допомогою quad
integral_value, _ = quad(f, 0, 2)

print("Точне значення інтеграла:", exact_value)
print("Значення інтеграла методом Монте-Карло:", area_under_curve)
print("Значення інтеграла за допомогою quad:", integral_value)
