#hier zorg dat ik de gebruiker een getal in voert dat opgeslagen wordt in de variable a & b.
a = input("voer een random getal in: ")
b = input("voer nogmaals een random getal toe: ")
#hier zorg ik ervoor dat ik al een waarde aangegeven heb aan de variable min & max.
#Ik gebruik hiervoor int(integer) om een nummer of een str(string) ernaar te converte.
min = int(0)
max = int(0)
#Hier gebruik ik een 'if' statement om te zeggen als a groter is dan b dan wordt er uit geprint  wat de grootste is plus het getal.
if a > b:
    max = a
    min = b
    print('a is het grootste getal: ' + max)
#Hier gebruik ik een 'elif' statement om te zeggen als anders a kleiner is dan b dan wordt er uit geprint  wat de kleinste is plus het getal.
elif a < b:
    max = b
    min = a
    print('a is het kleinste getal: ' + min)
else:
#Hier gebruik ik een 'else' statement om te zeggen als het gelijk is dan wordt a & b uit geprint plus de getallen.
    max = b
    min = a
    print('a: ' + str(min) + ' is even groot als b: ' + str(max))

print('Het minimum: ' + str(min))
print('Het maximum: ' + str(max))
