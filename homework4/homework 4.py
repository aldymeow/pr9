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

def count_even_odd(numbers):
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    even_count = len(numbers) - odd_count 
    return even_count, odd_count

numbers = input_numbers()
even_count, odd_count = count_even_odd(numbers)
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)