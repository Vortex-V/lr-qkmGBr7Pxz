#include <cstdlib>
#include <stdio.h>

int main(int argc, char *argv[]) {
    for (; *argv; ++argv)
        printf("%d\n", atoi(*argv));
}