def search_array(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return None

'''
def selection_sort(array, asc=True):

    n = len(array)

    for i in range(n):
        # Finde Min/Max im restlichen Array
        index = i
        for j in range(i + 1, n):
            if (asc and array[j] < array[index]) or (not asc and array[j] > array[index]):
                index = j

        # Tauschen
        array[i], array[index] = array[index], array[i]

    return array

'''



def selection_sort(array, asc):
    # DEINE ANTWORT HIER
    s = []
    u = array
    
    while len(u)>0:
        if asc:
            s.append(u.pop(u.index(min(u))))
        else:
            s.append(u.pop(u.index(max(u))))
                
    return s


# isinstance bool? #
def sum_array(array):

    summe = 0
    i = 0

    while i < len(array):
        if type(array[i]) == int:
            summe += array[i]
        i += 1

    return summe


def push(stack, element):
    stack.append(element)

'''
def pop(stack):
    if not stack:
        return None
    return stack.pop()
'''

def size(stack):
    return len(stack)
    

def pop(stack):
    # DEINE ANTWORT HIER
    if size(stack)==0:
        return None
    else:
        var = stack[-1]
        del stack[-1]
        return var



def top(stack):
    if not stack:
        return None
    return stack[-1]


def size(stack):
    return len(stack)






def get_digits(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n = n // 10

    return digits


def digit_power_sum(digits, power):
    return sum(digits) ** power


def is_interesting_number(n):

    digits = get_digits(n)
    digit_sum = sum(digits)

    if digit_sum == 1:
        return False
    
    for power in range(1, 20):
        if digit_power_sum(digits, power) == n:
            return True
        
        if digit_power_sum(digits, power) > n:
            break
    
    return False



def get_interesting_numbers(l, u):

    interesting_numbers = []

    for n in range(l, u + 1):
        if is_interesting_number(n):
            interesting_numbers.append(n)
    return interesting_numbers



'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
'''


def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result



def get_digits(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n = n // 10

    return digits


def digits_factorial_sum(n):
    digits = get_digits(n)

    return sum(factorial(digit) for digit in digits)


def sum_of_special_numbers(n):
    special_sum = 0

    for number in range(10, n):
        if number == digits_factorial_sum(number):
            special_sum += number
    return special_sum




def main():
# print tests for all the above functions

    print("search_array([1, 2, 3, 4, 5], 3) ==", search_array([1, 2, 3, 4, 5], 3))
    print("search_array([1, 2, 3, 4, 5], 6) ==", search_array([1, 2, 3, 4, 5], 6))
    print("search_array([1, 2, 3, 4, 5], 5) ==", search_array([1, 2, 3, 4, 5], 5))
    print("search_array([1, 2, 3, 4, 5], 1) ==", search_array([1, 2, 3, 4, 5], 1))

    print("selection_sort([1, 2, 3, 4, 5], True) ==", selection_sort([1, 2, 3, 4, 5], True))
    print("selection_sort([1, 2, 3, 4, 5], False) ==", selection_sort([1, 2, 3, 4, 5], False))
    print("selection_sort([5, 4, 3, 2, 1], True) ==", selection_sort([5, 4, 3, 2, 1], True))

    print("sum_array([1, 2, 3, 4, 5]) ==", sum_array([1, 2, 3, 4, 5]))
    print("sum_array([1, 2, 3, 4, 5, 'a']) ==", sum_array([1, 2, 3, 4, 5, 'a']))
    print("sum_array([1, 2, 3, 4, 5, 'a', 'b']) ==", sum_array([1, 2, 3, 4, 5, 'a', 'b']))

    stack = []
    push(stack, 1)
    push(stack, 2)
    push(stack, 3)

    print("stack ==", stack)
    print("pop(stack) ==", pop(stack))
    print("stack ==", stack)
    print("pop(stack) ==", pop(stack))