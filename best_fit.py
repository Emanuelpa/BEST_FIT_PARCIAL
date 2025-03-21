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
        print("Queda asignado en-> (" + str(hex(selected_row[0])) + ", "+ str(hex(requeriment)) + ")")

        if less == 0:
            print("No sobra nada de ese espacio")
            memory.pop(index)
            index = index % len(memory)
        else:
            new_base = selected_row[0] + requeriment
            new_limit = selected_row[1] - requeriment
            updated_row = (new_base, new_limit)
            memory[index] = updated_row
        return memory, selected_row[0], requeriment, index
    else:
        return None