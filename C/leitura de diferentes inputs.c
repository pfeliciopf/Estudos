#include <stdio.h>

int main(){

    int idade;
    float altura;
    char letra_nome;

    scanf("%d", &idade);
    scanf("%f", &altura);
    scanf(" %c", &letra_nome);

    printf("%d\n", idade);
    printf("%f\n", altura);
    printf("%c\n", letra_nome);

    return 0;
}
