#include <iostream>
#include <thread>
#include <chrono>

using namespace std;
#define N 100
unsigned int a[N];

void myThread1 (int duration){
    std::this_thread::sleep_for(std::chrono::seconds(duration));
    double time_spent = 0.0;
    clock_t begin = clock();
    for (int i = 0; i < N; i++){
        a[i] = i;
    }
    a[1] = 1;
    for (int s = 2; s < N; s++){
        if (a[s] != 0){
            for (int j = s * 2; j < N; j += s){
                a[j] = 0;
            }
        }
    }
    for (int i = 0; i < N; i++) {
        if (a[i] != 0 && a[i] >1) printf("%d, ", a[i]);
    }
    clock_t end = clock();
    time_spent = (double)(end-begin) / CLOCKS_PER_SEC; 
    printf("\nThe elapsed time is %f seconds\n", time_spent);
}

void myThread2 (int duration){
    std::this_thread::sleep_for(std::chrono::seconds(duration));
    double time_spent = 0.0;
    clock_t begin = clock();
    for (int i = 1; i <= 20; i++){ 
        printf("%d, ", i * i * i);
    }
    clock_t end = clock();
    time_spent = (double)(end-begin) / CLOCKS_PER_SEC;
    printf("\nThe elapsed time is %f seconds\n", time_spent);
}  

int main()
{
    std::thread th1(myThread1, 1);
    std::thread th2(myThread2, 2);
    th1.join();
    th2.join();
    return 0;
}