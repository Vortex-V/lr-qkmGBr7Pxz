#include <stdio.h>
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage : %s parameter\n", argv[0]);
        return 1;
    }
    printf("Starting program %s \n", argv[0]);
    printf("with %d parameter(s)\n", argc - 1);
    printf("First parameter is %s\n", argv[1]);
    return 0;
}
