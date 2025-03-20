def first_fit(memory, requeriment, index):
    raise NotImplementedError("first_fit no está implementado aún.")

def worst_fit(memory, requeriment, index):
    raise NotImplementedError("worst_fit no está implementado aún.")

def best_fit(memory, requeriment, index):

    if not memory:
        return None

    if requeriment <= 0 or index < 0:
        return None

    encontered = False
    new_base = 0
    new_limit = 0

    n = len(memory)
    i = index % n
    less = float('inf')
    for _ in range(n):
        row = memory[i]
        if (row[1] >= requeriment) and (row[1] - requeriment) < less:
            less = row[1] - requeriment
            index = i
            encontered = True
        i = (i + 1) % n

    if encontered:
        selected_row = memory[index]
        print("Elige el espacio->",hex(selected_row[0]),hex(selected_row[1]))
        if less == 0:
            print("No sobra nada de ese espacio")
            memory.pop(index)
        else:
            print("Queda asignado en-> (" + str(selected_row[0]) + ", "+ str(requeriment) + ")")
            new_base = selected_row[0] + requeriment
            new_limit = selected_row[1] - requeriment
            updated_row = (new_base, new_limit)
            memory[index] = updated_row
        return memory,new_base,new_limit,index
    else:
        return None


# initial_memory = [(0, 0), (0, 0), (0,0), (0, 0)]
# print("Memoria inicial")
# for row in initial_memory:
#     print(row)

# memory_result,base, limit, index = best_fit(initial_memory ,100, 3)


# if base != None:
#     print("Nueva memoria actualizada")
# else:
#     print("No se encontró un espacio")

# for row in memory_result:
#     print(row)
# print("\n\nProximo indice para iniciar busqueda", index)