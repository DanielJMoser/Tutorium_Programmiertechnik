# Nummer 1 #
def search_array(array, x):
    """
    Sucht nach dem ersten Vorkommen des Wertes x im Array und gibt dessen Index zurück.
    Gibt None zurück, falls x nicht im Array gefunden wird.
    """
    for i in range(len(array)):
        if array[i] == x:
            return i  # Gibt den Index zurück, wenn das Element gefunden wird
    return None  # Gibt None zurück, wenn das Element nicht gefunden wird





# Nummer 2 #
def selection_sort(array, asc=True):
    """
    Sortiert das Array mit dem Selectionsort-Algorithmus.
    Sortiert aufsteigend, wenn asc=True, und absteigend, wenn asc=False.
    """
    n = len(array)
    for i in range(n):
        # Finde das Minimum/Maximum im restlichen Array
        index = i
        for j in range(i+1, n):
            if (asc and array[j] < array[index]) or (not asc and array[j] > array[index]):
                index = j

        # Tausche das gefundene Minimum/Maximum mit dem aktuellen Element
        array[i], array[index] = array[index], array[i]

    return array




# Nummer 3 #
def sum_array(array):
    """
    Summiert alle Integer-Werte im Array und gibt die Summe zurück.
    Gibt 0 zurück, wenn kein Integer gefunden wird.
    """
    summe = 0
    i = 0
    while i < len(array):
        if isinstance(array[i], int):
            summe += array[i]
        i += 1
    return summe





# Nummer 4 #
def push(stack, element):
    """
    Fügt ein Element am Ende des Stacks hinzu.
    """
    stack.append(element)

def pop(stack):
    """
    Entfernt und gibt das oberste Element des Stacks zurück.
    Gibt None zurück, wenn der Stack leer ist.
    """
    if not stack:
        return None
    return stack.pop()

def top(stack):
    """
    Gibt das oberste Element des Stacks zurück, ohne es zu entfernen.
    Gibt None zurück, wenn der Stack leer ist.
    """
    if not stack:
        return None
    return stack[-1]

def is_empty(stack):
    """
    Überprüft, ob der Stack leer ist.
    """
    return len(stack) == 0

def size(stack):
    """
    Gibt die Größe des Stacks zurück.
    """
    return len(stack)





# Nummer 5 #
def get_digits(n):
    """
    Zerlegt eine Zahl in ihre einzelnen Ziffern und gibt diese als Liste zurück.
    """
    digits = []
    while n > 0:
        digits.append(n % 10)  # Extrahiert die letzte Ziffer
        n = n // 10  # Entfernt die letzte Ziffer
    return digits

def digit_power_sum(digits, power):
    """
    Berechnet die Summe der Ziffern in der Liste und potenziert das Ergebnis mit 'power'.
    """
    return sum(digits) ** power

def is_interesting_number(n):
    """
    Überprüft, ob eine Zahl 'interessant' ist, d.h. ob sie gleich der Ziffernsumme potenziert mit einer natürlichen Zahl ist.
    """
    digits = get_digits(n)
    digit_sum = sum(digits)
    if digit_sum == 1:
        return False  # Ignoriere Zahlen mit einer Ziffernsumme von 1

    for power in range(1, 21):  # Begrenze die Überprüfung auf realistische Exponenten
        if digit_power_sum(digits, power) == n:
            return True
        if digit_power_sum(digits, power) > n:
            break  # Kein weiterer Test notwendig, wenn die Potenzsumme größer als n ist

    return False

def get_interesting_numbers(l, u):
    """
    Gibt eine Liste aller 'interessanten' Zahlen im Bereich von l bis u zurück.
    """
    interesting_numbers = []
    for n in range(l, u + 1):
        if is_interesting_number(n):
            interesting_numbers.append(n)
    return interesting_numbers





# #
def factorial(num):
    """Berechnet die Fakultät einer Zahl."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def get_digits(n):
    """Zerlegt eine Zahl in ihre Ziffern."""
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits

    # Alternative:
    # return [int(digit) for digit in str(n)]


def digits_factorial_sum(n):
    """Berechnet die Summe der Fakultäten der Ziffern einer Zahl."""
    digits = get_digits(n)
    return sum(factorial(digit) for digit in digits)
    # Alternative:
    # return sum(factorial(digit) for digit in get_digits(n))


def sum_of_special_numbers(n):
    """Findet die Summe aller Zahlen bis n, deren Ziffernfakultätensumme die Zahl selbst ergibt."""
    special_sum = 0
    for number in range(10, n):  # Startet bei 10, da Zahlen unter 10 nicht betrachtet werden
        if number == digits_factorial_sum(number):
            special_sum += number
    return special_sum







# Main #
def main():
    # Test für die Funktion search_array
    test_array = [3, 6, 8, 10, 15]
    search_number = 10
    print(f"Suche nach {search_number} in {test_array}: Index =", search_array(test_array, search_number))

    # Test für die Funktion selection_sort
    unsorted_array = [34, 7, 23, 32, 5, 62]
    print("Unsortiertes Array:", unsorted_array)
    print("Aufsteigend sortiert:", selection_sort(unsorted_array.copy(), True))
    print("Absteigend sortiert:", selection_sort(unsorted_array.copy(), False))

    # Test für die Funktion sum_array
    mixed_array = [1, 'Python', 3, 'AI', 5, 7]
    print("Summe der Integer in", mixed_array, ":", sum_array(mixed_array))

    # Test für den Stack
    stack = []
    print("Füge Elemente zum Stack hinzu")
    push(stack, 'Python')
    push(stack, 2023)
    push(stack, [1, 2, 3])
    print("Aktueller Stack:", stack)
    print("Oberstes Element:", top(stack))
    print("Entferne oberstes Element:", pop(stack))
    print("Stack nach dem Entfernen:", stack)
    print("Ist der Stack leer?", is_empty(stack))
    print("Größe des Stacks:", size(stack))

    # Test für interessante Zahlen
    print("Interessante Zahlen zwischen 400 und 600:", get_interesting_numbers(400, 600))

    # Test für Fakultäten
    n = 50000  # Obergrenze
    print("Summe der speziellen Zahlen bis", n, ":", sum_of_special_numbers(n))

if __name__ == "__main__":
    main()
