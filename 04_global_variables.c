#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char key[19] = "FLAG{HERE_IS_FLAG}";

int main(void) {
    char input[19];
    printf("Please enter your serial key: ");
    scanf("%s", input);
    if (!strcmp(input, key)) {
        printf("Well done!\n");
    } else {
        printf("Wrong key!\n");
    }
    return 0;
}
