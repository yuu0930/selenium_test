def print_string(text):
    print(text)
    
print_string("Hello,Python!")

def add(a, b):
    x = a + b
    print(x)
    
add(10, 20)


def sum_and_avg(numbers): 
    sum_numbers = sum(numbers)
    len_numbers = len(numbers)
    avg_numbers = sum_numbers / len_numbers
    return sum_numbers, avg_numbers

numbers = [14, 32, 80, 1, 9]
result = sum_and_avg(numbers)
print(result)


numbers = [14, 32, 80, 1, 9]

def is_even(number):
    return number % 2 == 0

for num in numbers:
    if is_even(num):
        print(f"{num}は偶数です")
    else:
        print(f"{num}は奇数です")
        

