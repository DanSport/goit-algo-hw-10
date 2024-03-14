## Висновки

Після порівняння різних методів обчислення визначеного інтеграла для функції \( f(x) = x^2 \) на інтервалі \([0, 2]\) були отримані наступні результати:

- **Точне значення інтеграла:** 2.6666666666666665
- **Значення інтеграла методом Монте-Карло:** 2.6728
- **Значення інтеграла за допомогою quad:** 2.666666666666667

Метод Монте-Карло надав результат, який дуже близький до точного значення інтеграла. Це свідчить про ефективність методу Монте-Карло для наближеного обчислення визначених інтегралів. Також було встановлено, що значення, отримане методом quad з бібліотеки SciPy, також дуже близьке до точного значення, що підтверджує правильність реалізації методів.

У великому масштабі метод Монте-Карло може бути особливо корисним, оскільки він зазвичай вимагає менше обчислювальних ресурсів, а результати можуть бути досить точними з відповідним великим обсягом випробувань.