Sebastian Głowacz
I6E1S1

#Zadanie

Zadanie 1. Przedsiębiorstwo produkuje dwa wyroby. Do ich produkcji zużywa się m.in. dwa
limitowane surowce. Zużycie tych surowców na jednostkę każdego z wyrobów, dopuszczalne limity
zużycia oraz zyski jednostkowe ze sprzedaży podano w tabeli poniżej.

Wyroby: w1, w2

Zużycie surowca na jednostkę:
I: 
dla w1: 12
dla w2: 8
II:
dla w1: 4
dla w2: 8

Zysk jednostkowy [zł]:
dla w1: 50
dla w2: 10

Limit zużycia surowca:
dla I: 480
dla II: 640


#Zadanie optymalizacyjne

1.Ile należy wyprodukować wyrobu w1 , a ile w2 , aby nie przekraczając limitów
zmaksymalizować zysk ze sprzedaży wyrobów?
2.Jak zmieni się rozwiązanie, gdy podjęta zostanie decyzja, że wyrobu w1 , powinno się
produkować nie więcej niż wyrobu w2 ?


#Model matematyczny

funkcja celu: 50w1 + 10w2 -> max

ograniczenia dla punktu 1: 
12w1 + 4w2 <= 480
8w1 + 8w2 <= 640
w1 ,w2 >= 0

dla punktu 2 dodatkowo:
w1 <= w2

#Wynik

1. Aby zmaksymalizować zysk przy zachowaniu limitów należy wyprodukować 40 w1 i 0 w2
2. Gdy w1 jest nie więcej niż w2, należy wyprodukować 30 w1 i 30 w2
