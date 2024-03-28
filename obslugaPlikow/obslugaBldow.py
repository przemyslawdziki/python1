#Obsluga wyjątków

#try/except

try:
    num = float(input("Wprowadź liczbę: "))
except:
    print("Wystąpił jakiś błąd.")

#specyfikacja wyjątku

try:
    num = float(input("Wprowadź jakąś liczbbę: "))
except ValueError:
    print("To nie była liczba:")

#obsługa kilku wyjątków

print()
for value in (None, "hej"):
    try:
        print("Próba konwersji: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha na liczby.")
    except ValueError:
        print("Możliwa jest tylko konwrsja łancucha cyfr.")

#wykorzystanie argmentu wyjątlu
try:
    num = float(input("Wprowadx liczbę: "))
except ValueError as e:
    print("To nie była liczba!")
    print(e)

# try/except/else
try:
    num = float(input("Wprowadź liczbę: "))
except ValueError:
    print("To nie była liczba.")
else:
    print("Wprowdziłeś liczbę", num)
