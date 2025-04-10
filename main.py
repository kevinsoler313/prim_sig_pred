
grammar1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']],
    'C': [['cinco', 'D', 'B'], ['ε']],
    'D': [['seis'], ['ε']]
}
grammar2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['ε']]
}

gramaticas = [grammar1,grammar2]



def compute_first(grammar):
    first = {non_terminal: set() for non_terminal in grammar}

    def first_of(symbol):
        # Si el símbolo es terminal
        if not symbol.isupper():
            return {symbol}

        # Si ya está calculado
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





def compute_follow(grammar, first_sets, start_symbol):
    follow = {non_terminal: set() for non_terminal in grammar}
    follow[start_symbol].add('$')  # Símbolo de fin de cadena

    changed = True
    while changed:
        changed = False
        for lhs, productions in grammar.items():
            for production in productions:
                trailer = follow[lhs].copy()
                for symbol in reversed(production):
                    if symbol in grammar:  # es no terminal
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

def compute_predictions(grammar, first_sets, follow_sets):
    predictions = {}
    for lhs, productions in grammar.items():
        for production in productions:
            pred = set()
            
            # Si la producción es ε directamente
            if production == ['ε']:
                pred.update(follow_sets[lhs])
            else:
                for symbol in production:
                    if symbol in grammar:  # No terminal
                        pred.update(first_sets[symbol] - {'ε'})
                        if 'ε' not in first_sets[symbol]:
                            break
                    else:  # Terminal
                        pred.add(symbol)
                        break
                else:
                    # Todos los símbolos derivan ε
                    pred.update(follow_sets[lhs])

            predictions[(lhs, tuple(production))] = pred
    return predictions

valor = 1
for i in gramaticas:
    
    print(f'-----------------------------Gramatica{valor}----------------------------------\n')
    first_sets = compute_first(i)

    # Mostrar resultados
    for non_terminal, first_set in first_sets.items():
        print(f"FIRST({non_terminal}) = {first_set}")

    follow_sets = compute_follow(i, first_sets, start_symbol='S')
    prediction_sets = compute_predictions(i, first_sets, follow_sets)



    print("\nFOLLOW sets:")
    for nt, follow in follow_sets.items():
        print(f"FOLLOW({nt}) = {follow}")

    print("\nPREDICTION sets:")
    for (nt, prod), pred in prediction_sets.items():
        print(f"PRED({nt} -> {' '.join(prod)}) = {pred}")
    valor+=1
