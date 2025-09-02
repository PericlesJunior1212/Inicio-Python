def eh_palindromo(lista):
    return lista == lista[::-1]

lista = ["a", "b", "c", "d", "c",  "b", "a"]
lista_2 = ["a", "b", "c", "d", "e", "f", "g"]

print(eh_palindromo(lista))   
