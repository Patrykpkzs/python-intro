# Zadanie 1
# Wyszukaj w dokumentacji Pythona co najmniej trzy zagadnienia:
# • Opis funkcji wbudowanej (np. zip(), enumerate(), sorted()). | (zip() w tym wypadku)
# • Opis modułu z biblioteki standardowej (np. math, random, time). | (math w tym wypadku)
# • Opis wyjątku (np. ValueError, ZeroDivisionError).   | (ValueError w tym wypadku)
# Podaj krótkie wyjaśnienie każdego zagadnienia oraz link do dokumentacji

# Program powinien wykonywać:
# • Tworzenie dwóch list i łączenie ich funkcją zip().
# • Wykorzystanie jednej funkcji z wybranego modułu Pythona. |  (math.sqrt w tym wypadku)
# • Obsługę wyjątku try-except.
# • Komentarze w kodzie z opisem użytych funkcji i linkami do dokumentacji.

# importujemy moduł math
# Moduł math zawiera funkcje matematyczne
# Dokumentacja modułu math: https://docs.python.org/pl/3/library/math.html
import math

# Tworzymy dwie listy
lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20 , 30, 40, 50]

# Łączymy listy za pomocą funkcji zip()
# Funkcja zip() łączy elementy dwóch list w pary
# Funkcja zwraca iterator, dlatego konwertujemy go na listę
# Dokumentacja funkcji zip(): https://docs.python.org/pl/3/tutorial/datastructures.html
lista_zip = list(zip(lista1, lista2))
print("Połączone listy: ", lista_zip)

# Wykorzystanie funkcji z modułu math
# Funkcja math.sqrt() zwraca pierwiastek kwadratowy liczby
pierwiastek = math.sqrt(lista1[3])
print(f"Pierwiastek kwadratowy z {lista1[3]} to: {pierwiastek}")

# Obsługa wyjątku try-except
try:
    # próba obliczenia pierwiastka kwadratowego z liczby ujemnej
    # spowoduje zgłoszenie wyjątku ValueError
    pierwiastek = math.sqrt(-1)
except ValueError:
    # Dokumentacja wyjątków: https://docs.python.org/pl/3/tutorial/errors.html
    print("Nie można obliczyć pierwiastka z liczby ujemnej")