def input_numbers():
    numbers = []
    while True:
        a = input("Введите число (или 'end' для завершения): ")
        if a.lower() == 'end':
            break
        try:
            number = int(a)
            numbers.append(number)
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число или 'end' для завершения.")
    return numbers

def filter(numbers):
    return [num for num in numbers if num % 2 != 0]


numbers = input_numbers()
odd_numbers = filter(numbers)
print("Нечетные элементы списка:", odd_numbers)