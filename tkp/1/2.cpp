#include <iostream>
#include <string.h>
#include <ctime>

using namespace std;

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

    cout << "Prime numbers: ";
    for (int i = 2; i <= n; i++) {
        if (a[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
}

int main() {
    printf("Enter number: \n");
    int number;
    cin >> number;
    clock_t begin = clock();
    eratosthenesSieve(number);
    printf("The elapsed time is: %.6f sec\n", (double)(clock() - begin) / CLOCKS_PER_SEC);
}