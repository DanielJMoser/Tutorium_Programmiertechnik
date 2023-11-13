'''
Schreiben Sie eine Funktion convertNumber(n, B), welche die übergebene Dezimalzahl n in das
Zahlensystem mit der Basis B konvertiert. Das Ergebnis soll in Form einer Zeichenkette zurück-
gegeben werden. Dies kann durch folgende Schritte erreicht werden:

1. Berechne n : B (n dividiert durch b) = y Rest z
2. Solange y > 0 (größer 0): Mache y zum neuen n und wiederhole Schritt 1.
3. Die Restwerte z ergeben von unten nach oben gelesen die gesuchte Zahlendarstellung.

Gehen Sie am besten folgendermaßen vor:
1. Berechnen Sie den Rest der Division.
2. Konvertieren Sie den Rest zu einem String und hängen Sie ihn an den bestehenden String aus Restwerten an.
3. Berechnen sie das neue “y” 4. Reversieren Sie den String

Zur Lösung der Aufgabe benötigen Sie folgende Informationen:
* Eine Zahl kann in Python mittels
str(zahl) in einen String umgewandelt werden.
* Strings können mithilfe des + aneinandergereiht (= konkatenieren) werden - z.B. folgt aus x = "a" + "b" das Ergebnis x == "ab"
* Strings können wie folgt reversiert (“umgedreht”) werden:
    * result = "abc" * result = result[::-1]
* Die Variable “result” enthält nun “cba”
* Man kann diese Aufgabe auch lösen, ohne den String am Ende umdrehen zu müssen.

Finden Sie diese Lösung?
'''


def convertNumber(n, B):
    if n == 0:
        return "0"
    # Leerstring
    result = ""
    # Solange n größer 0
    while n > 0:
        # Berechne den Rest
        rest = n % B
        # Neues n berechnen
        n = n // B
        # Rest an den String anhängen
        # So wird der String von unten nach oben aufgebaut
        result = str(rest) + result

    return result

print(convertNumber(42, 2))
print(convertNumber(10, 3))
print(convertNumber(10, 4))



