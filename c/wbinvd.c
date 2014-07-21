/*
 * For Intel wbinvd instruction
 */
#include <stdio.h>
#include <sys/time.h> // For gettimeofday() and struct timeval

static inline 
void asm_wbinvd()
{
    __asm__ __volatile__("wbinvd");
}

/*******************************/
#define GET_INTERVAL(start, stop) ((stop.tv_sec - start.tv_sec) + \
    (stop.tv_usec - start.tv_usec) * 1.0 / 1000000)
#define SIZE 1024
int buf0[SIZE];
int buf1[SIZE];

int test_func() {
    const int size = 20*1024*1024; // Allocate 20M. Set much larger then L2
    char *c = (char *)malloc(size);
    int i, j;
    // But morden CPU will recognize this partten!
    for (i = 0; i < 0xffff; i++)
        for (j = 0; j < size; j++)
            c[j] = i*j;
}
int main()
{
    int i;
    struct timeval start_time;
    struct timeval stop_time;
    double t0, t1;
    
    // For raw test
    gettimeofday(&start_time, NULL);
    for (i = 0; i < SIZE; i++) {
        buf0[i] = i;
    }
    gettimeofday(&stop_time, NULL);
    t0 = GET_INTERVAL(start_time, stop_time);

    // For wbinvd test
    gettimeofday(&start_time, NULL);
    /*
    for (i = 0; i < SIZE; i++) {
        buf1[i] = i;
    }
    asm_wbinvd();
    */
    // test_func(); 
    gettimeofday(&stop_time, NULL);
    t1 = GET_INTERVAL(start_time, stop_time);
    
    // Print stats
    printf("raw time    : %lf\n", t0);
    printf("wbinvd time : %lf\n", t1);
    return 0;
}
