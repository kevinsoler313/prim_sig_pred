
📘 Cálculo de Conjuntos FIRST, FOLLOW y PREDICTION para Gramáticas
Este proyecto implementa el análisis sintáctico de gramáticas mediante el cálculo de los conjuntos FIRST, FOLLOW y PREDICTION usando Python.

📚 Descripción
El código define dos gramáticas y utiliza funciones para calcular:

FIRST: Conjunto de símbolos que pueden aparecer al inicio de una derivación de una producción.

FOLLOW: Conjunto de símbolos que pueden seguir a un no terminal en alguna derivación.

PREDICTION: Conjunto de símbolos que predicen qué producción aplicar, útil para construir analizadores predictivos tipo LL(1).

Esto es especialmente útil en cursos de teoría de lenguajes, compiladores o análisis sintáctico.

🧠 Ejemplo de Gramáticas
python
Copiar
Editar
grammar1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']],
    'C': [['cinco', 'D', 'B'], ['ε']],
    'D': [['seis'], ['ε']]
}
python
Copiar
Editar
grammar2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['ε']]
}
⚙️ Uso
Solo necesitas ejecutar el script en Python:

bash
Copiar
Editar
python3 nombre_del_archivo.py
El programa imprimirá para cada gramática:

Los conjuntos FIRST

Los conjuntos FOLLOW

Los conjuntos PREDICTION

📄 Estructura del Código
compute_first(grammar): Calcula el conjunto FIRST de la gramática.

compute_follow(grammar, first_sets, start_symbol): Calcula el conjunto FOLLOW.

compute_predictions(grammar, first_sets, follow_sets): Calcula el conjunto PREDICTION.

Se procesan múltiples gramáticas en una lista gramaticas.
