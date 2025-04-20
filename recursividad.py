# Gramática de ejemplo con posible recursividad
grammar5 = {
    'S': [['A', 'B', 'C'], ['D', 'E']],
    'A': [['dos', 'B', 'tres'], ['ε']],
    'B': [['B', 'cuatro', 'C', 'cinco'], ['ε']],
    'C': [['seis', 'A', 'B'], ['ε']],
    'D': [['uno', 'A', 'E'], ['B']],
    'E': [['tres']]
}


gramaticas = [grammar5]

# Detectar recursividad izquierda directa
def tiene_recursividad_izquierda(grammar):
    for nt, producciones in grammar.items():
        for prod in producciones:
            if prod[0] == nt:
                return True
    return False

# Eliminar recursividad izquierda (directa e indirecta)
def eliminar_recursividad_izquierda(grammar):
    nuevos = {}
    nt_list = list(grammar.keys())

    for i in range(len(nt_list)):
        Ai = nt_list[i]
        nuevas_producciones = []

        # Sustituir producciones indirectamente recursivas
        for j in range(i):
            Aj = nt_list[j]
            nuevas = []
            for prod in grammar[Ai]:
                if prod[0] == Aj:
                    for prod2 in nuevos[Aj]:
                        nuevas.append(prod2 + prod[1:])
                else:
                    nuevas.append(prod)
            grammar[Ai] = nuevas

        # Separar producciones recursivas directas y no recursivas
        recursivas = []
        no_recursivas = []
        for prod in grammar[Ai]:
            if prod[0] == Ai:
                recursivas.append(prod[1:])
            else:
                no_recursivas.append(prod)

        if recursivas:
            Ai_prime = Ai + "'"
            while Ai_prime in grammar or Ai_prime in nuevos:
                Ai_prime += "'"

            nuevos[Ai] = []
            nuevos[Ai_prime] = []

            for prod in no_recursivas:
                nuevos[Ai].append(prod + [Ai_prime])

            for prod in recursivas:
                nuevos[Ai_prime].append(prod + [Ai_prime])
            nuevos[Ai_prime].append(['ε'])
        else:
            nuevos[Ai] = grammar[Ai]

    return nuevos

# Calcular FIRST
def compute_first(grammar):
    first = {non_terminal: set() for non_terminal in grammar}

    def first_of(symbol):
        if not symbol.isupper():
            return {symbol}
        if first[symbol]:
            return first[symbol]

        for production in grammar[symbol]:
            for i, sym in enumerate(production):
                sym_first = first_of(sym)
                first[symbol].update(sym_first - {'ε'})

                if 'ε' not in sym_first:
                    break
                elif i == len(production) - 1:
                    first[symbol].add('ε')

        return first[symbol]

    for non_terminal in grammar:
        first_of(non_terminal)

    return first

# Calcular FOLLOW
def compute_follow(grammar, first_sets, start_symbol):
    follow = {non_terminal: set() for non_terminal in grammar}
    follow[start_symbol].add('$')  # Símbolo de fin de entrada

    changed = True
    while changed:
        changed = False
        for lhs, productions in grammar.items():
            for production in productions:
                trailer = follow[lhs].copy()
                for symbol in reversed(production):
                    if symbol in grammar:
                        before = len(follow[symbol])
                        follow[symbol].update(trailer)
                        if 'ε' in first_sets[symbol]:
                            trailer = trailer.union(first_sets[symbol] - {'ε'})
                        else:
                            trailer = first_sets[symbol]
                        if len(follow[symbol]) != before:
                            changed = True
                    else:
                        trailer = {symbol}
    return follow

# Calcular PREDICTION
def compute_predictions(grammar, first_sets, follow_sets):
    predictions = {}
    for lhs, productions in grammar.items():
        for production in productions:
            pred = set()
            if production == ['ε']:
                pred.update(follow_sets[lhs])
            else:
                for symbol in production:
                    if symbol in grammar:
                        pred.update(first_sets[symbol] - {'ε'})
                        if 'ε' not in first_sets[symbol]:
                            break
                    else:
                        pred.add(symbol)
                        break
                else:
                    pred.update(follow_sets[lhs])
            predictions[(lhs, tuple(production))] = pred
    return predictions

# Programa principal
valor = 1
for grammar in gramaticas:
    print(f'----------------------------- Gramática {valor} -----------------------------\n')

    if tiene_recursividad_izquierda(grammar):
        print("⚠️  La gramática tiene recursividad izquierda. Eliminando...\n")
        grammar = eliminar_recursividad_izquierda(grammar)
    else:
        print("✅ La gramática NO tiene recursividad izquierda.\n")

    print("📘 Gramática sin recursividad izquierda:\n")
    for nt, prods in grammar.items():
        for p in prods:
            print(f"{nt} → {' '.join(p)}")
    print()

    # Calcular conjuntos
    first_sets = compute_first(grammar)

    print("🔹 Conjuntos FIRST:")
    for non_terminal, first_set in first_sets.items():
        print(f"FIRST({non_terminal}) = {first_set}")

    follow_sets = compute_follow(grammar, first_sets, start_symbol='S')
    prediction_sets = compute_predictions(grammar, first_sets, follow_sets)

    print("\n🔸 Conjuntos FOLLOW:")
    for nt, follow in follow_sets.items():
        print(f"FOLLOW({nt}) = {follow}")

    print("\n🔮 Conjuntos PREDICTION:")
    for (nt, prod), pred in prediction_sets.items():
        print(f"PRED({nt} → {' '.join(prod)}) = {pred}")

    valor += 1
