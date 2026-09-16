### Диаграмма конечного автомата
![alt text](image.png)

```py
# выбранный вариант: (ab)ⁿ(cd)ᵐ, n ≥ 1, m ≥ 0



# Программный код:
def check_string(s):
    i = 0
    n = 0
    m = 0

    # Проверяем блоки "ab"
    while i + 1 < len(s) and s[i:i + 2] == "ab":
        n += 1
        i += 2

    # Проверяем блоки "cd"
    while i + 1 < len(s) and s[i:i + 2] == "cd":
        m += 1
        i += 2

    # Проверяем условия n >= 1
    # и полную обработку строки
    if n >= 1 and i == len(s):
        return True
    else:
        return False


while True:
    s = input("Введите строку: ")

    if s == "0":
        print("Программа завершена.")
        break

    if check_string(s):
        print("Строка принадлежит языку.")
    else:
        print("Строка не принадлежит языку.")
```
### Результат выполнения кода:

![alt text](image-1.png)