/* gettid  : OS thread id, int 
 * pthread_self : POSIX thread id, typedef unsigned long int pthread_t; 
 *           come from /usr/include/bits/pthreadtypes.h 
 * we can get sequence number from passing parameter from pthread_create. 
 *
 * NOTICE:
 * The return value of gettid and pthread_self is not start from 0 !  
 * Always very big.
 **/
#include <pthread.h>
#include <stdio.h>
#include <unistd.h> /* For sleep function */
#include <sys/syscall.h> /* For syscall  */

int gettid()
{
    return syscall(SYS_gettid);
}

#define NUM_THREADS 2

void* thread_main(void *p)
{
    pthread_t tid_posix = pthread_self();
    int tid_os = gettid();
    int *arg = (int *) p;
    int tid_logic = *arg;
    printf("hello thread (POSIX)=%lu (OS)=%d (logic)=%d\n", tid_posix, tid_os, tid_logic);
}


int main()
{
    pthread_t tid[NUM_THREADS];
    int i;
    int ret[NUM_THREADS];

    printf("start:\n");
    for( i = 0; i < NUM_THREADS; ++i){
        /* int phtread_create(pthread_t *thread, const pthread_attr_t *attr,
         *                  void *(*start_routine)(void *), void *arg) */
        ret[i] = pthread_create(&(tid[i]), NULL, &thread_main, &i);
    }
    sleep(1); 
    printf("end\n");
    return 0;
}
