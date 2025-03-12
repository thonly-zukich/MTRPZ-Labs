# Імпортуємо необхідні бібліотеки
import math  # Містить математичні функції, зокрема sqrt() для обчислення кореня дискримінанта
import sys   # Використовується для обробки аргументів командного рядка

# Функція для розв’язку квадратного рівняння
def solve_funny_math(alpha, beta, gamma):
    """
    Розв'язує квадратне рівняння αx² + βx + γ = 0

    Параметри:
    alpha (float): Коефіцієнт при x² (не може бути нулем)
    beta (float): Коефіцієнт при x
    gamma (float): Вільний член

    Повертає:
    tuple: Пара коренів (або один корінь, або порожній кортеж)
    """

    if alpha == 0:
        raise ValueError("Oops! Alpha (a) cannot be zero.")  # Перевіряємо, щоб alpha ≠ 0

    # Обчислюємо дискримінант
    discriminant = beta ** 2 - 4 * alpha * gamma  # Формула дискримінанта: D = b² - 4ac

    # Визначаємо кількість коренів
    if discriminant > 0:
        # Два дійсних корені
        root1 = (-beta + math.sqrt(discriminant)) / (2 * alpha)
        root2 = (-beta - math.sqrt(discriminant)) / (2 * alpha)
        return (root1, root2)
    elif discriminant == 0:
        # Один корінь (кратний)
        single_root = -beta / (2 * alpha)
        return (single_root,)
    else:
        # Немає дійсних коренів
        return ()

# Функція для запуску в інтерактивному режимі (користувач вводить значення вручну)
def fun_interactive_mode():
    """
    Інтерактивний режим: користувач вводить коефіцієнти рівняння
    """

    print("🎉 Super Fun Quadratic Equation Solver 🎉")
    print("Equation format: αx^2 + βx + γ = 0")

    while True:
        try:
            # Запитуємо у користувача коефіцієнти
            alpha = float(input("Enter α (a) = "))  # Введення коефіцієнта alpha
            if alpha == 0:
                print("🚨 Oops! Alpha cannot be zero, try again!")  # Забороняємо нульове значення
                continue

            beta = float(input("Enter β (b) = "))  # Введення коефіцієнта beta
            gamma = float(input("Enter γ (c) = "))  # Введення коефіцієнта gamma

            # Викликаємо функцію розв’язку
            roots = solve_funny_math(alpha, beta, gamma)

            # Виводимо рівняння у зрозумілому форматі
            print(f"Equation is: ({alpha}) x^2 + ({beta}) x + ({gamma}) = 0")

            # Виводимо результати
            if len(roots) == 2:
                print("🎉 There are 2 fantastic roots!")
                print(f"✨ Root 1: {roots[0]:.6g}")
                print(f"✨ Root 2: {roots[1]:.6g}")
            elif len(roots) == 1:
                print("⭐ Just 1 unique root!")
                print(f"🦄 Root: {roots[0]:.6g}")
            else:
                print("💨 No real roots this time, sorry!")

            break  # Виходимо після успішного розрахунку
        except ValueError:
            print("🚨 Whoops! That's not a valid number. Try again!")  # Обробка помилки введення

# Функція для роботи в неінтерактивному режимі (читання коефіцієнтів із файлу)
def file_mode(filename):
    """
    Читає коефіцієнти рівняння з файлу та розв'язує його

    Параметри:
    filename (str): Назва файлу, що містить три числа (α β γ)
    """

    try:
        # Відкриваємо файл для читання
        with open(filename, "r") as f:
            line = f.readline().strip()  # Читаємо перший рядок, видаляємо зайві пробіли
            parts = line.split()  # Розбиваємо рядок на три частини (α, β, γ)
            
            if len(parts) != 3:
                raise ValueError("Invalid file format")  # Перевіряємо коректність формату
            
            # Перетворюємо значення в числа
            alpha, beta, gamma = map(float, parts)

            # Викликаємо функцію розв’язку
            roots = solve_funny_math(alpha, beta, gamma)

            # Виводимо рівняння
            print(f"Equation is: ({alpha}) x^2 + ({beta}) x + ({gamma}) = 0")

            # Виводимо результати
            if len(roots) == 2:
                print("🎉 There are 2 fantastic roots!")
                print(f"✨ Root 1: {roots[0]:.6g}")
                print(f"✨ Root 2: {roots[1]:.6g}")
            elif len(roots) == 1:
                print("⭐ Just 1 unique root!")
                print(f"🦄 Root: {roots[0]:.6g}")
            else:
                print("💨 No real roots this time, sorry!")

    except FileNotFoundError:
        print(f"🚨 Error: File '{filename}' not found.")  # Якщо файл не знайдено
    except ValueError as e:
        print(f"🚨 Error: {e}")  # Якщо виникла помилка форматування

# Точка входу в програму
if __name__ == "__main__":
    """
    Визначає, як запускати програму: у інтерактивному або файловому режимі
    """

    # Якщо передано один аргумент (назва файлу), запускаємо файловий режим
    if len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        # Інакше запускаємо інтерактивний режим
        fun_interactive_mode()
