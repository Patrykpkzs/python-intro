# Laboratorium 4 – Metody MCDM z użyciem pymcdm

## 🎯 Temat
Zastosowanie metod wielokryterialnego podejmowania decyzji (TOPSIS, SPOTIS, VIKOR) do wyboru najlepszego samochodu osobowego spośród 4 alternatyw z wykorzystaniem biblioteki `pymcdm`.

## 🚗 Alternatywy
1. Toyota Corolla  
2. Volkswagen Golf  
3. Mazda 3  
4. Hyundai i30

## 📊 Kryteria
| Kryterium                | Typ   | Jednostka       | Opis                              |
|--------------------------|-------|------------------|------------------------------------|
| Cena                    | Min   | zł               | Im taniej, tym lepiej              |
| Spalanie                | Min   | l/100 km         | Mniejsze spalanie = oszczędność    |
| Moc silnika             | Max   | KM               | Większa moc = lepsze osiągi        |
| Pojemność bagażnika     | Max   | litry            | Więcej miejsca = praktyczność      |

## 🧮 Macierz decyzyjna

| Samochód         | Cena (zł) | Spalanie | Moc (KM) | Bagażnik (l) |
|------------------|-----------|----------|----------|--------------|
| Toyota Corolla   | 109900    | 5.5      | 140      | 470          |
| Volkswagen Golf  | 117000    | 6.1      | 150      | 381          |
| Mazda 3          | 112000    | 6.0      | 122      | 358          |
| Hyundai i30      | 105000    | 5.8      | 120      | 395          |

## ⚖️ Wagi
Wagi zostały obliczone automatycznie metodą **entropii**, co oznacza, że większe znaczenie mają kryteria, które bardziej różnicują dane.

## 🧪 Zastosowane metody
- **TOPSIS** – porównanie do rozwiązania idealnego i anty-idealnego
- **SPOTIS** – minimalizacja odległości od rozwiązania referencyjnego
- **VIKOR** – kompromis między maksymalizacją korzyści i minimalizacją strat

## 📈 Wyniki

(Wyniki przykładowe — zostaną wygenerowane po uruchomieniu programu)

| Samochód         | TOPSIS | SPOTIS | VIKOR | TOPSIS Rank | SPOTIS Rank | VIKOR Rank |
|------------------|--------|--------|-------|--------------|--------------|-------------|
| Toyota Corolla   |  5.916667e-01   |  4.08(3)   |  0.408(3)  |      2.0      |      2.0       |      2.0      |
| Volkswagen Golf  |  1.045478e-08   |  1   |  1  |      4.0       |      4.0       |      4.0      |
| Mazda 3          |  4.166667e-01   |  5.8(3)   |  0.58(3)  |      3.0       |      3.0       |      3.0      |
| Hyundai i30      |  1.000000e+00   |  3.544305e-08   |  0  |      1.0       |      1.0       |      1.0      |

## 🧠 Wnioski
- Metoda TOPSIS wskazała na __________ jako najbardziej zrównoważoną opcję.
- SPOTIS zaproponował __________ jako najbliższy ideałowi.
- VIKOR zasugerował __________ jako kompromisowe rozwiązanie.

Różnice w rankingach wynikają z różnych podejść każdej metody do liczenia "odległości" od idealnych rozwiązań. Wagi obliczone metodą entropii faworyzowały np. moc silnika i cenę.

## ✅ Spełnione wymagania
- [x] Użycie biblioteki `pymcdm`
- [x] Zdefiniowana macierz decyzyjna i typy kryteriów
- [x] Zastosowanie metod TOPSIS i SPOTIS
- [x] Dodatkowo: VIKOR (dla chętnych)
- [x] Obliczenie wag metodą entropii
- [x] Normalizacja danych (min-max)
- [x] Ranking i analiza wyników