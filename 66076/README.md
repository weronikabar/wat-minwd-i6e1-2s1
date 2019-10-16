# wat-minwd-i6e1-2s1

## Piotr Filochowski, grupa I6E2S1


## Treść zadania:
Zadanie 5
Zadanie 5. Dziecko w pewnym wieku potrzebuje określonych ilości witamin. Ilość witamin dostarczanych przez pewne produkty przedstawiono poniżej.

| Produkty	| Ilość witamin w jednostce	| Koszt jednostkowy [zł]
|	          | A	  | B	  | C	  | E       | 	
| P1	      | 6	  | 1	  | 9	  | 6	      | 1,2
| P2	      | 3	  | 3	  | 1	  | 6	      | 1,8
| Min ilośc	| 120	| 60	| 36	| 180	    |


## Model matematyczny

### Zmienne

x1 -- ilosc zjedzonego produktu P1
x2 -- ilosc zjedzonego produktu P2

### Ograniczenia

6x1 + 3x2 > 120
1x1 + 3x2 > 60
9x1 + 1x2 > 36
6x1 + 6x2 > 180

### Funkcja celu

Z = 1,2x1 + 1,8x2 ---> min


## Rozwiązanie zadania

Rozwiązałem zadanie przy pomocy biblioteki https://mvnrepository.com/artifact/org.ojalgo/ojalgo/47.1.1 w Javie




