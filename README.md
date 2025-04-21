Integrantes
Juan David Sanchez Vargas
Kevin Manuel Soler Uribe
Santiago Camacho Teatino



📘 Cálculo de Conjuntos FIRST, FOLLOW y PREDICTION para Gramáticas
Este proyecto implementa el análisis sintáctico de gramáticas mediante el cálculo de los conjuntos FIRST, FOLLOW y PREDICTION usando Python.

📚 Descripción
El código define dos gramáticas y utiliza funciones para calcular:

FIRST: Conjunto de símbolos que pueden aparecer al inicio de una derivación de una producción.

FOLLOW: Conjunto de símbolos que pueden seguir a un no terminal en alguna derivación.

PREDICTION: Conjunto de símbolos que predicen qué producción aplicar, útil para construir analizadores predictivos tipo LL(1).

Esto es especialmente útil en cursos de teoría de lenguajes, compiladores o análisis sintáctico.

🧠 Ejemplo de Gramáticas

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
⚙️ Uso
Solo necesitas ejecutar el script en Python:

bash

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

CONJUNTOS DE PRIMEROS, SIGUIENTES Y PREDICCION DE LAS GRAMATICAS

--------------------------------------------------------------------------------------------------
GRAMATICA 1

--CONJUNTO PRIMEROS-- 
D = ε, seis 
C = cuatro, cinco  
B = ε, tres, cuatro, cinco 
A = ε, dos 
S = dos, uno, tres, cuatro, cinco

--CONJUNTO FOLLOW-- 
S = $ 
A = uno, tres, cuatro, cinco, seis 
B = uno, tres, cuatro, cinco, seis 
C = uno, tres, cuatro, cinco, seis 
D = uno, tres, cuatro, cinco, seis 

--PREDICCIONES-- 
PRED(S -> A B uno) = {'dos', 'uno', 'cuatro', 'cinco', 'tres'}        
PRED(A -> dos B) = {'dos'} 
PRED(A -> ε) = {'cinco', 'tres', 'uno', 'cuatro', 'seis'} 
PRED(B -> C D) = {'cinco', 'cuatro'} 
PRED(B -> tres) = {'tres'} 
PRED(B -> ε) = {'cinco', 'tres', 'uno', 'cuatro', 'seis'} 
PRED(C -> cuatro A B) = {'cuatro'} 
PRED(C -> cinco) = {'cinco'} 
PRED(D -> seis) = {'seis'} 
PRED(D -> ε) = {'cinco', 'tres', 'uno', 'cuatro', 'seis'} 

--------------------------------------------------------------------------------------------------
GRAMATICA 2

--CONJUNTO PRIMEROS-- 
D = ε, seis 
C = ε, cinco 
B = ε, seis, cuatro 
A = ε, tres, seis, cuatro, cinco 
S = tres, seis, cuatro, cinco, uno  

--CONJUNTO FOLLOW-- 
S = $, dos 
A = uno, tres 
B = $, dos, cinco, seis, uno, tres 
C = $, dos, seis, uno, tres 
D = $, dos, uno, tres, cuatro, seis 

--PREDICCIONES-- 
PRED(S -> A uno B C) = {'seis', 'cuatro', 'cinco', 'uno', 'tres'}     
PRED(S -> S dos) = {'seis', 'cuatro', 'cinco', 'uno', 'tres'}         
PRED(A -> B C D) = {'seis', 'cuatro', 'cinco', 'uno', 'tres'}         
PRED(A -> A tres) = {'seis', 'cuatro', 'cinco', 'tres'} 
PRED(A -> ε) = {'uno', 'tres'} 
PRED(B -> D cuatro C tres) = {'seis', 'cuatro'} 
PRED(B -> ε) = {'seis', 'cinco', 'uno', 'tres', 'dos', '$'} 
PRED(C -> cinco D B) = {'cinco'} 
PRED(C -> ε) = {'seis', 'uno', 'tres', 'dos', '$'} 
PRED(D -> seis) = {'seis'} 
PRED(D -> ε) = {'seis', 'cuatro', 'uno', 'tres', 'dos', '$'} 
