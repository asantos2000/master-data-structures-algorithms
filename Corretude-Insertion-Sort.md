# Insertion-sort

## Corretude - Invariante de laço

![[Pasted image 20220207180743.png]]

- Inicialização: Ele é verdadeiro antes da primeira iteração do laço. 
- Manutenção: Se ele for verdadeiro antes de uma iteração do laço, permanecerá verdadeiro antes da próxima iteração.
- Término: Quando o laço termina, o invariante nos fornece uma propriedade útil que ajuda a mostrar que o algoritmo é correto.

Exemplo:

- **Inicialização**: Começamos mostrando que o invariante de laço é válido antes da primeira iteração do laço, quando $j = 2$. Então, o subarranjo $A[1 .. j − 1]$ consiste apenas no único elemento $A[1]$, que é de fato o elemento original em $A[1]$. Além disso, esse subarranjo é ordenado (trivialmente, é claro), e isso mostra que o invariante de laço é válido antes da primeira iteração do laço.
- **Manutenção**: Em seguida, abordamos a segunda propriedade: mostrar que cada iteração mantém o invariante de laço. Informalmente, o corpo do laço `for` funciona deslocando $A[ j − 1]$, $A[ j − 2]$, $A[ j − 3]$, e assim por diante, uma posição para a direita até encontrar a posição adequada para $A[j]$ (linhas 4 a 7); nesse ponto ele insere o valor de $A[ j]$ (linha 8). Então, o subarranjo $A[1 .. j]$ consiste nos elementos presentes originalmente em $A[1 .. j]$, mas em sequência ordenada. Portanto, incrementar $j$ para a próxima iteração do laço for preserva o invariante de laço.
- **Término**: Finalmente, examinamos o que ocorre quando o laço termina. A condição que provoca o término do laço `for` é que $j > A⋅comprimento = n$. Como cada iteração do laço aumenta $j$ de $1$, devemos ter $j = n + 1$ nesse instante. Substituindo $j$ por $n + 1$ no enunciado do invariante de laço, temos que o subarranjo $A[1 .. n]$ consiste nos elementos originalmente contidos em $A[1 .. n]$, mas em sequência ordenada. Observando que o subarranjo $A[1 .. n]$ é o arranjo inteiro, concluímos que o arranjo inteiro está ordenado. Portanto o algoritmo está correto.

> Um tratamento mais formal da segunda propriedade nos obrigaria a estabelecer e mostrar um invariante para o laço while das linhas 5–7. Porém, nesse momento, preferimos não nos prender a tal formalismo, e assim contamos com nossa análise informal para mostrar que a segunda propriedade é válida para o laço externo.