#dane
wzrost = float(input("Podaj swój wzrost: "))
waga = int(input("Podaj swoją wagę: "))

#liczenie
liczenie_bmi = waga / (wzrost * wzrost)
zaokraglone_bmi = round(liczenie_bmi, 1)

#wynik
print(f"Oto twoje BMI: {zaokraglone_bmi}")

#ify
if zaokraglone_bmi < 18.5:
    print (f"Oto twoje BMI: {zaokraglone_bmi}, masz niedowagę")

if zaokraglone_bmi < 25:
    print (f"Oto twoje BMI: {zaokraglone_bmi}, masz dobrą wagę")

if zaokraglone_bmi > 25:
    print (f"Oto twoje BMI: {zaokraglone_bmi}, masz nadwagę")