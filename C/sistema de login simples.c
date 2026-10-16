#include <stdio.h>
#include <string.h>

int main() {
    char usuario_correto[] = "admin";
    char senha_correta[] = "12345";

    char usuario_digitado[20];
    char senha_digitada[20];

    printf("--- Sistema de Login ---\n");

    printf("Digite o usuario: ");
    scanf("%19s", usuario_digitado);

    printf("Digite a senha: ");
    scanf("%19s", senha_digitada);

    if (strcmp(usuario_correto, usuario_digitado) == 0) {
        if (strcmp(senha_correta, senha_digitada) == 0) {
            printf("\nLogin realizado com sucesso! Bem-vindo.\n");
        } else {
            printf("\nUsuario ou senha incorretos.\n");
        }
    } else {
        printf("\nUsuario ou senha incorretos.\n");
    }

    return 0;
}
