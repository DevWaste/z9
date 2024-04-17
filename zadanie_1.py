def factorial(n):
    """ Функция для вычисления факториала числа n. """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_list_from_number(n):
    """ Функция для создания списка факториалов чисел от n! до 1. """
    final_factorial = factorial(n)  # Вычисляем факториал изначального числа
    factorials = []
    for i in range(final_factorial, 0, -1):
        factorials.append(factorial(i))
    return factorials

def main():
    """ Главная функция для выполнения программы. """
    input_number = int(input("Введите натуральное число: "))  # Пример ввода: 3
    result_factorials = factorial_list_from_number(input_number)
    print(f"Список факториалов от {factorial(input_number)} до 1: {result_factorials}")

if __name__ == "__main__":
    main()
