'''
Euler 7
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Find the 10001st prime number
result = find_nth_prime(10001)
print("The 10001st prime number is:", result)



'''
Euler 30
'''

def sum_of_powers_of_digits(n, power):
    total = 0
    for digit in str(n):
        total += int(digit) ** power
    return total

def find_numbers(power, limit):
    result_sum = 0
    for num in range(2, limit):  
        if num == sum_of_powers_of_digits(num, power):
            result_sum += num
    return result_sum

power = 5
limit = 1000000  

print(find_numbers(power, limit))


'''
Euler 5
'''

def ggt(x, y):
    if x == 0:
        return y
    else:
        return ggt(y % x, x)


def smallest_multiple_solution():
    sm_sum = 1
    for i in range(1, 21):
        sm_sum *= i // ggt(i, sm_sum) # Zuerst wird die Floor Division ausgeführt, dann wird auf sm_sum multipliziert
    return sm_sum


smallest_multiple_solution()


'''

KLAUSUR 2021


Prothsche Primzahlen sind Zahlen die sowohl Proth-Zahlen als auch Primzahlen sind.

Proth-Zahlen sind natürliche Zahlen der Form 𝑘⋅2𝑛+1
, wobei k und n positive Ganzzahlen sind und k sowohl ungerade als auch kleiner als 2𝑛

ist. Beispiele für Proth-Zahlen sind 3, 5, 9, 13, 17, 25, 33, 41, 49, 57, 65, 81, ...

Primzahlen sind natürliche Zahlen, die größer als 1 und ausschließlich durch sich selber oder durch 1 teilbar sind. Beispiele für Primzahlen sind 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, ...

Beispiele für Primzahlen, die auch Proth-Zahlen sind: 3, 5, 13, 17, 41, ...

Implementieren Sie in Python eine Funktion P(n, m), die alle Prothschen Primzahlen im Bereich von 𝑛
bis 𝑚

(beide Grenzen sind inklusive) findet und die Summe der gefundenen Zahlen zurückgibt.

Hinweis: Achten Sie beim Finden von Proth-Zahlen darauf, dass n nicht zu groß wird, da ansonsten sehr große Zahlen herauskommen können.
'''

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1): # +1 weil sonst die letzte Zahl nicht geprüft wird
            if n % i == 0:
                return False
        return True
    
def is_proth(n):
    for k in range(1, n):
        if n % (2 ** k) == 1:
            if is_prime((n - 1) // (2 ** k)):
                return True
    return False

def P(n, m):
    sum = 0
    for i in range(n, m + 1):
        if is_proth(i):
            sum += i
    return sum

print("Die Summe der Prothschen Primzahlen im Bereich von 1 bis 1000 ist:", P(1, 1000))




'''

KLAUSUR 2022

Mirpzahlen sind Primzahlen, die rückwärts gelesen eine andere Primzahl ergeben (mirp ist prim rückwärts geschrieben).

Ein Primzahlpalindrom wie z.B. 131 ist daher keine Mirpzahl, da sich rückwärts gelesen zwar ebenfalls eine Primzahl ergibt, aber keine andere, sondern dieselbe.

Primzahlen sind natürliche Zahlen, die größer als 1 und ausschließlich durch sich selber oder durch 1 teilbar sind. 
Beispiele für Primzahlen sind 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, ...

Die Eigenschaft Mirpzahl hängt vom verwendeten Zahlensystem ab, wir gehen daher vom Dezimalsystem aus.
Beispiele für Mirpzahlen im Dezimalsystem sind 13, 17, 31, 37, 71, 73, ...

Implementieren Sie in Python eine Funktion M(n, m), die alle Mirpzahlen im Bereich von n bis m
(beide Grenzen sind inklusive) findet, bei denen genau zweimal ein Einser als Ziffer vorkommt, und die Summe der gefundenen Zahlen zurückgibt.

Beispiel M(100, 1100) = 113 + 311 + 1021 + 1031 + 1061 + 1091 = 4628
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def reverse_number(num):
    return int(str(num)[::-1])

def count_ones(num):
    return str(num).count('1')

def is_mirp(num):
    if num < 10 or str(num)[-1] == '1':
        return False
    reversed_num = reverse_number(num)
    return num != reversed_num and is_prime(reversed_num)

def M(n, m):
    mirp_sum = 0
    for i in range(n, m + 1):
        if count_ones(i) == 2 and is_prime(i) and is_mirp(i):
            mirp_sum += i
    return mirp_sum

# Test
result = M(100, 1100)
print("Result:", result)

