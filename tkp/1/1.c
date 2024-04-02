#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h>
#include <pthread.h> 
#define N 100 
unsigned int a[N];

void *myThread1(void *vargp)
{
    sleep(1);
    double time_spent = 0.0; 
    clock_t begin = clock();
    for (int i = 0; i < N; i++){
        a[i] = i;
    }
    a[1] = 1;
    for (int s = 2; s < N; s++){
        if (a[s] != 0){
            for (int j = s *2; j < N; j+= s) {
                a[j] = 0;
            }
        }
    }
    for (int i = 0; i < N; i++){
        if (a[i] != 0 && a[i] > 1) printf("%d ", a[i]);
    }
    clock_t end = clock();
    time_spent = (double)(end-begin) / CLOCKS_PER_SEC; 
    printf("\nThe elapsed time is %f seconds\n", time_spent); 
    return NULL;
}

void *myThread2(void *vargp)
{
    sleep(2);
    double time_spent = 0.0;
    clock_t begin = clock();
    for (int i = 1; i <= 20; i++){ 
        printf("%d ", i * i * i);
    }
    clock_t end = clock();
    time_spent = (double)(end-begin) / CLOCKS_PER_SEC;
    printf("\nThe elapsed time is %f seconds\n", time_spent);
    return NULL;
}

int main()
{
    pthread_t th1;
    pthread_create(&th1, NULL, myThread1, NULL);
    pthread_t th2;
    pthread_create(&th2, NULL, myThread2, NULL);
    pthread_join(th1, NULL);
    pthread_join(th2, NULL); 
    exit(0);
}
