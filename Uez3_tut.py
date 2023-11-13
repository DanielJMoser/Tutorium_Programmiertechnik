## TUTORIUM PROGRAMMIERTECHNIK (DIE ERSTE)##

## Oans ##

# Implementieren Sie eine Funktion, welche für jede beliebige Integer-Zahl bestimmen kann, ob diese ungerade ist. 
# Falls eine Zahl ungerade ist, soll der Wahrheitswert "True" zurückgegeben werden.
# Falls es sich um eine gerade Zahl handelt, dann "False".

def is_odd(x):
    result = None
    # Gibt's an Rest bei x mod 2, so hamma a ungerade Zahl vorliegend.
    if ( x % 2 != 0):
        result = True
    else:
        result = False
    
    return result

print(is_odd(3))    #T
print(is_odd(4))    #F



## Zwoa ##

# Implementieren Sie eine Funktion, welche bei der Zahl 3 startet und jede fünfte Zahl, 
# die noch kleiner als die übergeben Zahl x ist, zu der bisherigen Summe (d.h. 3 + 8 + 13 + 18 + ...) hinzuaddiert. 
# Am Ende soll die Summe dieser Berechnung zurückgegeben werden.

def my_sum(x):
    sum = 0
    current_number = 3

    while current_number < x:
        sum += current_number
        current_number += 5

    return sum

print(my_sum(10))   #11
print(my_sum(20))   #42


## Drei ##

# Implementieren Sie eine Funktion, welche das Maximum und das Minimum von 6 Integer-Zahlen ermittelt und zurückgibt. 
# Verwenden Sie dafür möglichst wenige Vergleiche zwischen den einzelnen Zahlen.
# Die von Python bereitgestellten Funktionen min() und max() dürfen nicht verwendet werden.

def get_min_max(a, b, c, d, e, f):
    _max_ = a
    _min_ = a

    # Überprüfe und aktualisiere "_max_" und "_min_" für jede der sechs gegebenen Zahlen.
    # Für jede Zahl wird geprüft, ob sie größer oder kleiner ist als das aktuelle "_max_" bzw. "_min_".
    # Falls ja, wird "_max_" bzw. "_min_" aktualisiert.

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

    return _min_, _max_

print(get_min_max(5, 2, 9, 1, 7, 4))

## Vier ##

# Implementieren Sie eine Funktion, welche für eine beliebige positive Integer-Zahl ermittelt, 
# wie oft diese ohne Entstehung eines Restbetrages durch 2 geteilt werden kann (nur gerade Zahlen können ohne Restbetrag geteilt werden)
# und das Ergebnis anschließend zurückgibt. 
# Verwenden Sie dazu die in Aufgabe 3.1 implementierte Funktion "is_odd".

def count_loop(x):
    count = 0

    # mia nutzen obige Funktion
    while not is_odd(x):
        # Falls x gerade is, teilen mas durch zwoa...
        x = x // 2
        # ...und erhöhen den count um Eins.
        count += 1

    return count

print(count_loop(32))
print(count_loop(15)) 


## Fünf ##

# Implementieren Sie eine Funktion, welche die Division mit Rest für den Dividenten x und den Divisor y berechnet und zurückgibt.
# Der Divisions-Operator / bzw. // und der Modulo-Operator % dürfen nicht verwendet werden.

def division_mit_rest(x, y):
    result = 0
    remainder = x

    # Gültig, solange der remainder größer als oder gleich y is
    while remainder >= y:
        # Im Falle subtrahiern ma y vom Rest
        remainder -= y
        # Dann inkrementiern ma die Ergebnisvariable um 1
        result += 1

    return result, remainder

print(division_mit_rest(20, 7))
print(division_mit_rest(15, 5))


## Sechs ##

# Implementieren Sie eine Funktion, welche für die übergebene Zahl x bestimmt, ob diese Zahl eine Primzahl ist. 
# Wenn es sich um eine Primzahl handelt, dann soll True zurückgegeben werden, ansonsten False.
# Mathematisch gesehen ist eine Primzahl eine natürliche Zahl, die größer als 1 und ausschließlich durch sich selbst und durch 1 teilbar ist.
# Zur Überprüfung Ihrer Lösung finden Sie z.B. auf Wikipedia eine Liste von Primzahlen zum Testen.

# ----Primzahlen bis 100---- #
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 #

def is_prime(x):
    # Mia wissen, dass 0 und 1 koane Primes sein.
    if x == 0 or x == 1:
        return False
    # 2 dagegen schon, also retourniern ma True
    elif x == 2:
        return True
    # Dann iteriern ma über alle Werte von i zwischen 2 und x-1
    # (x is ja in dem Fall, als zweiter Wert, exklusiv, beim range-Operator. 
    # Würden mas inkludiern wollen, so müssts 'x+1' statt 'x' heißen.
    for i in range(2, x):
        # is x durch i ohne Rest teilbar?
        if x % i == 0:
            # weil in dem Fall hamma koa Primzahl vorliegend.
            return False
    # andernfalls hamma dagegen eine und geben 'True' zurück.
    return True

print(is_prime(17)) #T
print(is_prime(4))  #F

## Sechs - Alternative 1 ##

'''
Dabei benutzen ma a recht cooles Konzept namens "6*k +/- 1 Regel"
I hab des so auf meinem Übungszettel von damals stehn, aber heut hab i solches Mathematura-Wissen verdrängt.
Drum hier a Zusammenfassung von ChatGPT:

Die "6k +/- 1 Regel" ist eine einfache Regel zur schnellen Identifizierung von Primzahlen.
Sie besagt, dass fast alle Primzahlen (außer 2 und 3) in der Form 6k +/- 1 sind, 
wobei k eine nicht-negative ganze Zahl ist. 
Das bedeutet, dass Primzahlen entweder um 1 kleiner oder um 1 größer als ein Vielfaches von 6 sind. 
Diese Regel ermöglicht es, viele nicht-primäre Kandidaten effizient zu eliminieren und 
erleichtert die Identifizierung von Primzahlen.
'''

def is_prime_alt(x):
    # is x weniger oder gleich 1? Weil dann gwiß koa Prime
    if x <= 1:
        return False
    # wenn x 2 oder 3 is, dann hamma a Primzahl. Vielleicht is des a bissl Schwindeln, aber naja...
    elif x <= 3:
        return True
    # is x teilbar durch 2 oder 3? Weil koa Primzahl, im Falle
    elif x % 2 == 0 or x % 3 == 0:
        return False
    
    # 4 is koa Prime, des skippen ma und schauen uns die Divisoren ab 5 an.
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime_alt(17)) #T
print(is_prime_alt(4))  #F



## Sieben ##

# Implementieren Sie eine Funktion, welche für die übergebene Zahl x bestimmt, ob diese Zahl eine Dreieckszahl ist. 
# Wenn es sich um eine Dreieckszahl handelt, dann soll True zurückgegeben werden, ansonsten False.
# Eine Dreieckszahl ist eine Zahl, die der Summe aller Zahlen von 1 bis zu einer Obergrenze n entspricht. 
# Die 10 ist beispielsweise eine Dreieckszahl, da 1+2+3+4=10
# Die 28 ist auch eine Dreieckszahl, da 1+2+3+4+5+6+7=28.

'''
Verehrte Damen und Herren, meine Faulheit kennt keine Grenzen.
Weil i eh schon von obiger Aufgabe ChatGPT offen hab, hab i ma gedacht, i lass den Laggl glei meinen Code
der letzten Aufgab im tiroler Dialekt auskommentieren.
Es Ergebnis is zu genial ums euch vorzuenthalten.
Übersetzungshilfe: 

if "Zoidl" == "Zahl":
    return True
else:
    return False


...würd vermutlich True retourniern.
'''


def is_triangular(x):
    # I binsch der Anfangswert von n und dem dreieckigen Zoidl.
    n = 1
    triangular = 0

    # Solange des dreieckige Zoidl kleiner odo glei isch wia x, mach folgendes:
    while triangular < x:
        # Berechne des dreieckige Zoidl mittels der Forml: Dreieckszoidl = n * (n + 1) // 2
        triangular = n * (n + 1) // 2
        # Wenn des dreieckige Zoidl genau gleich x isch, dann isches a dreieckigs Zoidl.
        if triangular == x:
            return True
        # Ansonsten geh weiter und probiere mit'm nächsten Wert für n.
        n += 1

    # Wenn ma bis do kummen isch und kane Treffer g'hobt hobn, dann isches koa dreieckigs Zoidl.
    return False

print(is_triangular(10))    #T
print(is_triangular(27))    #F