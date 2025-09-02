lista = ["a", "b", "c", "d", "c",  "b", "a"]
remove_lista = "c"
nova_lista = []

for remove in remove_lista:
    for item in lista:
        if item != remove:
            nova_lista.append(item)

    print(f"A lista = {lista}")
    print(f"O item removido foi: {remove_lista}")
    print(f"A listaa com o item removido: {nova_lista}")