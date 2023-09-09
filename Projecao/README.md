# MC918 - Lab 01

## Especificações
Algoritmo para criar projeções de poliedros. Código 100% em python, usando apenas bibliotecas padrão.

## Execução
#### Projeção
A projeção de um poliedro P numa direção 'c' é chamada com a seguinte linha de código:

python3 Codigo/Projection.py projecao.in

Sendo projecao.in o nome de um arquivo que contém em sua primeira linha a direção 'c' e nas linhas seguintes o poliedro P (escrito através de suas restrições linha por linha). Um exemplo deste tipo de arquivo está presente no repositório ("projecao.in").

A saída é feita na saída stdout, mostrando o poliedro tal que sua intersecção com um conjunto é equivalente a projeção de P neste conjunto através de 'c', sendo o arquivo "projecao.out" o exemplo de saída para "projecao.in".

#### Checar se é vazio
A checagem de presença de algum elemento em um poliedro P é chamada da seguinte forma:

python3 Codigo/IsItEmpty.py ehVazio.in

Sendo ehVazio.in o nome do arquivo que contém P (escrito através de suas restrições linha por linha). Um exemplo deste tipo de arquivo está presente no repositório ("ehVazio.in") 

A saída é feita na saída stdout, mostrando o poliedro resultante do processo de eliminação seguida da conclusão quanto a presença de algum elemento no poliedro, sendo o arquivo "ehVazio.out" o exemplo de saída para "ehVazio.in".


