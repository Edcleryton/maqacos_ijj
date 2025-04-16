TODOs

1 - Filtragem e Transformação de Listas
- Criamos funções simples: `eh_par` e `multiplicar_por_dois`.
- Usamos `filter()` para selecionar pares.
- Usamos `map()` para multiplicar por 2.
- Ordenamos com `sorted(..., reverse=True)`.

2 - Filtragem e Transformação de Tuplas (Strings e Inteiros)
- Utilizamos `filter()` com uma **função `lambda`** que verifica se o elemento é uma `string` (`isinstance(x, str)`).
- Em seguida, aplicamos `map()` com a função embutida `str.upper` para transformar as strings em letras maiúsculas.
- Ordenamos o resultado com `sorted()` e transformamos a lista final em uma `tuple`.

3 - Filtragem e Transformação de Sets
- Aplicamos `filter()` com uma **função `lambda`** para selecionar apenas as palavras que começam com a letra "a" ou "A" (`x.lower().startswith("a")`).
- Utilizamos `map()` com `str.upper` para transformar as palavras em maiúsculas.
- O conjunto resultante foi ordenado com `sorted()` e transformado de volta em um `set`.

4 - Filtragem e Transformação de Valores de Dicionário
- Extraímos os valores com `dicionario.values()`.
- Criamos `string_maior_que_tres()` para filtrar strings com mais de 3 letras.
- Usamos `map()` com `para_minuscula()` para converter.
- Resultado é uma lista ordenada.