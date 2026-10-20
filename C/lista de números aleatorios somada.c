#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numeros[10];
    int soma = 0;

    srand(time(NULL));

    for (int i = 0; i < 10; i++) {
        numeros[i] = rand() % 50 + 1;
        soma += numeros[i];
    }

    printf("Lista: ");

    for (int i = 0; i < 10; i++) {
        printf("%d ", numeros[i]);
    }

    printf("\nSoma: %d\n", soma);

    return 0;
}
