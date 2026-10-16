#include <stdio.h>

int main(){
    int idade;
    
    printf("digite sua idade");
    scanf("%d", &idade);

    if (idade < 0){
        printf("Você não está vivo");
    }
    else if (idade == 0){
        printf("Voce acabou de nascer");
    }
    else if (idade <= 3){
        printf("Bebe");
    }
    else if (idade <= 11){
        printf("Crianca");
    }
    else if (idade <= 17){
        printf("Adolescente");
    }
    else if (idade <= 29){
        printf("Jovem adulto");
    }
    else if (idade <= 59){
        printf("Adulto");
    }
    else if (idade <= 99){
        printf("Idoso");
    }
    else {
        printf("Voce tem mais de 100 anos!");
    }

    return 0;
}