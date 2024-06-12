#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

void eratosthenesSieve(int n) {
    bool a[n];
    a[1] = 1;
    for (int i = 2; i <= n; i++) {
        a[i] = true;
    }
    for (int i = 2; i * i <= n; i++) {
        if (a[i]) {
            for (int j = i * i; j <= n; j += i) {
                a[j] = false;
            }
        }
    }
    printf("Prime numbers: ");
    for (int i = 2; i <= n; i++) {
        if (a[i]) {
            printf("%i ", i);
        }
    }
    printf("\n");
}

int main() {
    int number;
    printf("Enter number: \n");
    scanf("%i", &number);
    clock_t begin = clock();
    eratosthenesSieve(number);
    printf("The elapsed time is: %.6fs\n", (double)(clock() - begin) / CLOCKS_PER_SEC);
    return 0;
}