"""
Try-except

Tratarea exceptiilor (identificarea erorilor care apar de-a lungul exceptiei
programului) este implementat blocul try-except

Sintaxa:
try:
    instrictiuni
except:
    instructiuni_tratare_exceptii
else:
    instructiuni_executate_daca_nu_se_ridica_exceptii
finally:
    instructiuni_executate_neconditionat

Regula:
Ordinea blocurilor except trebuie respectate - exception hierarchy -, cele mai 
specifice (subclasele) trebuie sa fie plasate inaintea exceptiilor
instante ale claselor parinte, generice (mai sus in ierarhie, subclase)

"""

# Convertim o suma introdusa de la tastatura dupa o rata a conversie

rata_conversie = 4.9
suma = input('Introduceti suma: ')

try:
    suma = float(suma)  # conversia de la sting la float
except ValueError as e:
    print('Eroare la conversia la float')
except Exception as e:
    print('Eroare la conversie')
else:
    print(f'Suma {suma} convertita este {suma * rata_conversie}')
finally:
    print('Mesaj la final de try except')
