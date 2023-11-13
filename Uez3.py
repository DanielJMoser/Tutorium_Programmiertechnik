'''
Schreiben Sie eine Funktion, die für jede gegebene ganze Zahl feststellen kann, 
ob sie gerade ist. Wenn die Zahl gerade ist, sollte die Funktion "True" zurückgeben, andernfalls "False".
'''

def is_even(x):
    result = None
    # DEINE ANTWORT HIER
    if x % 2 == 0:
        result = True
    else:
        result = False
    return result

print(is_even(3))    #F



'''
Implementieren Sie eine Funktion, die bei der Zahl 4 startet und jede vierte Zahl, 
die noch kleiner als die übergebene Zahl y ist, zur bisherigen Summe (d.h. 4 + 8 + 12 + 16 + ...) hinzufügt. 
Am Ende soll die Summe dieser Berechnung zurückgegeben werden.
'''

def my_sum(y):
    sum = 0
    current_number = 4

    while current_number < y:
        sum += current_number
        current_number += 4

    return sum

print(my_sum(10))   # 16
print(my_sum(20))   # 40



'''
Implementieren Sie eine Funktion, die das Maximum und das Minimum von 7 Integer-Zahlen ermittelt und zurückgibt. 
Verwenden Sie dafür möglichst wenige Vergleiche zwischen den einzelnen Zahlen. 
Die von Python bereitgestellten Funktionen min() und max() dürfen nicht verwendet werden.
'''

def get_min_max(a, b, c, d, e, f, g):
    # Annahme, dass 'a' das vorläufige Maximum und Minimum ist.
    _max_ = a
    _min_ = a

    # Durchlauf der restlichen Zahlen und Aktualisierung von _max_ und _min_.
    if b > _max_:
        _max_ = b
    elif b < _min_:
        _min_ = b

    if c > _max_:
        _max_ = c
    elif c < _min_:
        _min_ = c

    if d > _max_:
        _max_ = d
    elif d < _min_:
        _min_ = d

    if e > _max_:
        _max_ = e
    elif e < _min_:
        _min_ = e

    if f > _max_:
        _max_ = f
    elif f < _min_:
        _min_ = f

    if g > _max_:
        _max_ = g
    elif g < _min_:
        _min_ = g

    return _min_, _max_

# Beispielaufruf
print(get_min_max(5, 2, 9, 1, 7, 4, 8))



'''
Schreibe eine Funktion namens count_loop_v2(x, divisor), die die Anzahl der Schleifendurchläufe zählt, 
die benötigt werden, um die Zahl x so lange durch divisor zu teilen, bis das Ergebnis ungerade ist. 
Die Funktion sollte dann die Anzahl der Schleifendurchläufe zurückgeben.
'''

def count_loop_v2(x, divisor):
    count = 0

    while x % divisor == 0 and x > 0:
        x = x // divisor
        count += 1

    return count

# Beispiele
print(count_loop_v2(32, 4))  # Ausgabe: 5, da 32/4 = 8, 8/4 = 2, 2/4 = 0, 0/4 = 0, 0/4 = 0 (erst nach 5 Schritten ungerade)
print(count_loop_v2(15, 3))  # Ausgabe: 1, da 15/3 = 5 (schon nach 1 Schritt ungerade)


'''
Implementieren Sie eine Funktion, die die Division mit Rest für den Dividend x und den Divisor y berechnet und das Ergebnis sowie den verbleibenden Rest zurückgibt. 
Die Division soll ohne die Verwendung der Division- und Modulo-Operatoren (/ bzw. %) erfolgen. 
Verwenden Sie stattdessen die von x und y abgezogene Vielfache von y, um den Rest zu berechnen.
'''

def division_mit_rest(x, y):
    result = 0
    remainder = x

    # Gültig, solange der remainder größer oder gleich y ist
    while remainder >= y:
        # Subtrahiere Vielfache von y vom Rest
        temp_y = y
        multiple = 1
        while remainder >= (temp_y << 1):  # Verwende Bitshift für die Multiplikation mit 2
            temp_y <<= 1
            multiple <<= 1
        remainder -= temp_y
        result += multiple

    return result, remainder

print(division_mit_rest(20, 7))
print(division_mit_rest(15, 5))



