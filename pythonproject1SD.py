import random
print("zadanie 1 podpunkt a)\n")

print ("typ działania - dodawanie, typ danych - int")
number1 = 1
number2 = 2
a =number1 + number2
print(a)
print ("typ działania - dodawanie, typ danych - float")
number1 =1
number2 = 4.5
b =number1 + number2
print(b)
print ("typ działania - dzielenie, typ danch - float")
number1 =3
number2 =2
c =(number1 / number2)
print(c)
print ("typ działania - dzielenie, typ danch - float")
number1 =4
number2 =2
d =(number1 / number2)
print(d)
print ("typ działania - dzielenie całkowite, typ danch - int")
number1 =3
number2 =2
e =(number1 // number2)
print(e)
print ("typ działania - dzielenie całkowite, typ danch - int")
number1 =(-3)
number2 =2
f =(number1 // number2)
print(f)
print ("typ działania - dzielenie modulo, typ danch - int")
number1 =11
number2 =2
g =number1 % number2
print(g)
print ("typ działania - potęgowanie, typ danch - int")
number1 =2
number2 =10
h =number1 ** number2
print(h)
print ("typ działania - potęgowanie, typ danch - int")
number1 =8
number2 =(1/3)
i =number1 ** number2
print(i)



print("zadanie 1 podpunkt b)\n")
print("int(3.0) - ta instrukcja zmienia liczbę zmiennoprzecinkową (float 3.0) na liczbę całkowitą (int), wszystkie wartości po przecinku są obcinane co daje wynik 3.")
print("float 3 - ta instrukcja zmienia liczbę całkowitą 3(int) na liczbę zmiennoprzecinkową (float), co daje wynik 3.0.")
print("float(''3'') - ta instrukcja zmienia ciąg danych znakowych (''3'') na liczbę zmiennoprzecinkową float, co daje wynik 3.0.")
print("str(12.4) - ta instrukcja zmienia liczbę zmiennoprzecinkową (float) na ciąg danych znakowych, co daje wynik (''12.4'').")
print("bool(0) - ta instrukcja umożliwia ocenę wyrażenia i uzyskanie odpowiedzi prawda lub fałsz, wynikiem tej instrukcji jest fałsz.")


print("zadanie 2\n")
uczelnia = "Studiuję  na WSIiZ"
print(uczelnia)


print("zadanie 3\n")
imię ="Jan"
wiek =20
wzrost =178
print(f"Nazywam się {imię} i mam {wiek} lat")
print(f"Mój wzrost to {178} cm")


print("zadanie 4\n")
Cena =39.99
Rabat = 0.2
cena_po_rabacie = Cena * (1 - Rabat)
print(f"cena po rabacie:{cena_po_rabacie:.2f} PLN")


print("zadanie 5\n")
bok_a = float(input("podaj długość boku a prostokąta: "))
bok_b = float(input("podaj długość boku b prostokąta: "))
pole = bok_a * bok_b
obwód =2 * (bok_a + bok_b)
print(f"Pole prostokąta wynosi: {pole:.2f}")
print(f"Obwód prostokąta wynosi: {obwód:.2f}")


print("zadanie 6\n")
dystans = random.randint(50, 500)

średnie_spalanie = float(input("Podaj średnie spalanie w litrach na 100km: "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr: "))

zużycie_paliwa = (dystans * średnie_spalanie) / 100
koszt_podróży = zużycie_paliwa * cena_paliwa

print(f"Długość przejechanej drogi: {dystans} km")
print(f"Przewidywane zużycie paliwa: {zużycie_paliwa:.2f} litrów")
print(f"Szacowane koszty podróży: {koszt_podróży:.2f} zł")


def kalkulator():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    suma = liczba1 + liczba2
    roznica = liczba1 - liczba2
    iloczyn = liczba1 * liczba2
    if liczba2 != 0:
        iloraz = liczba1 / liczba2
    else:
        iloraz = "Nie można dzielić przez zero"
    potega = liczba1 ** liczba2

    print(f"Wynik dodawania: {suma}")
    print(f"Wynik odejmowania: {roznica}")
    print(f"Wynik mnożenia: {iloczyn}")
    print(f"Wynik dzielenia: {iloraz}")
    print(f"Wynik potęgowania: {potega}")

kalkulator()













