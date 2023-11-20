
def find_nth_prime(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

result = find_nth_prime(10001)
print("10001st prime: ", result)




def powersumdigits(n, power):
    sum = 0

    for digit in str(n):
        sum += int(digit) ** power
    return sum

def find_numbers(power, limit):
    resSum = 0

    for num in range(2, limit):
        if num == powersumdigits(num, power):
            resSum += num
    return resSum

print(find_numbers(5, 1000000))



def ggt(x, y):
    if x == 0:
        return y
    else:
        return ggt(y % x, x)
    

def smallest_multiple_solution():
    sm_sum = 1

    for i in range(1, 21):
        sm_sum *= i // ggt(i, sm_sum)
    return sm_sum



'''
Prime
'''

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True



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